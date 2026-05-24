# print an  inverted full pyramid. Stars decrease each row,centered with spaces.

rows = int(input("Enter the number of rows: "))
for i in range(rows, 0, -1):
    stars = 2 * i - 1
    spaces =rows - i
    print(" " * spaces + "*" * stars)
    