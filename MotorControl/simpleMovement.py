# Import needed libraries
import sys
import time
import RPi.GPIO as GPIO

# Define the constant variables
FORWARD_RIGHT = 26
BACKWARD_RIGHT = 20
FORWARD_LEFT = 19
BACKWARD_LEFT = 16

# Cleanup the GPIO before starting
GPIO.cleanup()

# Setup the GPIO in board mode
GPIO.setmode(GPIO.BCM)

# Setup the GPIO input and output
GPIO.setup(FORWARD_RIGHT, GPIO.OUT)
GPIO.setup(BACKWARD_RIGHT, GPIO.OUT)
GPIO.setup(FORWARD_LEFT, GPIO.OUT)
GPIO.setup(BACKWARD_LEFT, GPIO.OUT)

# Function: 	forward
# Input: 		x - the amount of sleep
# Output: 		void
# Definition:	Move the wheel in the forward direction
def forward(x):
	# Set the GPIO forward movement output to HIGH
	GPIO.output(FORWARD_RIGHT, GPIO.HIGH)
	GPIO.output(FORWARD_LEFT, GPIO.HIGH)

	# Display message
	print("Moving Forward")

	# Sleep for x time
	time.sleep(x)

	# Set the GPIO forward movement output to LOW
	GPIO.output(FORWARD_RIGHT, GPIO.LOW)
	GPIO.output(FORWARD_LEFT, GPIO.LOW)

# Function:		reverse
# Input:		x - the amount of sleep
# Output:		void
# Definition:	Move the wheel in the reverse direction
def reverse(x):
	# Set the GPIO reverse movement output to HIGH
	GPIO.output(BACKWARD_RIGHT, GPIO.HIGH)
	GPIO.output(BACKWARD_LEFT, GPIO.HIGH)

	# Display message
	print("Moving Backward")

	# Sleep for x time
	time.sleep(x)

	# Set the GPIO reverse movement output to LOW
	GPIO.output(BACKWARD_RIGHT, GPIO.LOW)
	GPIO.output(BACKWARD_LEFT, GPIO.LOW)

# Continuously loop
while(True):

	# Move the wheel forward for 5 seconds
	forward(5)

	# Move the wheel backward for 5 seconds
	reverse(5)

# Cleanup the GPIO
GPIO.cleanup()
