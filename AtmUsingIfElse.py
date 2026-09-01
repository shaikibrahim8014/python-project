#Atm Machine Working Model
print("please insert your card")
print("please Select your language")
pins=8484
balance=10000
pin=int(input("please enter your pin number : "))
if pin==pins:
    print("please select your transaction")
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    choice=int(input("please enter your choice : "))
    if choice==1:
        print(f"your balance is : {balance}")
    elif choice==2:
        amount=int(input("please enter the amount you want to withdraw : "))
        if amount<=balance:
            balance=balance-amount
            print(f"your updated balance is : {balance}")
        else:
            print("insufficient balance")
    elif choice==3:
        amount=int(input("please enter the amount you want to deposit : "))
        balance=balance+amount
        print(f"your updated balance is : {balance}")
    else:
        print("invalid choice")
else:
    print("invalid pin number")
print("**** ur transaction is completed successfully ****")