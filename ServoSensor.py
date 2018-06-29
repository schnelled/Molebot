# Import needed modules
import ServoControl
import SensorControl

# Define constants
NUMBER_TRIALS = 5
FAR_PAUSE = 2
NEAR_PAUSE = 1

#####################################################################
# Function:     step_0
# Input:        None 
# Output:       None - void
# Description:	Move the servo to the far right position and obtains
#	distance to object at far right position
#####################################################################
def step_0():
	# Move the servo to the far right position
	ServoControl.step_0()

	# Pause
	time.sleep(FAR_PAUSE)

	# Obtain the distance
	distance = SensorControl.distance()

	# Pause
	time.sleep(FAR_PAUSE)

	# Return the distance
	return distance

# Define testing functionality
if __name__ == "__main__":
	# Initialize a counter
	counter = 0

	# Loop for a fixed amount of trials
	while counter < NUMBER_TRIALS:

		# Move to step 0 and obtain the distance
		tempDist = step_0()

		# Display the distance
		print "Step0 distance: " + str(tempDist)
		
