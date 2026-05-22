store_balance =int(input("enter the store_balance:"))
witdrawl_amount = int (input ("enter the withdrawal_amount :"))
if(store_balance >= witdrawl_amount):
    withdrawl_amount = store_balance - witdrawl_amount
    print("Remaining balance:", withdrawl_amount)

    print("you can withdraw the amount")
else:
    print("Remaining balance:", store_balance) 

    print ("you cannot withdraw the amount")

    
