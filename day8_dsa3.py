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
