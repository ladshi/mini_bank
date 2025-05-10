import os
def account_number():
    if not os.path.exists("account_num.txt"):
        return 'AC0001'
    else:
        with open("account_num.txt", "r") as num_file:
            num = num_file.readlines()
            if not num:
                next_acc_num = 'AC0001'
            else:
                last_acc_num = num[-1].strip().split(",")[0]
                next_acc_num = (f"AC{int(last_acc_num[2:]) + 1:04}")
        # Append mode to add the new account number without overwriting
        with open("account_num.txt", "a") as num_file:
            num_file.write(f"{next_acc_num}\n")
            print(next_acc_num)

def next_customer_id():
    if not os.path.exists("last_id.txt"):
        return 'C001'
    else:
        with open('last_id.txt', 'r') as cus_file:
            customer_id = cus_file.readlines()   
            if not customer_id:
                next_customer_id = 'C001'
            else:
                last_customer_id = customer_id[-1].split(',')[0]
                next_customer_id = (f"C{int(last_customer_id[1:]) + 1:03}")
        with open('last_id.txt', 'a') as cus_file:
            cus_file.write(f"{next_customer_id}\n")
            return next_customer_id
        
def next_admin_id():
    if not os.path.exists("admin_id.txt"):
        return 'U001'
    else:
        with open("admin_id.txt","r") as admin_file:
            admin_id = admin_file.readlines()
            if not admin_id:
                next_admin_id = 'U001'
            else:
                last_admin_id = admin_id[-1].split(',')[0]
                next_admin_id = (f"U{int(last_admin_id[1:]) + 1:04}")
        with open("admin_id.txt","a") as admin_file:
            admin_file.write(f"{next_admin_id}\n")
            return next_admin_id

CUSTOMER_ID = "last_id.txt"
ADMIN_ID = "admin_id.txt"
ADMIN_DETAILS = "admin_details.txt"
CUSTOMER_DETAILS = "create_customer.txt"
ACCOUNT_NUM = "account_num.txt"
ACCOUNTS = "account.txt"
TRANSACTION_HISTORY = "transaction_history.txt"

# -------------setting up the first time system login----------------------------------------------
def admin_setup():
    print("Command. Control. Customize.Your Admin Setup.")
    admin_name = input("Enter the admin name:")
    admin_password = input("Enter the password:").strip()
    # creatig a id for admin
    new_admin_id = next_admin_id()

    try:
        with open(ADMIN_DETAILS,"a") as admin_file:
            admin_file.write(f"{next_admin_id()},{admin_name},{admin_password}\n")
            print(f"Admin created successfully! Admin id is:{next_admin_id()}")
    except FileNotFoundError:
        print("file not found")
        exit()
    start()

# -------------starting the banking system----------------------------------------------
def start():
    
    for i in range(3):
        print("WELCOME TO THE BANKING SYSTEM!")
        print("*******************************")
        print("1.Login\n2.Exit")

        try:
            choice =int(input("Enter the number of your choice:"))

            if choice == 1:
                print("=====Login=====")
                Login()
            elif choice == 2:
                print("Thank you for using the banking system!")
                exit()
            else:
                print("Invalid choice.Please try again.")
        except ValueError:
            print("Invalid input.Please enter a valid number.")

# -------------login to the system-----------------------------------------------------------
def Login():
    global admin_password
    Next_admin = next_admin_id()
    print("1.Admin\n2.Customer\n3.Exit")

    choice = int(input("Enter the number of your role:"))
    try:
        if choice == 1:
            
            correct_admin_id= input("Enter the admin id: ")
            correct_password = input("Enter your password: ")

            login_successful= False

            with open(ADMIN_DETAILS, 'r') as admin_file:
                for admin in admin_file:
                    admin_details = admin.strip().split(',')
            
                if admin_details[0] == correct_admin_id and admin_details[2] == correct_password:
                    login_successful = True
                    
                if login_successful == True:
                    print("Login successful!")
                    admin_menu()
                else:
                    print("Login failed! Try again.")
        elif choice == 2:
            main_menu()
        elif choice == 3:
            exit()
        elif choice < 0 or choice > 0:
            print("You can only choose between 1-3.Try again!")
    except ValueError:
        print("Invalid input.Try again!")
