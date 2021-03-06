# Import needed libraries
import sys
import time
import RPi.GPIO as GPIO
import MotorControl

# Cleanup the GPIO before starting
GPIO.cleanup()

# Setup the GPIO in BCM mode
GPIO.setmode(GPIO.BCM)

# Setup the GPIO outputs
GPIO.setup(MotorControl.FORWARD_RIGHT, GPIO.OUT)
GPIO.setup(MotorControl.BACKWARD_RIGHT, GPIO.OUT)
GPIO.setup(MotorControl.FORWARD_LEFT, GPIO.OUT)
GPIO.setup(MotorControl.BACKWARD_LEFT, GPIO.OUT)

try:
    # Continuously loop
    while(True):
        # Move both wheels forward
        MotorControl.forward(5)

        # Move both wheels backward
        MotorControl.reverse(5)

        # Turn to the right
        MotorControl.turn_right(5)

        # Turn to the left
        MotorControl.turn_left(5)

        # Spin to the right
        MotorControl.spin_right(5)

        # Spin to the left
        MotorControl.spin_left(5)

# Interrupt from keyboard
except KeyboardInterrupt:
    # Display interrupt message
    print("Exiting Program")

# Error occured
except:
    # Display error message
    print("Error occurs, exiting program")

# Cleanup the GPIO and exit the program
finally:
    # Cleanup the GPIO
    GPIO.cleanup()
    sys.exit()
