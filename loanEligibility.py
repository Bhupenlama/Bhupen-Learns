age =int(input ("Enter your age:"))
income = int(input ("Enter your income:"))
has_id = True
eligible= age >= 18 and income >= 30000 and has_id
if eligible:
    print("You are eligible for the loan.")
else:
    print("You are not eligible for the loan.")

#why rejected
if not has_id:
    print("You are not eligible for the loan because you do not have a valid ID.")
if income < 30000:
    print("You are not eligible for the loan because your income is too low.")
if age < 18:
    print("You are not eligible for the loan because you are under 18 years old.")