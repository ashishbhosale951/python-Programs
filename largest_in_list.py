# Find the largest number in a list

numbers = [12, 45, 7, 89, 34, 67]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Numbers:", numbers)
print("Largest number:", largest)
