# Import needed libraries
from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor

# Define constants
LEFT_MOTOR = 1
RIGHT_MOTOR = 3

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
# Function:     stop
# Input:        leftMotor - 
#		rightMotor - 
# Output:       void
# Description:  Release the wheels,stopping movement
####################################################
def stop(leftMotor, rightMotor):
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


