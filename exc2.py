for _ in range(3):
    usr = input("Enter username: ")
    psw = input("Enter password: ")
    
    if usr == "bank_admin" and psw == "Hytu76E":
        print("Access Granted!")
        break
    else:
        print("Access Denied!")
    print("Try Again!")
else:
    print("No more attemps!")