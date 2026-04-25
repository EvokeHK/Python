class BankAcc:
    def __init__(self, accNo, name, amount):
        self.accNo = accNo
        self.name = name
        self.amount = amount

    def getamount(self):
        return self.amount

    def getname(self):
        return self.name

    def getaccNo(self):
        return self.accNo

    def withdraw(self, x):
        self.amount -= x

    def deposit(self, x):
        self.amount += x


class Error(Exception):
    def __init__(self, message, error_code):
        self.message = message
        self.error_code = error_code

    def __str__(self):
        return f"{self.message} (Error Code : {self.error_code})"


accDict = {}
accNo = 10020100

import os
import pickle

if os.path.exists("BankAcc.pkl") and os.path.getsize("BankAcc.pkl"):
    with open("BankAcc.pkl", "rb") as f:
        accDict = pickle.load(f)
        accNo = max(accDict.keys()) + 1


while True:
    i = int(
        input(
            """MAIN MENU \n
                  1. Create Account
                  2. Transaction
                  3. Check Account Balance
                  4. All Accounts
                  5. Remove Account
                  6. Exit\n"""
        )
    )
    match i:
        case 1:
            username = input("Enter the User Name :")
            amount = int(input("Enter the initial Amount :"))
            while (amount % 100 != 0) or (amount < 1000):
                amount = int(
                    input(
                        "The initial amount should be multiple of 100 and more than 1000\n Enter the amount again \n"
                    )
                )
            b = BankAcc(accNo, username, amount)
            print("Account ", accNo, " Created")
            accDict[accNo] = b
            accNo += 1
        case 2:
            x = int(input("Enter the Account Number : "))
            while x in accDict:
                y = int(
                    input(
                        """MENU \n
                                1. Withdraw`
                                2. Deposit 
                                3. Show account Balance
                                4. Exit\n"""
                    )
                )
                match y:
                    case 1:
                        z = int(input("Enter the amount to be withdrawn "))
                        if accDict[x].getamount() - z > 1000 and z % 100 == 0:
                            accDict[x].withdraw(z)
                            print("Amount Successfully Withdrawn \n")
                        else:
                            print(
                                "Withdrawal amount should be multiple of 100 and final balance should be more than 1000 .....\nreturning to Main Menu"
                            )

                    case 2:
                        z = int(input("Enter the amount to be deposited :"))
                        if z % 100 == 0:
                            accDict[x].deposit(z)
                            print("Amount Deposited\n")
                        else:
                            print("Deposit amount should be multiple of 100")
                    case 3:
                        print("The account Balance is :", accDict[x].getamount())
                    case 4:
                        break
                    case _:
                        print("Invalid input!!")
            else:
                print("Enter valid Account Number!!!!")
        case 3:
            x = input("Enter the Account Number :")
            if x in accDict:
                print("Username : ", accDict[x]["Username"])
                print("Balance : ", accDict[x]["Amount"])
            else:
                print("Account does not exist \n Returning to main menu \n")

        case 4:
            print("AccNo   UserName    Amount")
            for x in accDict:
                print(x, accDict[x].getname(), accDict[x].getamount())

        case 5:
            x = input("Enter the account to  be removed :")
            if x in accDict:
                del accDict[x]
                print("Account Removed")
            else:
                print("Account not Found")
        case 6:
            with open("BankAcc.pkl", "wb") as f:
                pickle.dump(accDict, f)
            break
        case _:
            print("Invalid Input!!")
