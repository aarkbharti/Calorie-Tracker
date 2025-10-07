print("Welcome to Daily Calorie Tracker!")
print("Log your meals and see if you are within your daily calorie limit")
print("="*50)


num_meals = int(input("How many meals today? "))

total = 0

for i in range(num_meals):
    meal = input("Enter meal name: ")
    cal = float(input("Enter calories for this meal: "))
    total = total + cal
    print(f"{meal}: {cal}")


average = total / num_meals
limit = float(input("\nEnter your daily calorie limit: "))


if total > limit:
    print("\n⚠️  You exceeded your daily limit!")
else:
    print("\n✅ You are within your daily limit!")
print(f"\nTotal calories: {total}")
print(f"Average calories: {average:.2f}")


save = input("\nSave session? yes/no: ")
if save == "yes":
    file = open("calorie_log.txt", "w")
    for i in range(num_meals):
        meal = input(f"Re-enter meal {i+1} name for log: ")
        cal = float(input(f"Re-enter calories for {meal} for log: "))
        file.write(f"{meal}: {cal}\n")
    file.write(f"Total calories: {total}\n")
    file.write(f"Average calories: {average:.2f}\n")
    if total > limit:
        file.write("Exceeded daily limit!\n")
    else:
        file.write("Within daily limit!\n")
    file.close()
    print("Saved to calorie_log.txt")
