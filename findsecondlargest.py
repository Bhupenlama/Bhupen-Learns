#without using sort()or max()find the second largest elements in a list using loops only
nums = [3, 1, 4, 1, 5, 9, 2, 6, 5]
largest = float('-inf')
second_largest = float('-inf')      
for n in nums:
    if n > largest:
        second_largest = largest
        largest = n
    elif largest > n > second_largest:
        second_largest = n
print("Second largest number:", second_largest)