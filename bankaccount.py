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

accDict = {}
accNo = 10020100


def main():
    global accNo, accDict
    i = int(
        input(
            """MAIN MENU \n
                  1. Create Account
                  2. Transaction
                  3. Check Account Balance
                  4. All Accounts
                  5. Exit\n"""
        )
    )
    match i:
        case 1:
            createaccount()
        case 2:
            Transaction()
        case 3:
            balance()
        case 4:
            accounts()
        case 5:
            exit()


def createaccount():
    global accNo
    global accDict
    username = input("Enter the User Name ")
    amount = int(input("Enter the initial Amount "))
    while (amount % 100 != 0) or (amount < 1000):
        amount = int(
            input(
                "The initial amount should be multiple of 100 and more than 1000\n Enter the amount again \n"
            )
        )
    accDict.update({accNo: {"Username": username, "Amount": amount}})
    print("Account ", accNo, " Created")
    accNo += 1
    y = input("Do you want to go back to Main Menu (y/n)")
    match y:
        case "y":
            main()
        case "n":
            exit()


def Transaction():
    global accDict, accNo
    acc = int(input("Enter the account Number \n"))
    if acc in accDict.keys():
        x = int(
            input(
                """MENU \n
                      1. Withdraw\n
                      2. Deposit \n"""
            )
        )
        match x:
            case 1:
                z = int(input("Enter the amount to be withdrawn "))
                if ((accDict[acc]["Amount"] - z) > 1000) and (z % 100 == 0):
                    accDict[acc]["Amount"] -= z
                    print("Amount Successfully Withdrawn \n")
                    y = input("Do you want to go back to Main Menu (y/n)")
                    match y:
                        case "y":
                            main()
                        case "n":
                            exit()
                else:
                    print(
                        "Withdrawal amount should be multiple of 100 and final balance should be more than 1000 .....\nreturning to Main Menu"
                    )
                    main()
            case 2:
                z = int(input("Enter the amount to be deposited "))
                if z % 100 == 0:
                    accDict[acc]["Amount"] += z
                    print("Amount Deposited\n")
                    y = input("Do you want to go back to Main Menu (y/n)")
                    match y:
                        case "y":
                            main()
                        case "n":
                            exit()
                else:
                    print("Deposit amount should be multiple of 100")
                    main()
    else:
        print("Account Not found .... Returning to Main Menu")
        main()


def accounts():
    print("AccNo   UserName    Amount")
    for x in accDict.keys():
        print(x, accDict[x]["Username"], accDict[x]["Amount"])
    y = input("Do you want to go back to Main Menu (y/n)")
    match y:
        case "y":
            main()
        case "n":
            exit()


def exit():
    print("Visit Again!!")


def balance():
    x = int(input("Enter the account Number "))
    if x in accDict.keys():
        print("Username : ", accDict[x]["Username"])
        print("Balance : ", accDict[x]["Amount"])
        y = input("Do you want to go back to Main Menu (y/n)")
        match y:
            case "y":
                main()
            case "n":
                exit()
    else:
        print("Account does not exist \n Returning to main menu \n")
        main()


if __name__ == "__main__":
    main()
