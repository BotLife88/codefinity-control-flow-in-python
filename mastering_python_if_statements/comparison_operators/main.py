street_temperature = 15
hydration_goal_met = True

running_temp = False

if (10<= street_temperature <=20):
    running_temp = True

# Testing
print("Are the conditions ideal for running now?", running_temp)

# Hydration goal check
if hydration_goal_met == True:
    print("Great job meeting your hydration goal!")