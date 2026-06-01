#return a single value 
def square(n):
    return n ** 2
#return multiple values (tuple unpacking)
def min_max(nums):
    return min(nums), max(nums)

#return ends the function immediately
def check_age(age):
    if age < 18:
        return "Minor"
    else:
        return "Adult"
    #using the returns
    print(square(7))
    lo,hi = min_max([4,1,9,2,7])
    print(f"Min(lo),Max(hi)     ")  
    print (check_age(25))
    