# Import the needed libraries
from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor
import MotorControl
import atexit
import sys

# Create a default stepper motor HAT object
mh = Raspi_MotorHAT(addr=0x6f)

# Disable motors on startup
atexit.register(MotorControl.turnOffMotors(mh))

# Create DC motors
leftMotor = mh.getMotor(1)
rightMotor = mh.getMotor(3)

try:
	# Continuously loop
	while (True):

		# Command from keyboard
		cmd = input("")

		# Move forward
		if cmd == 'w':
			MotorControl.forward(leftMotor, rightMotor)
			MotorControl.setSpeed(leftMotor, rightMotor, 150)

		# Move backward
		if cmd == 's':
			MotorControl.reverse(leftMotor, rightMotor)
			MotorControl.setSpeed(leftMotor, rightMotor, 150)

		# Turn right
		if cmd == 'd':
			MotorControl.turnRight(leftMotor, rightMotor)
			MotorControl.setSpeed(leftMotor, rightMotor, 150)

		# Turn left
		if cmd == 'a':
			MotorControl.turnLeft(leftMotor, rightMotor)
			MotorControl.setSpeed(leftMotor, rightMotor, 150)

		# Spin right
		if cmd == 'e':
			MotorControl.spinRight(leftMotor, rightMotor)
			MotorControl.setSpeed(leftMotor, rightMotor, 150)

		# Spin left
		if cmd == 'q':
			MotorControl.spinLeft(leftMotor, rightMotor)
			MotorControl.setSpeed(leftMotor, rightMotor, 150)

		# Stop
		if cmd == 'r':
			MotorControl.stop(leftMotor, rightMotor)
		
# Handle the keyboard interrupt
except KeyboardInterrupt:
	# Display message
	print "Exiting program"

	# Release the device
	MotorControl.turnOffMotors()

	# Exit the program
	sys.exit()
