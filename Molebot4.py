# Import needed libraries
from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor
import RPi.GPIO as GPIO
import MotorControl
import SonicSensor
import time
import atexit
import sys

####################################################
# Function:     turnOffMotors
# Input:        mh - 
# Output:       void
# Description:  Auto-disables motors on shutdown
####################################################
def turnOffMotors():
	mh.getMotor(1).run(Raspi_MotorHAT.RELEASE)
	mh.getMotor(2).run(Raspi_MotorHAT.RELEASE)
	mh.getMotor(3).run(Raspi_MotorHAT.RELEASE)
	mh.getMotor(4).run(Raspi_MotorHAT.RELEASE)

# Declare stuck counter
counter = 0

# Create a default stepper motor HAT object
mh = Raspi_MotorHAT(addr=0x6f)

# Disable motors on startup
atexit.register(turnOffMotors)

# Create DC motors
leftMotor = mh.getMotor(1)
rightMotor = mh.getMotor(3)

# Set the GPIO to BCM mode
GPIO.setmode(GPIO.BCM)

# Initialize the GPIO input and output
GPIO.setup(SonicSensor.TRIG, GPIO.OUT)
GPIO.setup(SonicSensor.ECHO, GPIO.IN)

# Set the output to low
GPIO.output(SonicSensor.TRIG, False)

# Pause for a second
time.sleep(1)

try:
	# Continuously loop
	while (True):
		# Scan ahead for object
		distance = SonicSensor.distance()
		
		# Check if object is in range
		while distance < 20:
			# Stop
			MotorControl.stop(leftMotor, rightMotor)

			# Pause for a second
			time.sleep(1)

			# Spin to the right
			MotorControl.spinRight(leftMotor, rightMotor)
			MotorControl.setSpeed(leftMotor, rightMotor, 175)

			# Pause for a half second
			time.sleep(0.25)

			# Stop
			MotorControl.stop(leftMotor, rightMotor)

			# Scan ahead for object
			distance = SonicSensor.distance()

			# Increament the value of the counter
			counter += 1

			# Check if the robot is stuck
			while counter >= 3:

				# Reverse the robot
				MotorControl.reverse(leftMotor, rightMotor)
				MotorControl.setSpeed(leftMotor, rightMotor, 175)

				# Wait a second
				time.sleep(1)

				# Turn around the robot
				MotorControl.spinRight(leftMotor, rightMotor)
				MotorControl.setSpeed(leftMotor, rightMotor, 175)

				# Stop
				MotorControl.stop(leftMotor, rightMotor)

				# Scan ahead for object
				distance = SonicSensor.distance()

				# Check the distance
				if distance > 20:
				
					# Reset the counter
					counter = 0
			
		# Move forward
		MotorControl.forward(leftMotor, rightMotor)
		MotorControl.setSpeed(leftMotor, rightMotor, 175)

		# Reset the counter
		counter = 0
			

# Handle the keyboard interrupt
except KeyboardInterrupt:
	# Display message
	print ("Exiting program")

	# Release the device
	MotorControl.turnOffMotors()

	# Cleanup the GPIO
	GPIO.cleanup()

	# Exit the program
	sys.exit()
