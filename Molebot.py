# Import needed libraries
from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor
import RPi.GPIO as GPIO
import MotorControl
import SonicSensor
import ServoControl
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
		# Set default position
		ServoControl.step_2()
				
		# Scan ahead for object
		distance = SonicSensor.distance()
		
		# Check if object is in range
		while distance < 20:
			# Stop
			MotorControl.stop(leftMotor, rightMotor)

			# Turn the scanner to step 0
			ServoControl.step_0()

			# Pause for a second
			time.sleep(0.5)

			# Collect distance data
			distance = SonicSensor.distance()

			# Pause for a second
			time.sleep(0.5)

			# Display the distance
			print "Step0: " + str(distance)

			# Turn the scanner to step 1
			ServoControl.step_1()

			# Pause for a second
			time.sleep(0.5)

			# Collect distance data if larger
			if SonicSensor.distance() > distance:
				distance = SonicSensor.distance()

			# Pause for a second
			time.sleep(0.5)

			# Display the distance
			print "Step1: " + str(distance)

			# Turn the scanner to step 2
			ServoControl.step_2()

			# Pause for a second
			time.sleep(0.5)

			# Collect distance data if larger
			if SonicSensor.distance() > distance:
				distance = SonicSensor.distance()

			# Pause for a second
			time.sleep(0.5)

			# Display the distance
			print "Step2: " + str(distance)

			# Turn the scanner to step 3
			ServoControl.step_3()

			# Pause for a second
			time.sleep(0.5)

			# Collect distance data if larger
			if SonicSensor.distance() > distance:
				distance = SonicSensor.distance()

			# Pause for a second
			time.sleep(0.5)

			# Display the distance
			print "Step3: " + str(distance)

			# Turn the scanner to step 4
			ServoControl.step_4()

			# Pause for a second
			time.sleep(0.5)

			# Collect distance data if larger
			if SonicSensor.distance() > distance:
				distance = SonicSensor.distance()

			# Pause for a second
			time.sleep(0.5)

			# Display the distance
			print "Step4: " + str(distance)

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
