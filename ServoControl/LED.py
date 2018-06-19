import RPi.GPIO as GPIO
import time
import sys

# Declare constant variable
LED_PIN = 18
FREQ = 50

# Set the pin mode to BCM numbering
GPIO.setmode(GPIO.BCM)

# Disable the warnings
GPIO.setwarnings(False)

# Setup GPIO pin 18 as output
GPIO.setup(LED_PIN, GPIO.OUT)

# Setup PWM with frequency of 50MHz
pwm_led = GPIO.PWM(LED_PIN, FREQ)

# Start the PWM with 100% duty cycle
pwm_led.start(100)

try:
	# Continuously loop
	while(True):
		# Obtain user input for brightness
		duty_s = input("Enter brightness value (0 to 100):")

		# Convert into integer value
		duty = int(duty_s)

		# Change the duty cycle of the PWM
		pwm_led.ChangeDutyCycle(duty)

		# Sleep for a second
		time.sleep(1)

# Interrupt from keyboard
except KeyboardInterrupt:
	# Display exit interrupt message
	print("Exiting program")

# Error occured
except:
	# Display error message
	print("Error occurs, exiting program")

# Cleanup the GPIO and exit the program
finally:
	GPIO.cleanup()
	sys.exit()
