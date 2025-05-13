import os
from datetime import datetime

CUSTOMER_ID = "last_id.txt"
ADMIN_ID = "admin_id.txt"
ADMIN_DETAILS = "admin_details.txt"
CUSTOMER_DETAILS = "create_customer.txt"
ACCOUNT_NUM = "account_num.txt"
ACCOUNTS = "account.txt"
TRANSACTION_HISTORY = "transaction_history.txt"

def account_number():
    if not os.path.exists(ACCOUNT_NUM):
        with open(ACCOUNT_NUM, "a") as num_file:
            num_file.write("AC0001\n")
            return 'AC0001'
    else:
        with open(ACCOUNT_NUM, "r") as num_file:
            num = num_file.readlines()
            last_acc_num = num[-1].strip().split(",")[0]
            next_acc_num = (f"AC{int(last_acc_num[2:]) + 1:04}")
    
        with open(ACCOUNT_NUM, "a") as num_file:
            num_file.write(f"{next_acc_num}\n")
            return (next_acc_num)

def next_customer_id():
    if not os.path.exists(CUSTOMER_ID):
        with open(CUSTOMER_ID, "a") as cus_file:
            cus_file.write("C001\n")
        return 'C001'
    else:
        with open(CUSTOMER_ID, 'r') as cus_file:
            customer_id = cus_file.readlines()
            last_customer_id = customer_id[-1].split(',')[0]
            next_customer_id = (f"C{int(last_customer_id[1:]) + 1:03}")

        with open(CUSTOMER_ID, 'a') as cus_file:
            cus_file.write(f"{next_customer_id}\n")
            return (next_customer_id)

def next_admin_id():
    if not os.path.exists(ADMIN_ID):
        with open(ADMIN_ID, "a") as admin_file:
            admin_file.write("U001\n")
            return 'U001'
    else:

        with open(ADMIN_ID, "r") as admin_file:
            admin_id = admin_file.readlines()
            last_admin_id = admin_id[-1].split(',')[0]
            next_admin_id = (f"U{int(last_admin_id[1:]) + 1:03}")
            
        with open(ADMIN_ID, "a") as admin_file:
            admin_file.write(f"{next_admin_id}\n")
            return next_admin_id

def transaction_history():
    if not os.path.exists(TRANSACTION_HISTORY):
        with open(TRANSACTION_HISTORY, "a") as transaction_file:
            transaction_file.write(f"{account_number},{transaction_type},{amount},{balance}\n")
    else:
        with open(TRANSACTION_HISTORY, "a") as transaction_file:
            transaction_file.write(f"{account_number},{transaction_type},{amount},{balance}\n")
    print(f"{account_number},{transaction_type},{amount},{balance},{timestamp}")

# -------------setting up the first time system login----------------------------------------------
def admin_setup():
    if not os.path.exists(ADMIN_DETAILS):
        print("Command! Control! Customize!Your Admin Setup.")
        admin_name = input("Enter the admin name:")
        admin_password = input("Enter the password:").strip()
        # creatig a id for adminprint(next_admin_id())
        new_admin_id = next_admin_id()

    try:
        if not os.path.exists(ADMIN_DETAILS):
            with open(ADMIN_DETAILS, "a") as admin_file:
                admin_file.write(f"{new_admin_id},{admin_name},{admin_password}\n")
                print(f"Admin created successfully! Admin id is:{new_admin_id}")
        else:
            print("Admin already exists")
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
            choice = int(input("Enter the number of your choice:"))

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
    print("1.Admin\n2.Customer\n3.Exit")

    choice = int(input("Enter the number of your role:"))
    try:
        if choice == 1:

            correct_admin_id = input("Enter the admin id: ")
            correct_password = input("Enter your password: ")

            login_successful = False

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
    try:
        initial_balance = float(input("Enter the initial balance:").strip())
        if initial_balance < 0 :
            print("Initial balance should be non-negative.")
            return
    except ValueError:
        print("Invalid input.Please enter a valid number.")
        
    try:
        with open(ACCOUNTS, "a") as acc_file:
            acc_file.write(f"{account_num},{customer_name},{password},{initial_balance}\n")
            print(f"welcome {customer_name}! Thank you for choosing our bank.\n""We are happy to serve you!")
            print(f"YOUR USER ID : {customer_user_id}")
            print(f"Your account number is:{account_num}")
    except FileNotFoundError:
        print("File not found")

        # with open(TRANSACTION_HISTORY,"w")


