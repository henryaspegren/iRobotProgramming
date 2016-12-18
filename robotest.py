#!/usr/bin/env python3

from breezycreate2 import Robot
import time

# Create a Create2. This will automatically try to connect to your robot over serial
bot = Robot()

# Play a note to let us know you're alive!
# bot.playNote('A4', 100)

bot.robot.digit_led_ascii('hi! ')

time.sleep(1)

bot.robot.play_test_sound()

time.sleep(1)

# # Tell the Create2 to turn right slowly
# bot.setTurnSpeed(-50)

time.sleep(1)

bot.setForwardSpeed(100)


time.sleep(1)

bot.setForwardSpeed(-100)

# Wait a second
time.sleep(1)

# Stop
bot.setForwardSpeed(0)

# Report bumper hits and wall proximity for 30 seconds
start_time = time.time()
while (time.time() - start_time) < 30:
	bot._get_sensor_packet()
	print 'Sensor Data: ' + str(bot.robot.sensor_state['cliff front right'])

# Close the connection
bot.close()