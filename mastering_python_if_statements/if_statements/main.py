calories_burned = 200
calories_goal = 300

calories_goal_met = False  # default value

# Check calories
if calories_burned >= calories_goal:
    calories_goal_met = "True"

# Testing
print("Is the goal for burned calories met?", calories_goal_met)