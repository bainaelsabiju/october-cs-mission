import json
import csv

# JSON
student = {
    "name": "Baina",
    "age": 17,
    "course": "Computer Science"
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

# Read JSON
with open("student.json", "r") as file:
    data = json.load(file)

print("JSON:", data["name"])


# CSV
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["name", "age", "course"])
    writer.writerow(["Baina", 17, "Computer Science"])

print("CSV file created!")



try:
    amount = float(input("Enter an amount: "))
    print("Amount:", amount)

except ValueError:
    print("Please enter a valid number!")


def validate_amount(amount):
    if amount <= 0:
        return False

    return True


try:
    amount = float(input("Enter an amount: "))

    if validate_amount(amount):
        print("Valid amount!")
    else:
        print("Amount must be greater than 0!")

except ValueError:
    print("Please enter a valid number!")

finally:
    print("Input process finished.")


    numbers = [2, 1, 5, 1, 3, 2]
k = 3

window_sum = sum(numbers[:k])
max_sum = window_sum

for i in range(k, len(numbers)):
    window_sum = window_sum - numbers[i - k] + numbers[i]

    if window_sum > max_sum:
        max_sum = window_sum

print("Maximum sum:", max_sum)