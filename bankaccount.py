accNo = 10020100
accCount = 0

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
    

def account():

def exit():

if __name__ == "__main__":
    main()
