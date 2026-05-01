steps_taken = 12000
step_goal = 10000
calories_burned = 350
calorie_goal = 500

result_message = False

if steps_taken >= step_goal or calories_burned>=calorie_goal:
        result_message = True
        print("Great job, you've reached at least one goal")