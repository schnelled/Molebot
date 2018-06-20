# Import the needed libraries
from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor
import time
import atexit

# Function:     turnOffMotors
# Input:        none
# Output:       void
# Description:  Auto-disables motors on shutdown
def turnOffMotors(mh):
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

while (True):
	print "Forward! "
	leftMotor.run(Raspi_MotorHAT.FORWARD)
    	rightMotor.run(Raspi_MotorHAT.FORWARD)

	print "\tSpeed up..."
	for i in range(255):
		leftMotor.setSpeed(i)
        	rightMotor.setSpeed(i)
		time.sleep(0.01)

	print "\tSlow down..."
	for i in reversed(range(255)):
		leftMotor.setSpeed(i)
        	rightMotor.setSpeed(i)
		time.sleep(0.01)

	print "Backward! "
	leftMotor.run(Raspi_MotorHAT.BACKWARD)
    	rightMotor.run(Raspi_MotorHAT.BACKWARD)

	print "\tSpeed up..."
	for i in range(255):
		leftMotor.setSpeed(i)
        	rightMotor.setSpeed(i)
		time.sleep(0.01)

	print "\tSlow down..."
	for i in reversed(range(255)):
		leftMotor.setSpeed(i)
        	rightMotor.setSpeed(i)
		time.sleep(0.01)

	print "Release"
	leftMotor.run(Raspi_MotorHAT.RELEASE)
    	rightMotor.run(Raspi_MotorHAT.RELEASE)
	time.sleep(1.0)
