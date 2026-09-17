# Program to reverse a number

number = int(input("Enter a number: "))

reverse = 0
temp = number

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

print("Original number:", number)
print("Reversed number:", reverse)
