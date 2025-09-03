print("-------------ATM machine---------")
print("            1.Deposit")
print("            2.withdraw")
print("            3.Check balance")
print("            4.Exit")

pin=3000
balance=0
trials=0
while True:
  choice=int(input("Enter option:"))
  match(choice):
    case 1:
         amount=input("Enter amount to deposit:")
         balance+=int(amount) if int(amount) > 0 else print(f"Please deposit.")
         print(f"Your new balance is ${balance}. Thank you \n")
    case 2:
         amount=int(input("Enter amount to withdraw:"))
         if amount <balance and pin==int(input("Enter your pin to cofirm:")) :
            balance-=amount
            print(f"You have withdrawn {amount}.Your Account balance is {balance} \n")
         elif amount >= balance :
            print("Transaction failed due to Insufficient balance to complete transaction \n")  
         else :
            print("Access denied : invalid pin.You have 2 more wrong attempts  and your account will be blocked \n")
            trials+=1
            if trials ==3:
                print("Your account has beeen blocked")
                break

    case 3:
         print(f"Your current balance is {balance}")

    case 4:
        break
