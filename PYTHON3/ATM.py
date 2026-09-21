from time import sleep
print("Welcome to python ATM")
sleep(1)
print("Please insert your ATM card  \n please wait")
sleep(1)
pinlist=[1111,9090,8989,1289,3333,5555,8912,6789,4321,5656,2456]
pin=int(input("Please enter your ATM pin"))
Amount,balance = 0.0,0.0
if pin in pinlist:
    while True:
        choose=input ("Select D for Deposit: \n Select W for withdraw: \n select C for check balance: \n select Q for quite from ATM:")
        if choose == "D":
            balance=float(input("please enter your deposit amount Rs."))
            Amount += balance
        elif choose == "W":
            balance=float(input("Please enter withdraw amount Rs."))
            if balance > Amount:
                print("Insufficient Amount")
                exit()
            else:
                Amount -= balance
        elif choose == "C":
            print("Your current balance is Rs.",Amount)
        elif choose == "Q":
            exit()
        else:
            print("Your choice is Invalid \n Try next time")
            exit()
        option=input("Do You want to continue (Y/N)")
        if option == "Y":
            continue
        else:
            break
else:
    print("Pin is invalid \n Try next time")
    exit()
