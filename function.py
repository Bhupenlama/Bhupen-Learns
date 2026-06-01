def calculate_area(length, width):
    """Calculate the area of a rectangle."""
    area= length * width
    return area

#callin the function
result = calculate_area(5, 3)
print("The area of the rectangle is:", result)


#types of functions argument
#1. Positional Arguments
#Values are passed based on position.

#Eg-def greet(name, age):
    #print(name, age)
#greet("Bhupen", 20)

#2. Keyword Arguments

#Arguments are passed using parameter names.

#def greet(name, age):
 #   print(name, age)

#greet(age=20, name="Bhupen")

O#rder does not matter here.

#3. Default Arguments

#Parameters have default values.

#ef greet(name, country="Nepal"):
 #   print(name, country)

#greet("Bhupen")

#4. Variable-Length Arguments (*args)

#sed when you don't know how many arguments will be passed.

##   print(args)

#numbers(1, 2, 3, 4)

#5. Keyword Variable-Length Arguments (**kwargs)

#Accepts multiple keyword arguments.

#def details(**kwargs):
 #   print(kwargs)

#details(name="Bhupen", age=20)