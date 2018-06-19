# Import needed libraries
import sys
import time
import RPi.GPIO as GPIO

# Define the constant variables
FORWARD = 26
BACKWARD = 20

# Cleanup the GPIO before starting
GPIO.cleanup()

# Setup the GPIO in board mode
GPIO.setmode(GPIO.BCM)

# Setup the GPIO input and output
GPIO.setup(FORWARD, GPIO.OUT)
GPIO.setup(BACKWARD, GPIO.OUT)

# Function: 	forward
# Input: 	x - the amount of sleep
# Output: 	void
# Definition:	Move the wheel in the forward direction
def forward(x):
	# Set the GPIO forward movement output to HIGH
	GPIO.output(FORWARD, GPIO.HIGH)

	# Display message
	print("Moving Forward")

	# Sleep for x time
	time.sleep(x)

	# Set the GPIO forward movement output to LOW
	GPIO.output(FORWARD, GPIO.LOW)

# Function:	reverse
# Input:	x - the amount of sleep
# Output:	void
# Definition:	Move the wheel in the reverse direction
def reverse(x):
	# Set the GPIO reverse movement output to HIGH
	GPIO.output(BACKWARD, GPIO.HIGH)

	# Display message
	print("Moving Backward")

	# Sleep for x time
	time.sleep(x)

	# Set the GPIO reverse movement output to LOW
	GPIO.output(BACKWARD, GPIO.LOW)

# Continuously loop
while(True):

	# Move the wheel forward for 5 seconds
	forward(5)

	# Move the wheel backward for 5 seconds
	reverse(5)

# Cleanup the GPIO
GPIO.cleanup()
