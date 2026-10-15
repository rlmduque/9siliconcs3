class BankAccount:
      def __init__(self, account_number = 0, balance = 0):
            self._account_number = account_number
            self._balance = balance

      def set_account_number(self, account_number):
            self._account_number = account_number #This ensures that the given value of account_number would be stored in the private attribute.

      def set_balance(self, balance):
            if balance<0:
                        print("The balance must not be a negative number.")
                        print(f"Account Number: {a1.get_account_number()}")
                        print(f"Balance: {float(a1.get_balance()):.2f}")
                        raise SystemExit #This stops the code because a negative balance would make the program logically invalid.
            else:
                        print(f"Account Number: {a1.get_account_number()}")
                        self._balance = balance 
                        return balance

      def get_account_number(self):
            return self._account_number

      def get_balance(self):
            return self._balance

a1 = BankAccount(12345, 1000) #I used the given example in the module to sample the program.

print("Account 1")
print(f"Account Number: {a1.get_account_number()}")
print(f"Balance: {float(a1.get_balance()):.2f}") #This ensures that the balance is a float. The :.2f also ensures that the balance number is reduced only to the hundredths.

print("")
print("Update balance to -100")
print(f"Balance: {float(a1.set_balance(-100)):.2f}") #When this attribute is called, it runs the if-else statement and checks whether the set balance is negative or positive then the code either proceeds with the program and returns the new set balance or stops the program.