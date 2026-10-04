numbers=[12, 5, 8, 20, 3]
largest=numbers[0]

for number in numbers:
    if number > largest:
        largest=number

print("The largest number is:", largest)

smallest=numbers[0]
for number in numbers:
    if number < smallest:
        smallest=number

print("The smallest number is:", smallest)

for number in numbers:
    total = total + number

print("Total:", total)    