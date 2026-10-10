
# Problem 1: Find the second-largest distinct number

numbers = [10, 5, 8, 10, 7]

largest = None
second_largest = None

for number in numbers:
    if largest is None or number > largest:
        second_largest = largest
        largest = number
    elif number != largest and (
        second_largest is None or number > second_largest
    ):
        second_largest = number

print("Second-largest number:", second_largest)





# Problem 2: Count character frequency

text = "Hello World"

text = text.lower()
frequency = {}

for character in text:
    if character == " ":
        continue

    if character in frequency:
        frequency[character] += 1
    else:
        frequency[character] = 1

print("Character frequencies:")

for character, count in frequency.items():
    print(character, ":", count)



# Problem 3: Longest substring without repeating characters

text = "abcabcbb"

left = 0
seen = set()
max_length = 0

for right in range(len(text)):
    while text[right] in seen:
        seen.remove(text[left])
        left += 1

    seen.add(text[right])

    current_length = right - left + 1

    if current_length > max_length:
        max_length = current_length

print("Longest length:", max_length)
