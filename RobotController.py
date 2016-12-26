from breezycreate2 import Robot 
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from threading import Thread, Event
import numpy as np
import time
import math

class RobotController(object):

	"""docstring for RobotController"""

	def __init__(self):
		# robot starts at origin 
		# facing upward along y axis
		self.velocity = 0
		self.angle = 0
		self.position = (0, 0)
		self.radius = 0
		self.bot = Robot()
		self.visualizer = RobotStateVisualizer()

	def test(self):
		self.bot._get_sensor_packet()
		stop_event = Event()
		sensor_thread = Thread(target = self.update_plot_loop, args = [stop_event])
		sensor_thread.start()

		self.turn_robot_to_angle(90)
		time.sleep(10)
		print 'here'
		# self.bot.robot.drive(100, 0)
		# self.set_velocity(100)
		# self.set_radius(0)
		# time.sleep(1)
		# self.bot.robot.drive(100, -1)
		# self.set_velocity(100)
		# self.set_radius(1)
		# time.sleep(1)
		# self.bot.robot.drive(100, 0)
		# self.set_velocity(100)
		# self.set_radius(0)
		# time.sleep(2)
		# self.bot.robot.drive(0, 0)
		# self.set_velocity(0)
		# self.set_radius(0)
		# time.sleep(1)

		# now triger the stopping event
		stop_event.set()

	def get_sensor_data(self):
		# get a new packet
		self.bot._get_sensor_packet()

		# get this data from the sensors
		distance_traveled = self.bot.robot.sensor_state['distance']
		angle_turned = self.bot.robot.sensor_state['angle']

		# if turning we don't need to update distance
		if self.bot.robot.sensor_state['requested radius'] != 0:
			distance_traveled = 0

		# to crudely reduce sensor noise we are going to cap these values
		# to a reasonable domain
		distance_traveled = max(min(100, distance_traveled), -100)
		angle_turned = max(min(25, angle_turned), -25)

		current_angle = self.get_angle()

		# simplifying assumption here
		avg_angle = current_angle+(angle_turned/2)


		# current position
		(x, y) = self.get_position()

		# calculate new position 
		x_new = x + math.cos(math.radians(avg_angle))*distance_traveled
		y_new = y + math.sin(math.radians(avg_angle))*distance_traveled

		# save new position and angle
		self.set_position(x_new, y_new)
		self.set_angle((current_angle+angle_turned) % 360)


	def turn_robot_to_angle(self, target_angle, speed_turning=500, error_threshold=5):
		self.bot.robot.drive(0, 0)
		self.set_velocity(0)
		print 'current angle: ', self.angle
		print 'target angle: ', target_angle
		print 'difference: ', target_angle - self.angle

		while abs(self.angle-target_angle) > error_threshold:
			# print 'current angle: ', self.angle
			difference = self.angle - target_angle
			if difference > 0 and difference < 180:
				if self.get_radius() != 1 or self.get_velocity() != 0:
					print 'setting drive speed'
					print self.get_radius()
					print self.get_velocity()
					self.bot.robot.drive(25, 1)
					self.set_velocity(50)
					self.set_radius(1)
			else:
				if self.get_radius() != -1 or self.get_velocity() != 0:
					print 'setting drive speed'
					print self.get_radius()
					print self.get_velocity()
					self.bot.robot.drive(25, -1)
					self.set_velocity(50)
					self.set_radius(-1)

		self.bot.robot.drive(0, 0)
		return 


	def go_to_position(self, x_target, y_target, speed_turning=25, speed_straight=50, distance_threshold=50, angle_threshold=5):
		(x_current, y_current) = self.get_position()
		print 'currently: ', x_current, y_current, self.angle

		# if close enough just stop
		if abs(x_current - x_target) < distance_threshold and abs(y_current - y_target) < distance_threshold:
			self.bot.robot.drive(0, 0)
			return

		# calculate direction to point
		if x_target == x_current:
			if y_target >= y_target:
				target_angle = 90
			else:
				target_angle = 180
		else:
			target_angle = np.degrees(np.arctan((y_target-y_current)/float(
				x_target - x_current)))

		print 'target: ', x_target, y_target, target_angle


		# turn if needed
		if abs(target_angle-self.angle) > angle_threshold:
			if target_angle - self.angle < 180 and target_angle - self.angle > 0:
				self.bot.robot.drive(speed_turning, 1)
			else:
				self.bot.robot.drive(speed_turning, -1)

			while abs(self.angle-target_angle) > angle_threshold:
	 			continue

 		# now drive straight
 		self.bot.robot.drive(speed_straight, 0)

		# then recurse (updating path)
		return self.go_to_position(x_target, y_target, speed_turning=speed_turning, speed_straight=speed_straight, distance_threshold=distance_threshold, angle_threshold=angle_threshold)


	def get_velocity(self):
		return self.velocity

	def set_velocity(self, velocity):
		self.velocity = velocity

	def get_position(self):
		return self.position

	def set_position(self, x, y):
		self.position = (x, y)

	def set_angle(self, angle):
		self.angle = angle

	def get_angle(self):
		return self.angle

	def set_radius(self, radius):
		self.radius = radius

	def get_radius(self):
		return self.radius

	def update_plot(self):
		# get new sensor data
		self.get_sensor_data()
		self.visualizer.update_plot(self.get_position(), self.get_velocity(), self.get_angle())

	def update_plot_loop(self, stop_event):
		# this will loop until the stop event is triggered
		while (not stop_event.is_set()):
			self.update_plot()


class RobotStateVisualizer(object):

	def __init__(self):

		self.time_step = 0
		self.fig = plt.figure()
		plt.ion()
		gs = gridspec.GridSpec(4,2)
		self.position = plt.subplot(gs[:2, :])
		plt.title('Position of Robot')
		self.velocity = plt.subplot(gs[3, :1])
		plt.title('Velocity')
		self.angle = plt.subplot(gs[3, 1:]) 
		plt.title('Angle')
		plt.show()

	def update_plot(self, position, velocity, angle, pause_interval=0.001):
		self.position.scatter(position[0], position[1])
		self.velocity.scatter(self.time_step, velocity)
		self.angle.scatter(self.time_step, angle)
		self.time_step += 1
		plt.show()
		plt.pause(pause_interval)


rc = RobotController().test()
