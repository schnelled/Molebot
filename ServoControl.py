# Import needed modules
from Raspi_PWM_Servo_Driver import PWM
import time

# Initialise the PWM device using the default address
# bmp = PWM(0x40, debug=True)
pwm = PWM(0x6F)

# Define constants
servoMin = 275  # Min pulse length out of 4096
servoMax = 475  # Max pulse length out of 4096
servoMid = 375

def setServoPulse(channel, pulse):
	pulseLength = 1000000                   # 1,000,000 us per second
	pulseLength /= 60                       # 60 Hz
	print "%d us per period" % pulseLength
	pulseLength /= 4096                     # 12 bits of resolution
	print "%d us per bit" % pulseLength
	pulse *= 1000
	pulse /= pulseLength
	pwm.setPWM(channel, 0, pulse)

pwm.setPWMFreq(60)                        # Set frequency to 60 Hz

# Declare and initailize the counter
counter = servoMin
while (True):
	# Change speed of continuous servo on channel O
	while counter <= servoMax:
		# Set the pulse width modulation
		pwm.setPWM(0, 0, counter)

		# Pause for a second
		time.sleep(1)

		# Display the value
		print "Current pulse length: " + str(counter)

		# Increament the counter
		counter += 50


	# Reset the position
	counter = servoMin




