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

			# Pause for a half second before scan
			time.sleep(0.5)

			# Collect distance data
			distance = SonicSensor.distance()

			# Set the state equal to 0
			state = 0

			# Pause for a half second after scan
			time.sleep(0.5)

			# Display the distance
			print "Step0: " + str(distance)

			# Turn the scanner to step 1
			ServoControl.step_1()

			# Pause for a half second before scan
			time.sleep(0.5)

			# Collect distance data
			tempDist = SonicSensor.distance()


			# Collect distance data if larger
			if tempDist > distance:
				# Collect distance data and change state to 1
				distance = tempDist
				state = 1

			# Pause for a half second after scan
			time.sleep(0.5)

			# Display the distance
			print "Step1: " + str(tempDist)

			# Turn the scanner to step 2
			ServoControl.step_2()

			# Pause for a half second before scan
			time.sleep(0.5)

			# Collect distance data
			tempDist = SonicSensor.distance()

			# Collect distance data if larger
			if tempDist > distance:
				# Collect distance data and change state to 2
				distance = tempDist
				state = 2

			# Pause for a half second after scan
			time.sleep(0.5)

			# Display the distance
			print "Step2: " + str(tempDist)

			# Turn the scanner to step 3
			ServoControl.step_3()

			# Pause for a half second before scan
			time.sleep(0.5)

			# Collect distance data
			tempDist = SonicSensor.distance()

			# Collect distance data if larger
			if tempDist > distance:
				# Collect distance data and change state to 3
				distance = tempDist
				state = 3

			# Pause for a half second after scan
			time.sleep(0.5)

			# Display the distance
			print "Step3: " + str(tempDist)

			# Turn the scanner to step 4
			ServoControl.step_4()

			# Pause for a half second before scan
			time.sleep(0.5)

			# Collect distance data
			tempDist = SonicSensor.distance()

			# Collect distance data if larger
			if tempDist > distance:
				# Collect distance data and change state to 4
				distance = tempDist
				state = 4

			# Pause for a half second after scan
			time.sleep(0.5)

			# Display the distance
			print "Step4: " + str(tempDist)

			# Check the state
			#if state == 0:
				# Turn hard right
				#MotorControl.spinRight(leftMotor, rightMotor)
				#MotorControl.setSpeed(leftMotor, rightMotor, 200)

				# Pause for a second
				#time.sleep(0.35)

				# Stop all movement
				#MotorControl.stop(leftMotor, rightMotor)

			#elif state == 1:
				# Turn right
				#MotorControl.spinRight(leftMotor, rightMotor)
				#MotorControl.setSpeed(leftMotor, rightMotor, 200)

				# Pause for a second
				#time.sleep(0.2)

				# Stop all movement
				#MotorControl.stop(leftMotor, rightMotor)

			#elif state == 2:
				# Go backward
				#MotorControl.reverse(leftMotor, rightMotor)
				#MotorControl.setSpeed(leftMotor, rightMotor, 200)

				# Pause for a second
				#time.sleep(1)

				# Stop all movement
				#MotorControl.stop(leftMotor, rightMotor)

			#elif state == 3:
				# Turn left
				#MotorControl.spinLeft(leftMotor, rightMotor)
				#MotorControl.setSpeed(leftMotor, rightMotor, 200)

				# Pause for a second
				#time.sleep(0.2)

				# Stop all movement
				#MotorControl.stop(leftMotor, rightMotor)

			#else:
				# Turn hard left
				#MotorControl.spinLeft(leftMotor, rightMotor)
				#MotorControl.setSpeed(leftMotor, rightMotor, 200)

				# Pause for a second
				#time.sleep(0.35)

				# Stop all movement
				#MotorControl.stop(leftMotor, rightMotor)


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
