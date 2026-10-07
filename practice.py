print("\n--- Dictionary Practice ---")

expense = {
    "amount": 500,
    "category": "Food",
    "date": "2026-10-06"
}

expense["amount"] = 750
expense["payment"] = "UPI"

print(expense)

print(expense.keys())
print(expense.values())
print(expense.items())

categories = {"Food", "Clothes", "Food", "Books", "Clothes"}



categories.add("Transport")
print(categories)

categories1 = {"Food", "Books", "Clothes"}
categories2 = {"Food", "Books", "Transport"}

print("Union:", categories1 | categories2)
print("Intersection:", categories1 & categories2)
print("Difference:", categories1 - categories2)

numbers = [1, 2, 3, 4, 5]

squares = {number: number * number for number in numbers}

print(squares)


numbers = [1, 2, 3, 4, 5]

even_numbers = [number for number in numbers if number % 2 == 0]

print(even_numbers)


numbers = [1, 2, 2, 3, 3, 3, 4, 4]

frequency = {}

for number in numbers:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1

print(frequency)


numbers = [4, 2, 4, 3, 2, 4, 1, 3, 4]

most_frequent = None
max_count = 0

for number in frequency:
    if frequency[number] > max_count:
        most_frequent = number
        max_count = frequency[number]

print("Most frequent:", most_frequent)



for number in numbers:
    if frequency[number] == 1:
        print("First non-repeating:", number)
        break



def greet(name):
    print("Hello", name)

greet("Baina")


def introduce(name, age):
    print("My name is", name)
    print("I am", age, "years old")

introduce("Baina", 17)


def greet(name, country="India"):
    print("Hello", name)
    print("You are from", country)

greet("Baina")


def introduce(name, age):
    print("My name is", name)
    print("I am", age, "years old")

introduce(age=17, name="Baina")



def add_expenses(*amounts):
    total = 0

    for amount in amounts:
        total += amount

    print("Total:", total)

add_expenses(100, 200, 300, 50)


def show_expense(**details):
    print("Category:", details["category"])
    print("Amount:", details["amount"])

show_expense(category="Food", amount=500)


numbers = [2, 1, 5, 1, 3, 2]
k = 3

window_sum = sum(numbers[:k])
max_sum = window_sum

for i in range(k, len(numbers)):
    window_sum = window_sum - numbers[i - k] + numbers[i]

    if window_sum > max_sum:
        max_sum = window_sum

print("Maximum sum:", max_sum)