steps_taken = 8500
step_goal = 10000

result_more_than_90 = False  # Default value

if steps_taken >= step_goal *.9:
    result_more_than_90 = True
    print("Great job! You've reached more than 90% of your goal!")
else:
    steps_left = step_goal - steps_taken
    print(f"Keep going! You still need {steps_left} more steps to reach your goal.")