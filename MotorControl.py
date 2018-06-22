# Import needed libraries
import time
import RPi.GPIO as GPIO

# Define the constant variables for motor movement
FORWARD_RIGHT = 26
BACKWARD_RIGHT = 20
FORWARD_LEFT = 19
BACKWARD_LEFT = 16

# Set GPIO to BCM mode
GPIO.setmode(GPIO.BCM)

# Function: 	forward
# Input: 		x - the amount of sleep
# Output: 		void
# Definition:	Move forward both wheels
def forward(x):
	# Set both the forward output to HIGH
	GPIO.output(FORWARD_RIGHT, GPIO.HIGH)
	GPIO.output(FORWARD_LEFT, GPIO.HIGH)

	# Display message
	print("Moving Forward")

	# Sleep for x time
	time.sleep(x)

	# Set both the forward movement output to LOW
	GPIO.output(FORWARD_RIGHT, GPIO.LOW)
	GPIO.output(FORWARD_LEFT, GPIO.LOW)

# Function:		reverse
# Input:		x - the amount of sleep
# Output:		void
# Definition:	Move in reverse both wheels
def reverse(x):
    	# Set both the reverse output to HIGH
    	GPIO.output(BACKWARD_RIGHT, GPIO.HIGH)
    	GPIO.output(BACKWARD_LEFT, GPIO.HIGH)

   	# Display message
   	print("Moving Backward")

    	# Sleep for x time
    	time.sleep(x)

    	# Set both the reverse output to LOW
    	GPIO.output(BACKWARD_RIGHT, GPIO.LOW)
    	GPIO.output(BACKWARD_LEFT, GPIO.LOW)

# Function:     turn_right
# Input:        x - the amount of sleep
# Output:       void
# Definition:   Move the right wheel forward
def turn_right(x):
    	# Set the right forward output to HIGH
    	GPIO.output(FORWARD_RIGHT, GPIO.HIGH)

    	# Display message
    	print("Moving Right")

    	# Sleep for x time
    	time.sleep(x)

    	# Set the right forward output to LOW
    	GPIO.output(FORWARD_RIGHT, GPIO.LOW)

# Function:     turn_left
# Input:        x - the amount of sleep
# Output:       void
# Definition:   Move the left wheel forward
def turn_left(x):
    	# Set the left forward output to HIGH
    	GPIO.output(FORWARD_LEFT, GPIO.HIGH)

    	# Display message
    	print("Moving Left")

    	# Sleep for x time
    	time.sleep(x)

    	# Set the left forward output to LOW
   	GPIO.output(FORWARD_LEFT, GPIO.LOW)

# Function:     double_right
# Input:        x - the amount of sleep
# Output:       void
# Definition:   Turn the right wheel forward and the left wheel backward
def spin_right(x):
    	# Set the right forward output to HIGH
    	# Set the left reverse output to HIGH
    	GPIO.output(FORWARD_RIGHT, GPIO.HIGH)
    	GPIO.output(BACKWARD_LEFT, GPIO.HIGH)

    	# Display message
    	print("Spinning Right")

    	# Sleep for x time
    	time.sleep(x)

    	# Set the right forward output to LOW
    	# Set the left reverse output to LOW
    	GPIO.output(FORWARD_RIGHT, GPIO.LOW)
    	GPIO.output(BACKWARD_LEFT, GPIO.LOW)

# Function:     double_left
# Input:        x - the amount of sleep
# Output:       void
# Definition:   Turn the left wheel forward and the right wheel backward
def spin_left(x):
    	# Move the left forward output to HIGH
    	# Move the right reverse output to HIGH
    	GPIO.output(FORWARD_LEFT, GPIO.HIGH)
    	GPIO.output(BACKWARD_RIGHT, GPIO.HIGH)

    	# Display message
    	print("Spinning Left")

    	# Sleep for x time
    	time.sleep(x)

    	# Set the left forward output to LOW
    	# Set the right forward output to LOW
    	GPIO.output(FORWARD_LEFT, GPIO.LOW)
    	GPIO.output(BACKWARD_RIGHT, GPIO.LOW)

# Function:		stop
# Input:		x -  the amount of sleep
# Output:		void
# Definition:	Both wheels stop movement
def stop(x):
	# Set the all GPIOs to low
	GPIO.output(FORWARD_LEFT, GPIO.LOW)
	GPIO.output(FORWARD_RIGHT, GPIO.LOW)
	GPIO.output(BACKWARD_LEFT, GPIO.LOW)
	GPIO.output(BACKWARD_RIGHT, GPIO.LOW)

	# Display message
    	print("Stopping")

    	# Sleep for x time
    	time.sleep(x)
	