# -------------------creating a new customer account---------------------------------------------------
def create_account():
 
    print("Creating a new customer")
    account_num = account_number()
    customer_user_id = next_customer_id() 
    customer_name = input("Enter your Name:")
    NIC_No = input("Enter your NIC_NO:")
    address = input("Enter your address:")
    phone_num = input("Enter your mobile number:")
    password = input("Enter the password:")
    initial_balance = float(input("Enter the initial balance:").strip())

    with open(CUSTOMER_DETAILS, "a") as create_file:
        create_file.write(f"{customer_user_id},{customer_name},{NIC_No},{address},{phone_num},{password}\n")

    print(f"welcome {customer_name}! Thank you for choosing our bank.\n""We are happy to serve you!")
    print(f"YOUR USER ID : {customer_user_id}")

    with open(ACCOUNTS,"a") as acc_file:
        acc_file.write(f"{account_num},{customer_name},{password},{initial_balance}\n")

    print(f"Your account number is:{account_num}")
# -------------------adding a new admin---------------------------------------------------
def add_admin():
    admin_name = input("Enter the admin name:")
    admin_password = input("Enter the password:")

    try:
        with open("admin_details.txt","a") as details_file:
            details_file.write(f"{next_admin_id()},{admin_name},{admin_password}\n")
            print(f"Admin created successfully! Admin id is:{next_admin_id()}")
    except FileNotFoundError:
        print("File not found")
#----------------ADMIN MENU-----------------------------------------------------------------
def admin_menu():

    while True:
        print("ADMIN MENU")
        print("1.Create Account\n2.Add admin\n3.Exit")
        try:
            choice =int(input("Enter your choice:"))

            if choice == 1:
                print("Creating a customer...")
                create_account()
            elif choice == 2:
                print("Create account")
                add_admin()
            elif choice == 3:
                print("Exit!") 
                break
            elif choice < 1 or choice >3:
                print("Your choice must be 1-3.")
        except ValueError:
            print("Invalid Input!Try again!")
#----------------MAIN MENU-----------------------------------------------------------------
def main_menu():
    while True:
        print("======MENU======\n1.Deposit Money\n2.Withdraw Money\n3.Check Balance\n4.Transaction History\n5.Exit")

        try:
            user_choice=int(input("Choose the number from the menu(1-6):"))
            if user_choice == 1:
                print("=====Deposit Money=====")
                deposit()
                continue
            elif user_choice == 2:
                print("=====withdraw money====")
                withdrawal()
                continue
            elif user_choice == 3:
                print("=====check_balance=====")
                check_balance()
                continue
            elif user_choice == 4:
                transaction_history()
                continue
                print("=====transaction history=====")
            elif user_choice == 5:
                print("Exit!")
                break
            elif user_choice < 1 or user_choice > 5:
                print("Invalid number.Choose betweewn 1-6 only!")
        except ValueError:
            print("Invalid Input.Try again!")
# -------------------DEPOSIT MONEY---------------------------------------------------
def deposit():

    Account_number = input("Enter your account number:")

    with open(ACCOUNTS,"r") as acc_file:
        lines = acc_file.readlines()

    with open(ACCOUNTS,"a") as acc_file:
        for line in lines:
            acc_details = line.strip().split(',')
            if acc_details[0] == Account_number:
                while True:
                
                    try:
                        deposit_amount=float(input("Enter the deposit amount:"))
                    
                        if deposit_amount > 0:
                            balance=float(acc_details[3])+deposit_amount
                            print(f"You have deposited successfully!\nYour current balance is {balance}.")

                            while True:
                                depositeagain=input("Are you going to do another deposit?\nyes or no:")
                                if depositeagain.lower() == "yes" :
                                    break
                                elif depositeagain.lower() == "no":
                                    print(f"Your deposit was successful.\nYour current balance is {balance}.\nThank You!")
                                    exit()
                                
                                else:
                                    print("Your input is invalid.Please input yes or no.")
                                    continue

                        elif deposit_amount == 0:
                            print("Your Deposit amount should be greater than 0.")
                        else:
                            print("Your deposit amount should be a positive.")
                    except ValueError:
                            print("Please enter the valid amount.")

                acc_details[3] = str(float(acc_details[3]) + deposit_amount)
                acc_file.write(','.join(acc_details) + "\n")

    with open(TRANSACTION_HISTORY,"a") as transaction_file:
        transaction_file.write(f"{account_number},deposit:{deposit_amount},{balance}\n")
                
# -------------------WITHDRAW MONEY---------------------------------------------------
def withdrawal():
    account_number = input("Enter your account number:")
    password = input("Enter your password:")

    with open(ACCOUNTS,"r") as acc_file:
        for line in acc_file:
            acc_details = line.strip().split(',')
            if acc_details[0] == account_number and acc_details[2] == password:
                balance = float(acc_details[3])
                break
    while True:
        try:
            withdrawal_amount = float(input("Enter the withdrawal amount :"))

            if withdrawal_amount > balance:
                print(f"Your withdrawal amount is greater than your account balance.\nYour account balance is {balance}.Try again!")
                
            elif withdrawal_amount == balance:
                print("Sorry!Your withdrawal amount is equals to your account balance.\nYou must maintain a minimum balance of rs.1000 in your account.Try again!")
                
            elif withdrawal_amount < balance :
                balance = balance - withdrawal_amount
                if balance >= 1000.00:
                    print(f"Your withdrawal was successful!\nYour account balance is rs.{balance}")
                    while True:
                        userinput = input("Are you going to do another withdrawal?\nyes or no:")
                        if userinput.lower() == "yes":
                            break
                        elif userinput.lower() == "no":
                            print("Thank you for using our service!")
                            return
                        
                elif balance <= balance:
                    print("Sorry!You must maintain a minimum balance of rs.1000 in your account.Try again!")
                    continue
        except ValueError:
            print("Invalid input!Try again!")

    with open(TRANSACTION_HISTORY,"a") as transaction_file:
        transaction_file.write(f"{account_number},withdraw:{withdrawal_amount},{balance}\n")
# -------------------TRANSACTION HISTORY---------------------------------------------------------------
def transaction_history():
    global deposit_amount
    global withdrawal_amount
    with open(TRANSACTION_HISTORY,"a") as transaction_file:
        transaction_file.write(f"{account_number},{withdrawal_amount or deposit_amount},{balance}\n")
# -------------------CHECK BALANCE-------------------------------------------------------------------
def check_balance():
    account_number = input("Enter your account number:").strip()
    password = input("Enter your password:")
    
    with open(ACCOUNTS,"r") as acc_file:
        for line in acc_file:
            acc_details = line.strip().split(',')
            if acc_details[0] == account_number and acc_details[2] == password:
                
                with open(TRANSACTION_HISTORY,"r") as transaction_file:
                    for line in transaction_file:
                        transaction_details = line.strip().split(',')
                        
                    print(f"Your current balance is {transaction_details[2]}.")
            else:
                print("Invalid account number or password.")

# -------------------TRANSACTION HISTORY---------------------------------------------------
def transaction_history():

    account_number = input("Enter your account number:")
    password = input("Enter your password:")

    with open(ACCOUNTS,"r") as acc_file:
        for line in acc_file:
            acc_details = line.strip().split(',')
            if acc_details[0] == account_number and acc_details[2] == password:
                with open(TRANSACTION_HISTORY,"r") as transaction_file:
                    for line in transaction_file:
                        transaction_details = line.strip().split(',')
                    print(f"Transaction details: {transaction_details[0]},{transaction_details[1]},{transaction_details[2]}")
            else:
                print("Invalid account number or password.")
    
admin_setup()
    

        

            
            