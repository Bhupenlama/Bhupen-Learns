# print a diamond pattern where each row shows the row number repeated Rows go 1-N-1.
n = int(input("Enter the number of rows: "))
#Top half
for i in range(1, n + 1):
    print(""(n-1)+(str(i)+"") * i)
#Bottom half
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + (str(i) + " ") * i)   