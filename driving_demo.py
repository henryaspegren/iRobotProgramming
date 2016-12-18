import time
from breezycreate2 import Robot

def seek_edge_and_backup(speed=100):
	bot = Robot()

	# this resets the connection
	time.sleep(1)

	bot.robot.full()

	time.sleep(1)

	bot.robot.play_note('C4', 100)

	time.sleep(1)

	# go forward at speed mm/sec
	bot.setForwardSpeed(100)

	time.sleep(1)

	# keep going forward until run off the edge of the table 
	while True:
		cliff_left, cliff_front_left, cliff_front_right, cliff_right = bot.getCliffSensors()
		print cliff_left, cliff_front_left, cliff_front_right, cliff_right
		if cliff_left or cliff_front_left or cliff_front_right or cliff_right:
			bot.robot.play_note('A4', 200)
			bot.setForwardSpeed(0)
			break

	time.sleep(2)

	# go forward at speed mm/sec
	bot.setForwardSpeed(-100)

	time.sleep(0.5)

	bot.setForwardSpeed(0)
	bot.setTurnSpeed(100)

	time.sleep(0.5)
	angle_moved = 0
	while True:
		bot.robot.get_packet(100)
		angle_moved += bot.robot.sensor_state['angle']
		print angle_moved
		if angle_moved > 32767*180:
			bot.setTurnSpeed(0)
			break

	time.sleep(0.5)

	# go forward at speed mm/sec
	bot.setForwardSpeed(100)

	time.sleep(1)

	# keep going forward until run off the edge of the table 
	while True:
		cliff_left, cliff_front_left, cliff_front_right, cliff_right = bot.getCliffSensors()
		print cliff_left, cliff_front_left, cliff_front_right, cliff_right
		if cliff_left or cliff_front_left or cliff_front_right or cliff_right:
			bot.robot.play_note('A4', 200)
			bot.setForwardSpeed(0)
			break

	time.sleep(2)

	bot.close()


seek_edge_and_backup()

