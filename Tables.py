""" Table using loop concept """
num=int(input("Enter a Number :  "))
for i in range(1,11):
    print(f"{num} x {i} ={num*i}")
print("\nTable is printed successfully")




""" using while loop concept """




while True:
    choice=input("Do you want to print another table (y/n) :  ").lower()
    if choice=='y':
        num=int(input("Enter a Number :  "))
        for i in range(1,11):
            print(f"{num} x {i} ={num*i}")
        print("\nTable is printed successfully")
    elif choice=='n':
        print("Thank you for using the program")
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")