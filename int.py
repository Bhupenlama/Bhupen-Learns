#Take an integer . find the sum of all the digits of that integer.
n = int(input("Enter an integer: "))
total = 0
for digit in n:
    total += int(digit)
    print("Sum of digits:", total)