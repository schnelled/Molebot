# Import needed libraries
from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor
import RPi.GPIO as GPIO
import MotorControl
import time
import atexit
import sys

# Define constants
TRIG = 23
ECHO = 24

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
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

# Set the output to low
GPIO.output(TRIG, False)

# Pause for a second
time.sleep(1)

try:
	# Continuously loop
	while (True):
		# Scan ahead for object
		# Set the output to high
		GPIO.output(TRIG, True)

		# Pause for 10 microseconds
		time.sleep(0.00001)

		# Set the output to low
		GPIO.output(TRIG, False)

		# While echo is low record the start time
		while GPIO.input(ECHO) == 0:
			pulseStart = time.time()

		# While echo is high record the end time
		while GPIO.input(ECHO) == 1:
			pulseEnd = time.time()

		# Measure the duration of the pulse
		pulseDuration = pulseEnd - pulseStart

		# Obtain the distance in cm
		distance = pulseDuration * 17150
		
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
			time.sleep(0.5)

			# Stop
			MotorControl.stop(leftMotor, rightMotor)

			# Set the output to high
			GPIO.output(TRIG, True)

			# Pause for 10 microseconds
			time.sleep(0.00001)

			# Set the output to low
			GPIO.output(TRIG, False)

			# While echo is low record the start time
			while GPIO.input(ECHO) == 0:
				pulseStart = time.time()

			# While echo is high record the end time
			while GPIO.input(ECHO) == 1:
				pulseEnd = time.time()

			# Measure the duration of the pulse
			pulseDuration = pulseEnd - pulseStart

			# Obtain the distance in cm
			distance = pulseDuration * 17150


		# Move forward
		MotorControl.forward(leftMotor, rightMotor)
		MotorControl.setSpeed(leftMotor, rightMotor, 175)
			

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
