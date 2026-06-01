#function that process a list
def find_evens(numbers):
    evens = []
    for number in numbers:
        if number % 2 == 0:
            evens.append(number)
    return evens

#function that builds a multiplication table 
def multiplication_table(n):
    table = []
    for i in range(1, 11):
        table.append(f"{n} x {i} = {n*i}")
    return table