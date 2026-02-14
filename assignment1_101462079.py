"""
Author: Muhammet Yusuf OZCAN
Assignment: #1
"""

# Step b: Create 4 variables
#String
gym_member = "Alex Alliton"
#Float
preferred_weight_kg = 20.5
#Integer
highest_reps = 25
#Boolean
membership_active = True

# Step c: Create a dictionary named workout_stats
workout_stats = {
    "Alex" : (30,60,55),
    "Jamie": (45,10,50),
    "Taylor": (20,62,31)
}

# Step d: Calculate total workout minutes using a loop and add to dictionary
for names in list(workout_stats.keys()):
    times = workout_stats[names]
    total_times = sum(times)
    key = f"{names}_Total"
    workout_stats[key] = total_times

# Step e: Create a 2D nested list called workout_list
workout_list = [
    list(workout_stats["Alex"]),
    list(workout_stats["Jamie"]),
    list(workout_stats["Taylor"])
]

# Step f: Slice the workout_list
print(f"Yoga Results for Every Person")
for result in workout_list[-3:]:
    print(f"{result[0]}")

print("Weightlifting Results for Every Person")
for result in workout_list[-2:]:
    print(f"{result[1]}")

print("running Results for Every Person")

for result in workout_list[-3:]:

    print(result[2])

# Step g: Check if any friend's total >= 120
for members,times in workout_stats.items() :
    if "_Total" in members:
        if workout_stats[members] >= 120:
            print(f"Great Job staying active {members}, your total workout time is 120 or above ")


# Step h: User input to look up a friend
member_name = input("Please Enter Member Name: \n")
member = False
for members in workout_stats:
    stats = workout_stats[members]
    if members == member_name:
        member = True
        message = (f"Yoga: {stats[0]},\n"
                   f"Weightlifting: {stats[1]},\n"
                   f"Running: {stats[2]},\n"
                   f"Your Total Workout Minutes: {sum(stats)}")

        print(f"\nHey {members}!\nYour Workout Minutes by each activity:\n\n{message}\n\n")
        break

if not member:
    print(f"Friend `{member_name}` not found in the records.")
#Step i: Friend with highest and lowest total workout minutes
for key, value in workout_stats.items():
    if "_Total" in key:
        name = key.replace("_Total","")
        print(f"{name}: {value}")


namelist = []
for key, value in workout_stats.items():
    if "_Total" in key:
        name = key.replace("_Total","")
        namelist.append([value, name])
low = min(namelist)
high = max(namelist)
print(f"Lowest Minutes: {low}")
print(f"Highest Minutes: {high}")


