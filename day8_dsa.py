numbers = [2, 3, 1, 2, 4, 3]
target = 7

left = 0
window_sum = 0
min_length = len(numbers) + 1

for right in range(len(numbers)):
    window_sum += numbers[right]

    while window_sum >= target:
        current_length = right - left + 1

        if current_length < min_length:
            min_length = current_length

        window_sum -= numbers[left]
        left += 1

if min_length == len(numbers) + 1:
    print("No valid subarray")
else:
    print("Minimum length:", min_length)
