steps_taken = 9000
step_goal = 10000
calories_burned = 350
calorie_goal = 500
morning_exercise = False

all_conditions_met = True

# Rewrite this using a single if statement
if steps_taken <= step_goal and calories_burned<=calorie_goal and morning_exercise==False:
    all_conditions_met = False

# Testing
print("Have all conditions been met?", all_conditions_met)