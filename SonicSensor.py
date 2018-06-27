# Include needed modules
import RPi.GPIO as GPIO
import time

# Define constants
TRIG = 23
ECHO = 24

####################################################
# Function:     distance
# Input:         
# Output:       
# Description:
####################################################
def distance():
	# Set the trigger output to high
	GPIO.output(TRIG, True)

	# Pause for 10 microseconds
	time.sleep(0.00001)

	# Set the trigger output to low
	GPIO.output(TRIG, False)

	# While echo is in the low state record the start time of the pulse
	while GPIO.input(ECHO) == 0:
		pulseStart = time.time()	

	# While echo is in the high state record the end time of the pulse
	while GPIO.input(ECHO) == 1:
		pulseEnd = time.time()

	# Measure the duration of the pulse
	pulseDuration = pulseEnd - pulseStart

	# Obtain the distance in cm
	distance = pulseDuration * 17150

	# Return the distance
	return distance

# Define testing functionality
if __name__ == "__main__":
	# Set the GPIO to BCM mode
	GPIO.setmode(GPIO.BCM)

	# Initialize the GPIO input and output
	GPIO.setup(TRIG, GPIO.OUT)
	GPIO.setup(ECHO, GPIO.IN)

	# Set the output to low
	GPIO.output(TRIG, False)

	# Pause for a second
	time.sleep(1)

	# Obtain the distance
	distance = distance()

	# Display the distance
	print "The distance: " + str(distance)

