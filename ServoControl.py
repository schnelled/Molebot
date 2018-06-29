# Import needed modules
from Raspi_PWM_Servo_Driver import PWM
import time

# Initialise the PWM device using the default address
# bmp = PWM(0x40, debug=True)
pwm = PWM(0x6F)

# Define constants
SERVO_MIN = 275  # Min pulse length out of 4096
SERVO_MAX = 475  # Max pulse length out of 4096
SERVO_MID = 375

####################################################
# Function:     step_0
# Input:        None 
# Output:       None - void
# Description:
####################################################
def step_0():
	# Set frequency to 60 Hz
	pwm.setPWMFreq(60)

	# Set the pulse width modulation
	pwm.setPWM(0, 0, SERVO_MIN)

####################################################
# Function:     step_1
# Input:        None
# Output:       None - void
# Description:
####################################################
def step_1():
	# Set frequency to 60 Hz
	pwm.setPWMFreq(60)

	# Set the pulse width modulation
	pwm.setPWM(0, 0, SERVO_MIN + 50)

####################################################
# Function:     step_2
# Input:        None
# Output:       None - void
# Description:
####################################################
def step_2():
	# Set frequency to 60 Hz
	pwm.setPWMFreq(60)

	# Set the pulse width modulation
	pwm.setPWM(0, 0, SERVO_MID)

####################################################
# Function:     step_3
# Input:        None
# Output:       None - Void
# Description:
####################################################
def step_3():
	# Set frequency to 60 Hz
	pwm.setPWMFreq(60)

	# Set the pulse width modulation
	pwm.setPWM(0, 0, SERVO_MID + 50)

####################################################
# Function:     step_4
# Input:        None
# Output:       None - Void
# Description:
####################################################
def step_4():
	# Set frequency to 60 Hz
	pwm.setPWMFreq(60)

	# Set the pulse width modulation
	pwm.setPWM(0, 0, SERVO_MAX)

# Define testing functionality
if __name__ == "__main__":
	while (True):
		# Move to position 0
		step_0()

		# Pause movement
		time.sleep(1)

		# Move to position 1
		step_1()

		# Pause movement
		time.sleep(1)

		# Move to position 2
		step_2()

		# Pause movement
		time.sleep(1)

		# Move to position 3
		step_3()

		# Pause movement
		time.sleep(1)

		# Move to position 4
		step_4()

		# Pause movement
		time.sleep(1)

