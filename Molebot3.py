# Import the needed libraries
from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor
import MotorControl.py
import time
import atexit

# Create a default stepper motor HAT object
mh = Raspi_MotorHAT(addr=0x6f)

# Disable motors on startup
atexit.register(MotorControl.stop(0))

# Create DC motors
leftMotor = mh.getMotor(1)
rightMotor = mh.getMotor(3)

try:
	# Continuously loop
	while(True):

		# Command input
		cmd = input("")

		# Forward command
		if cmd == 'w': MotorControl.forward(1)

		# Backward command
		if cmd == 's': MotorControl.reverse(1)

		# Right turn
		if cmd == 'd': MotorControl.turn_right(1)

		# Left turn
		if cmd == 'a': MotorControl.turn_left(1)

		# Right spin
		if cmd == 'e': MotorControl.spin_right(1)

		# Left spin
		if cmd == 'q': MotorControl.spin_left(1)

		# Stop
		if cmd == 'r': MotorControl.stop(1)
		
# Interrupt from keyboard
except:
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

