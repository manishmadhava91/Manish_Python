a=1
while a<=5:
    b = int(input("Enter a Password: "))
    if b == 567:
        print(b,"password is correct")
    elif a>=5:
        print("5 times above try so please wait 30 seconds")
    else:
    print(b,"password is incorrect retry password")
    a=a+1
    