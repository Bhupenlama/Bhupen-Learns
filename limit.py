# Given N and a limit , count how many multiples of N are there between 1 and limit (inclusive).
n = int(input("N:"))
limit=int(input("Limit:"))
count = 0
for i in range(1, limit+1):
    if i % n == 0:
        count += 1
print("count:",count)