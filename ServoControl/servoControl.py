import RPi.GPIO as GPIO
import time

# Define constant variables
LED = 18
FRQ = 50

# Setup the GPIO for BCM
GPIO.setmode(GPIO.BCM)

# Turn of the GPIO warnings
GPIO.setwarnings(False)

# Setup the led on GPIO pin 18
GPIO.setup(LED,GPIO.OUT)

# Setup the PWM with a 50MHz frequency
p = GPIO.PWM(LED, FRQ)

# Start the PWM
p.start(7.5)

try:
	while(True):
		# Change the duty cycle
		p.ChangeDutyCycle(7.5)

		# Sleep for 1 second
		time.sleep(1)

		# Change the duty cycle
		p.ChangeDutyCycle(12.5)

		# Sleep for 1 seconds
		time.sleep(1)

		# Change the duty cycle
		p.ChangeDutyCycle(2.5)

		# Sleep for 1 second
		time.sleep(1)

# Handle the keyboard interrupt
except KeyboardInterrupt:
	# Stop the PWM
	p.stop()
	# Cleanup the GPIO
	GPIO.cleanup()