# -------------------adding a new admin---------------------------------------------------
def add_admin():
    admin_name = input("Enter the admin name:")
    admin_password = input("Enter the password:")
    new_admin_id = next_admin_id()
    try:
        with open("admin_details.txt", "a") as details_file:
            details_file.write(f"{new_admin_id},{admin_name},{admin_password}\n")
            print(f"Admin created successfully! Admin id is:{new_admin_id}")
    except FileNotFoundError:
        print("File not found")

# ----------------ADMIN MENU-----------------------------------------------------------------
def admin_menu():
    while True:
        print("ADMIN MENU")
        print("1.Create Account\n2.Add admin\n3.Exit")
        try:
            choice = int(input("Enter your choice:"))

            if choice == 1:
                print("====Creating a customer...====")
                create_account()
            elif choice == 2:
                print("====Adding a new admin====")
                add_admin()
            elif choice == 3:
                print("Exit!")
                break
            elif choice < 1 or choice > 3:
                print("Your choice must be 1-3.")
        except ValueError:
            print("Invalid Input!Try again!")


# ----------------MAIN MENU-----------------------------------------------------------------
def main_menu():
    while True:
        print("======MENU======\n1.Deposit Money\n2.Withdraw Money\n3.Check Balance\n4.Transaction History\n5.Exit")

        try:
            user_choice = int(input("Choose the number from the menu(1-6):"))
            if user_choice == 1:
                print("=====Deposit Money=====")
                deposit()
            elif user_choice == 2:
                print("=====withdraw money====")
                withdrawal()
            elif user_choice == 3:
                print("=====check_balance=====")
                check_balance()
            elif user_choice == 4:
                print("=====transaction history=====")
                transaction_history()
            elif user_choice == 5:
                print("Exit!")
                exit()
            elif user_choice < 1 or user_choice > 5:
                print("Invalid number.Choose betweewn 1-6 only!")
        except ValueError:
            print("Invalid Input.Try again!")

# -------------------DEPOSIT MONEY---------------------------------------------------
def deposit():
    isYes = True
    Account_number = input("Enter your account number:")

    with open(ACCOUNTS, "r") as acc_file:
        lines = acc_file.readlines()

    update_lines = [] #this is a list to store the updated balance

    with open(ACCOUNTS, "w") as acc_file:
        i = 0
        isIndex = True
        for line in lines:
            acc_details = line.strip().split(',')
            if acc_details[0] == Account_number:
                while True:
                    if isYes == True:
                        try:
                            deposit_amount = float(input("Enter the deposit amount:"))

                            if deposit_amount > 0:
                                balance = float(acc_details[3]) + deposit_amount
                                print(f"You have deposited successfully!\nYour current balance is {balance}.")    

                                if isIndex == True:                          
                                    update_lines.append(f"{acc_details[0]},{acc_details[1]},{acc_details[2]},{balance}\n")
                                else:
                                    update_lines[i] = f"{acc_details[0]},{acc_details[1]},{acc_details[2]},{balance}\n"                                                                                        

                                while isYes:
                                    depositeagain = input("Are you going to do another deposit?\nyes or no:")
                                    if depositeagain.lower() == "yes":
                                        isIndex = False
                                        break
                                    elif depositeagain.lower() == "no":
                                        print(f"Your deposit was successful.\nYour current balance is {balance}.\nThank You!")
                                        # saving the transaction history
                                        
                                        with open(TRANSACTION_HISTORY, "a") as transaction_file:
                                            transaction_type = "deposit"
                                            amount = deposit_amount
                                            transaction_file.write(f"{Account_number},{transaction_type},{amount},{balance}\n")
                                            # transaction_file.write(f"{Account_number},{transaction_type},{amount},{balance},{timestamp}\n")
                                            isYes = False
                                        
                                    else:
                                        print("Your input is invalid.Please input yes or no.")
                                        continue

                            elif deposit_amount == 0:
                                print("Your Deposit amount should be greater than 0.")
                            else:
                                print("Your deposit amount should be a positive.")

                        except ValueError:
                            print("Please enter the valid amount.")
                    else:                    
                        print("TESTING 02")
                        break
                print('TESTING 03')
                # update_lines.append(f"{acc_details[0]},{acc_details[1]},{acc_details[2]},{balance}")   
            else:
                update_lines.append(f"{line}")
            i = i + 1
        acc_file.writelines(update_lines)

    print(update_lines)

    #     # Add the (updated or unchanged) account details to the list
    #     updated_lines.append(','.join(acc_details))
    #     print('TESTING 01: ', updated_lines)
    # # Update the accounts file with the new balance
    # # with open(ACCOUNTS, "w") as acc_file:
    #     acc_file.write("\n".join(updated_lines))
    #     print("\n".join(updated_lines)) 
    main_menu()
