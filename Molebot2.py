# Import the needed libraries
from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor
import time
import atexit

####################################################
# Function:     turnOffMotors
# Input:        mh - 
# Output:       void
# Description:  Auto-disables motors on shutdown
####################################################
def turnOffMotors(mh):
	mh.getMotor(1).run(Raspi_MotorHAT.RELEASE)
	mh.getMotor(2).run(Raspi_MotorHAT.RELEASE)
	mh.getMotor(3).run(Raspi_MotorHAT.RELEASE)
	mh.getMotor(4).run(Raspi_MotorHAT.RELEASE)

####################################################
# Function:     forward
# Input:        leftMotor - 
#		rightMotor - 
# Output:       void
# Description:  Move both wheels forward
####################################################
def forward(leftMotor, rightMotor):
	# Move the left wheel forward
	leftMotor.run(Raspi_MotorHAT.FORWARD)

	# Move the right wheel forward
	rightMotor.run(Raspi_MotorHAT.FORWARD)

####################################################
# Function:     reverse
# Input:        leftMotor - 
#		rightMotor - 
# Output:       void
# Description:  Move both wheels backwards
####################################################
def reverse(leftMotor, rightMotor):
	# Move the left wheel backward
	leftMotor.run(Raspi_MotorHAT.BACKWARD)

	# Move the right wheel backward
	rightMotor.run(Raspi_MotorHAT.BACKWARD)

####################################################
# Function:     turnLeft
# Input:        leftMotor -  
# Output:       void
# Description:  Move the left wheel forward
####################################################
def turnRight(leftMotor, rightMotor):
	# Move the left wheel forward
	leftMotor.run(Raspi_MotorHAT.FORWARD)

	# Stop the right wheel
	rightMotor.run(Raspi_MotorHAT.RELEASE)

####################################################
# Function:     turnRight
# Input:        rightMotor - 
# Output:       void
# Description:  Move the right wheel forward
####################################################
def turnLeft(leftMotor, rightMotor):
	# Move the right wheel forward
	rightMotor.run(Raspi_MotorHAT.FORWARD)

	# Stop the left wheel
	leftMotor.run(Raspi_MotorHAT.RELEASE)

####################################################
# Function:     spinLeft
# Input:        leftMotor - 
#		rightMotor - 
# Output:       void
# Description:  Move the left wheel forward and the
#		right wheel backward
####################################################
def spinRight(leftMotor, rightMotor):
	# Move the left wheel forward
	leftMotor.run(Raspi_MotorHAT.FORWARD)

	# Move the right wheel backward
	rightMotor.run(Raspi_MotorHAT.BACKWARD)

####################################################
# Function:     spinRight
# Input:        leftMotor - 
#		rightMotor - 
# Output:       void
# Description:  Move the right wheels forward and
#		the left wheel backward
####################################################
def spinLeft(leftMotor, rightMotor):
	# Move the right wheel forward
	rightMotor.run(Raspi_MotorHAT.FORWARD)

	# Move the left wheel backward
	leftMotor.run(Raspi_MotorHAT.BACKWARD)
	

####################################################
# Function:     release
# Input:        leftMotor - 
#		rightMotor - 
# Output:       void
# Description:  Release the wheels,stopping movement
####################################################
def release(leftMotor, rightMotor):
	# Stop the right wheel
	rightMotor.run(Raspi_MotorHAT.RELEASE)

	# Stop the left wheel
	leftMotor.run(Raspi_MotorHAT.RELEASE)

####################################################
# Function:     setSpeed
# Input:        leftMotor - 
#		rightMotor - 
#		speed - 
# Output:       void
# Description:  Set the speed to the wheels
####################################################
def setSpeed(leftMotor, rightMotor, speed):
	# Set the speed of the right wheel
	rightMotor.setSpeed(speed)

	# Set the speed of the left wheel
	leftMotor.setSpeed(speed)

# Create a default stepper motor HAT object
mh = Raspi_MotorHAT(addr=0x6f)

# Disable motors on startup
atexit.register(turnOffMotors)

# Create DC motors
leftMotor = mh.getMotor(1)
rightMotor = mh.getMotor(3)

try:
	# Continuously loop
	while (True):
		# Move the device forward
		print "Forward! "
		forward(leftMotor, rightMotor)

		# Speed up the movement by an increament of 1 every 10ms
		print "\tSpeed up..."
		for i in range(255):
			setSpeed(leftMotor, rightMotor, i)
			time.sleep(0.01)

		# Slow down the movement by an increament of 1 every 10ms
		print "\tSlow down..."
		for i in reversed(range(255)):
			setSpeed(leftMotor, rightMotor, i)
			time.sleep(0.01)

		# Move the device backward
		print "Backward! "
		reverse(leftMotor, rightMotor)

		# Speed up the movement by an increament of 1 every 10ms
		print "\tSpeed up..."
		for i in range(255):
			setSpeed(leftMotor, rightMotor, i)
			time.sleep(0.01)

		# Slow down the movement by an increament of 1 every 10ms
		print "\tSlow down..."
		for i in reversed(range(255)):
			setSpeed(leftMotor, rightMotor, i)
			time.sleep(0.01)

		# Turn the device to the right
		print "Turn right"
		turnRight(leftMotor, rightMotor)

		# Speed up the movement by an increament of 1 every 10ms
		print "\tSpeed up..."
		for i in range(255):
			setSpeed(leftMotor, rightMotor, i)
			time.sleep(0.01)

		# Slow down the movement by an increament of 1 every 10ms
		print "\tSlow down..."
		for i in reversed(range(255)):
			setSpeed(leftMotor, rightMotor, i)
			time.sleep(0.01)

		# Turn the device to the left
		print "Turn left"
		turnLeft(leftMotor, rightMotor)

		# Speed up the movement by an increament of 1 every 10ms
		print "\tSpeed up..."
		for i in range(255):
			setSpeed(leftMotor, rightMotor, i)
			time.sleep(0.01)

		# Slow down the movement by an increament of 1 every 10ms
		print "\tSlow down..."
		for i in reversed(range(255)):
			setSpeed(leftMotor, rightMotor, i)
			time.sleep(0.01)

		# Spin the device to the right
		print "Spin right"
		spinRight(leftMotor, rightMotor)

		# Speed up the movement by an increament of 1 every 10ms
		print "\tSpeed up..."
		for i in range(255):
			setSpeed(leftMotor, rightMotor, i)
			time.sleep(0.01)

		# Slow down the movement by an increament of 1 every 10ms
		print "\tSlow down..."
		for i in reversed(range(255)):
			setSpeed(leftMotor, rightMotor, i)
			time.sleep(0.01)

		# Spin the device to the left
		print "Spin left"
		spinLeft(leftMotor, rightMotor)

		# Speed up the movement by an increament of 1 every 10ms
		print "\tSpeed up..."
		for i in range(255):
			setSpeed(leftMotor, rightMotor, i)
			time.sleep(0.01)

		# Slow down the movement by an increament of 1 every 10ms
		print "\tSlow down..."
		for i in reversed(range(255)):
			setSpeed(leftMotor, rightMotor, i)
			time.sleep(0.01)

		# Release the device
		print "Release"
		release(leftMotor, rightMotor)
		time.sleep(1.0)

# Handle the keyboard interrupt
except KeyboardInterrupt:
	# Display message
	print "Exiting program"

	# Release the device
	release(leftMotor, rightMotor)

	# Exit the program
	sys.exit()
	
