exercise_time = 8  # Example value for total exercise time in hours
title = ""

if exercise_time >10:
    title = "Super Achiever"
elif 6 <= exercise_time <= 10:
    title = "Hard Worker"
elif 3 <= exercise_time < 6 :
    title = "Getting There"
elif exercise_time < 3:
    title = "Needs Improvement"
else:
    title="Get moving!"
# Testing
print("Your fitness level:", title)