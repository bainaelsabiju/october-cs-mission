numbers = [4, 7, 2, 9, 7, 5]

largest = float("-inf")
second_largest = float("-inf")

for number in numbers:
    if number > largest:
        second_largest = largest
        largest = number
    elif number < largest and number > second_largest:
        second_largest = number

print("Second-largest distinct number:", second_largest)


text = "Hello World"

frequency = {}

for char in text.lower():
    if char != " ":
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

print(frequency)



numbers = [1, 2, 3, 4, 6]
target = 6

left = 0
right = len(numbers) - 1
found = False

while left < right:
    total = numbers[left] + numbers[right]

    if total == target:
        found = True
        break
    elif total < target:
        left += 1
    else:
        right -= 1

print(found)

numbers = [4, 2, 7, 2, 4, 9, 2]
frequency = {}

for number in numbers:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1

print(frequency)