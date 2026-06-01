#lambda expression is a small anonymous function that can take any number of arguments, but can only have one expression. The syntax for a lambda function is:
#lambda vs def - same thing but different syntax
def square(x): return x * x
square_lambda = lambda x: x * x
print(square(5)) # Output: 25
print(square_lambda(5)) # Output: 25

#lambda with sorted function
students = [('Alice', 25), ('Bob', 20), ('Charlie', 30)]
# Sort by age using a lambda function as the key
students_sorted = sorted(students, key=lambda student: student[1])
print(students_sorted) # Output: [('Bob', 20), ('Alice', 25), ('Charlie', 30)]      
print(students) # Output: [('Alice', 25), ('Bob', 20), ('Charlie', 30)] 
print(students_sorted) # Output: [('Bob', 20), ('Alice', 25), ('Charlie', 30)]


#part 2
#lambda with map() and filter()
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(doubled) # Output: [2, 4, 6, 8, 10]
print(evens) # Output: [2, 4]   

#lambda in ml- custom lost weight 
loss_weight = lambda epoch: 0.1 * epoch
print(loss_weight(5)) # Output: 0.5 