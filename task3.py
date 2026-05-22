total_bill = 3750.00
num_people = 5
paid_extra = True
discount_percent = 10
Your_name = "Bhupen"

discount =  (total_bill * discount_percent)/100)
eachpersonshare = (total_bill - discount) / num_people
typeofeachvariable = type(eachpersonshare)
print(f"Total bill: {total_bill}\nNumber of people: {num_people}\nPaid extra: {paid_extra}\nDiscount percent: {discount_percent}\nYour name: