balance= 1000
pin= 1234
transaction=[]

#pin validation

for i in range (3):
        pin_verification= int(input("Enter your pin"))
        if pin_verification == pin :
            print("Login Sucessfully !")
            break
        else:
            print("Invalid Pin\nPlease try again ")

else:
    print("Invalid Pin\n Card Blocked")
    exit()


#menu Choice

while True:
    print("1.Check Balance\n2.Deposit Money\n3.Withdraw Money\n4.Show Transaction\n5.Exit")

    Choice= input("Enter your Choice")

    if Choice == "1":
        print("Balance:",balance)
    elif Choice == "2":
        amount= int(input("Enter the amount you wanna Deposit"))
        balance = balance + amount
        transaction.append(f"Deposited Amount: {amount}")
        print("Updated Balance", balance)
    elif Choice == "3":
        amount= int(input("Enter the amount you wanna Withdraw"))
        if amount>0 and  amount<= balance:
            balance = balance - amount
            transaction.append(f"Withdrawn Amount: {amount}")
            print("Remaining Balance", balance)
        else:
            print("Insufficient Balance")
    elif Choice == "4":
        
             if not transaction:
                print("No Transactions yet")
             else:
                for t in transaction:
                    print(t)

    elif Choice =="5":
        print("Thank you for choosing our ATM")
        break

    else:
        print("Invalid Choice\n Please try again")

    
