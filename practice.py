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