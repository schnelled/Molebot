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

####################################################
# Function:     step_0
# Input:         
# Output:       
# Description:
####################################################
def step_0():
	# Set frequency to 60 Hz
	pwm.setPWMFreq(60)

	# Set the pulse width modulation
	pwm.setPWM(0, 0, servoMin)

####################################################
# Function:     step_1
# Input:         
# Output:       
# Description:
####################################################
def step_1():
	# Set frequency to 60 Hz
	pwm.setPWMFreq(60)

	# Set the pulse width modulation
	pwm.setPWM(0, 0, servoMin + 50)

####################################################
# Function:     step_2
# Input:         
# Output:       
# Description:
####################################################
def step_2():
	# Set frequency to 60 Hz
	pwm.setPWMFreq(60)

	# Set the pulse width modulation
	pwm.setPWM(0, 0, servoMid)

####################################################
# Function:     step_3
# Input:         
# Output:       
# Description:
####################################################
def step_3():
	# Set frequency to 60 Hz
	pwm.setPWMFreq(60)

	# Set the pulse width modulation
	pwm.setPWM(0, 0, servoMid + 50)

####################################################
# Function:     step_4
# Input:         
# Output:       
# Description:
####################################################
def step_4():
	# Set frequency to 60 Hz
	pwm.setPWMFreq(60)

	# Set the pulse width modulation
	pwm.setPWM(0, 0, servoMax)

# Define testing functionality
if __name__ == "__main__":
	while (True):
		# Move to position 0
		step_0()

		# Pause for a second
		time.sleep(1)

		# Move to position 1
		step_1()

		# Pause for a second
		time.sleep(1)

		# Move to position 2
		step_2()

		# Pause for a second
		time.sleep(1)

		# Move to position 3
		step_3()

		# Pause for a second
		time.sleep(1)

		# Move to position 4
		step_4()

		# Pause for a second
		time.sleep(1)




