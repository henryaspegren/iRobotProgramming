import time
from breezycreate2 import Robot


"""
This function is used to demo the cliff sensors. 
Position the robot over the edge of something and see how the values change.

Prints outputs of the sensor values for duration seconds (defaults to 60)
"""
def demo_cliff_sensors(duration=60):
	bot = Robot()

	bot.playNote('A4', 100)

	time.sleep(1)

	# Report for 30 seconds
	start_time = time.time()
	while (time.time() - start_time) < duration:
		# this requests a new packet from the robot
		# so we can get a new sensor observation
		bot._get_sensor_packet()
		print "Raw Signal Values"
		print 'Cliff Right: ' + str(bot.robot.sensor_state['cliff right signal'])
		print 'Cliff Front Right: ' + str(bot.robot.sensor_state['cliff front right signal'])
		print 'Cliff Front Left: ' + str(bot.robot.sensor_state['cliff front left signal'])
		print 'Cliff Left: ' + str(bot.robot.sensor_state['cliff left signal'])
		print ' '
		print 'Boolean Values'
		print 'Cliff Right: ' + str(bot.robot.sensor_state['cliff right'])
		print 'Cliff Front Right: ' + str(bot.robot.sensor_state['cliff front right'])
		print 'Cliff Front Left: ' + str(bot.robot.sensor_state['cliff front left'])
		print 'Cliff Left: ' + str(bot.robot.sensor_state['cliff left'])
		print '______________'
		# sleep half a second to make this slower
		time.sleep(0.5)



	# Close the connection
	bot.close()



"""
This function is used to demo the light bumper sensors.

Prints outputs of sensor values for duration seconds (defaults to 60)
"""
def demo_light_bumper_sensors(duration=60):
	bot = Robot()

	bot.playNote('B4', 100)

	time.sleep(1)


	# Report for 30 seconds
	start_time = time.time()
	while (time.time() - start_time) < duration:
		# this requests a new packet from the robot
		# so we can get a new sensor observation
		bot._get_sensor_packet()
		print "Raw Signal Values"
		print 'Light Bumper Right: ' + str(bot.robot.sensor_state['light bump right signal'])
		print 'Light Bumper Front Right: ' + str(bot.robot.sensor_state['light bump front right signal'])
		print 'Light Bumper Front Left: ' + str(bot.robot.sensor_state['light bump front left signal'])
		print 'Light Bumper Left: ' + str(bot.robot.sensor_state['light bump left signal'])
		print ' '
		print 'Boolean Values'
		print 'Light Bumper Right: ' + str(bot.robot.sensor_state['light bumper']['right'])
		print 'Light Bumper Front Right: ' + str(bot.robot.sensor_state['light bumper']['center right'])
		print 'Light Bumper Front Left: ' + str(bot.robot.sensor_state['light bumper']['center left'])
		print 'Light Bumper Left: ' + str(bot.robot.sensor_state['light bumper']['left'])
		print '______________'
		# sleep half a second to make this slower
		time.sleep(0.5)



	# Close the connection
	bot.close()


"""
This function is used to demo the wheel drop sensors.

Prints outputs of sensor values for duration seconds (defaults to 60)
"""
def demo_wheel_drop(duration=60):
	bot = Robot()

	bot.playNote('C4', 100)

	time.sleep(1)


	# Report for 30 seconds
	start_time = time.time()
	while (time.time() - start_time) < duration:
		# this requests a new packet from the robot
		# so we can get a new sensor observation
		bot._get_sensor_packet()
		print 'Drop Right: ' + str(bot.robot.sensor_state['wheel drop and bumps']['drop right'])
		print 'Drop Left: ' + str(bot.robot.sensor_state['wheel drop and bumps']['drop left'])
		print '______________'
		# sleep half a second to make this slower
		time.sleep(0.5)



	# Close the connection
	bot.close()



"""
This function is used to demo the physical bumper sensors.

Prints outputs of sensor values for duration seconds (defaults to 60)
"""
def demo_physical_bumper(duration=60):
	bot = Robot()

	bot.playNote('D4', 100)

	time.sleep(1)


	# Report for 30 seconds
	start_time = time.time()
	while (time.time() - start_time) < duration:
		# this requests a new packet from the robot
		# so we can get a new sensor observation
		bot._get_sensor_packet()
		print 'Bumper Right: ' + str(bot.robot.sensor_state['wheel drop and bumps']['bump right'])
		print 'Bumper Left: ' + str(bot.robot.sensor_state['wheel drop and bumps']['bump left'])
		print '______________'
		# sleep half a second to make this slower
		time.sleep(0.5)



	# Close the connection
	bot.close()


