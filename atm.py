def main():
    balance = 1000  # Starting balance in Ksh

    while True:
        # Present the menu to the user
        print("\nCooperative Bank of Kenya")
        print("\nWelcome To Cooperative Bank of Kenya")
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        # Get the user's option
        option = input("Enter your choice (1-4): ")

        # Handle the user's option using if-elif-else statements
        if option == '1':
            print(f"Your current account balance is: Ksh.{balance}")
            print(f"Your working balance is: Ksh.{balance}")
        
        elif option == '2':
            try:
                amount = float(input("Enter the amount to deposit: "))
                if amount <= 0:
                    print("Please enter a positive amount.")
                else:
                    balance += amount
                    print(f"Ksh.{amount} has been deposited to your account.\n Your new account balance is: Ksh.{balance}")
            except ValueError:
                print("Invalid input. Please enter a numerical value.")
        
        elif option == '3':
            try:
                amount = float(input("Enter the amount to withdraw: "))
                if amount <= 0:
                    print("Please enter a positive amount.")
                elif amount > balance:
                    print("You have insufficient balance your.")
                else:
                    balance -= amount
                    print(f"Ksh.{amount} has been withdrawn. Your new balance is: Ksh.{balance}")
            except ValueError:
                print("Invalid input. Please enter a numerical value.")
        
        elif option == '4':
            print("Thank you for choosing Cooperative Bank.\nGoodbye! \nWelcome Again!")
            break
        
        else:
            # Invalid option
            print("Invalid option. Please select a valid option (1-4).")

if __name__ == "__main__":
    main()