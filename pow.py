#Compute base*exp using only multiplications in a fo a loop.No**or pow()
base = int(input("Enter the base: "))
exp = int(input("Enter the exponent: "))
result = 1
for i in range(exp):
    result = result *base 
    print(result)