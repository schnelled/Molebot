# Import needed libraries
import RPi.GPIO as GPIO
import time

# Define constants
TRIG = 23
ECHO = 24

# Set the GPIO to BCM mode
GPIO.setmode(GPIO.BCM)

# Initialize the GPIO input and output
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

# Set the output to low
GPIO.output(TRIG, False)

# Measure in progress
print "Distance Measure In Progress"

# Waiting for sensor
print "Waiting For Sensor To Settle"

# Pause for 2 seconds
time.sleep(2)

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

# Round the distance to two decimals of precission
distance = round(distance, 2)

# Display the distance
print "Distance: ", distance, "cm"

# Cleanup the GPIO
GPIO.cleanup()