# -------------------WITHDRAW MONEY---------------------------------------------------
def withdrawal():
    account_number = input("Enter your account number:")
    password = input("Enter your password:")

    with open(ACCOUNTS, "r") as acc_file:
        lines = acc_file.readlines()

        updated_lines = []
    with open(ACCOUNTS, "r") as acc_file:
        lines = acc_file.readlines()
        for line in lines:
            acc_details = line.strip().split(',')
            if acc_details[0] == account_number and acc_details[2] == password:
                balance = float(acc_details[3])
                
                while True:
                    try:
                        withdrawal_amount = float(input("Enter the withdrawal amount :"))

                        if withdrawal_amount > balance:
                            print(
                                f"Your withdrawal amount is greater than your account balance.\nYour account balance is {balance}.Try again!")

                        elif withdrawal_amount == balance:
                            print(
                                "Sorry!Your withdrawal amount is equals to your account balance.\nYou must maintain a minimum balance of rs.1000 in your account.Try again!")

                        elif withdrawal_amount < balance:
                            balance = balance - withdrawal_amount
                            if balance >= 1000.00:
                                print(f"Your withdrawal was successful!\nYour account balance is rs.{balance}")
                                
                                with open(TRANSACTION_HISTORY, "a") as transaction_file:
                                    transaction_type = "withdraw"
                                    amount = withdrawal_amount
                                    transaction_file.write(f"{account_number},{transaction_type},{amount},{balance}\n")
                                
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
            else:
                print("Invalid account number or password.")
               # Add the (updated or unchanged) account details to the list
                updated_lines.append(','.join(acc_details))

    with open(ACCOUNTS, "w") as acc_file:
        acc_file.write("\n".join(updated_lines))
                            
# -------------------CHECK BALANCE-------------------------------------------------------------------
def check_balance():
    account_number = input("Enter your account number:").strip()
    password = input("Enter your password:")

    with open(ACCOUNTS, "r") as acc_file:
        for line in acc_file:
            acc_details = line.strip().split(',')
            if acc_details[0] == account_number and acc_details[2] == password:
                print(f"Your current balance is {acc_details[3]}.")
                break

                # with open(TRANSACTION_HISTORY, "r") as transaction_file:
                #     for line in transaction_file:
                #         transaction_details = line.strip().split(',')

                #         print(f"Your current balance is {transaction_details[3]}.")
        else:
            print("Invalid account number or password.\n")
            

# -------------------UPDATE ACCOUNT BALANCE-------------------------------------------
# def update_account_balance(account_number, new_balance):
#     with open(ACCOUNTS, "r") as acc_file:
#         accounts = [line.strip() for line in acc_file]

#     with open(ACCOUNTS, "w") as acc_file:
#         for account in accounts:
#             acc_details = account.split(',')
#             if acc_details[0] == account_number:
#                 acc_details[3] = str(new_balance)
#             acc_file.write(','.join(acc_details) + "\n")

# -------------------TRANSACTION HISTORY----------------------------------------------
def transaction_history():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    account_number = input("Enter your account number:").strip()

    
    if not os.path.exists(TRANSACTION_HISTORY):
        with open(TRANSACTION_HISTORY, "a") as transaction_file:
            transaction_file.write(f"{account_number},{transaction_type},{amount},{balance}\n")
            
    with open(TRANSACTION_HISTORY, "r") as transaction_file:
        print("Your Transaction History:")
        for line in transaction_file:
            details = line.strip().split(',')
            if details[0] == account_number:
                print(f"{details[0]},{details[1]},{details[2]},{details[3]}")

admin_setup()

# 



