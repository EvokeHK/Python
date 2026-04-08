accNo = 10020100
accCount = 0

# # Bank app using dictionary
# # Main menu
# # 1.account create
# # 2.transaction
# # 3.all accounts 
# # 4.exit
# # Note. Account no should be automaticaly increment which must use as global variable start with 10020100
# # 1.create account
# # Read username and amount to open an account
# # Check the amount is multiple of 100 and must be greater than 1000 then save to dictionary using account no as key
# 2.transaction
# Read account no of exist then
# Show another menu
# 1.deposit
# Amount must be multiple of 100
# 2.withdraw
# Amount must be multiple of 100 and minimum 1000 must be kept
# 3.show
# 4.exit

# Else
# Show account number is not exist
# 3.show all account
# Show all entry in account dictionary


def main():
    i = int(
        input(
            """MAIN MENU \n
                  1. Create Account\n
                  2. Transaction\n
                  3. All Accounts\n
                  4. Exit\n"""
            )
    )
    match i:
        case 1:
            accCount += 1
            createaccount()
            accNo = accNo + 1
        case 2:
            Transaction()
        case 3:
            account()
        case 4:
            exit()

def createaccount():
    username = input("Enter the username ")
    amount = input("Enter the initial Amount ")
    while (amount % 100 != 0 and amount > 1000):
        amount = ("The initial amount should be multiple of 100 and more than 1000\n Enter the amount again")
    

def Transaction():
    i = int(input(""))

def account():

def exit():

if __name__ == "__main__":
    main()
