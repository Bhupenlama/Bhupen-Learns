#simulate ATM login.Give 3 attempt .lock the account after 3 failed attempts.
correct_pin = "1234"
attempts = 3
while attempts > 0:
    pin = input("Enter your PIN: ")
    if pin == correct_pin:
        print("Access granted.")
        break
    else:
        attempts -= 1
        print("Incorrect PIN. Attempts left:", attempts)
else:
    print("Account locked.")    
    if success:
        print("Access granted.")
    else:
        print("Account locked.")    