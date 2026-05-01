heart_rate = 135
zone = ""

if heart_rate >= 150:
    zone = "Max Zone"
elif heart_rate >= 100 and heart_rate < 150:
    zone = "Cardio Zone"
elif heart_rate >= 60 and heart_rate < 100:
    zone = "Fat-Burning Zone"
elif heart_rate < 60:
    zone = "Resting Zone"
else:
    zone="dead"
# Testing
print("Your heart rate level is:", zone)