class BankAccount:
    def __init__(self, account_holder, PIN, balance, frozen):
        self.account_holder = account_holder
        self.__PIN = PIN
        self.__balance = balance
        self.frozen = frozen

    def deposit(self, amount, PIN):
        if PIN != self.__PIN:
            return "Incorrect PIN. Cannot deposit."
        if self.frozen:
            return "Account is frozen. Cannot deposit."
        if amount <= 0:
            return "Deposit amount must be positive."
        
        self.__balance += amount
        return f"Deposited {amount}. New balance is {self.__balance}."

    def withdraw(self, amount, PIN):
        if PIN != self.__PIN:
            return "Incorrect PIN. Cannot withdraw."
        if self.frozen:
            return "Account is frozen. Cannot withdraw."
        if amount <= 0:
            return "Withdrawal amount must be positive."
        if amount > self.__balance:
            return "Insufficient funds."
        
        self.__balance -= amount
        return f"Withdrew {amount}. New balance is {self.__balance}."

    def displayBalance(self, PIN):
        if PIN != self.__PIN:
            return "Incorrect PIN. Cannot display balance."
        if self.frozen:
            return "Account is frozen. Cannot display balance."
        return f"Current balance is {self.__balance}."

    def freezeAccount(self):
        self.frozen = True
        return "Account has been frozen."

    def unfreezeAccount(self):
        self.frozen = False
        return "Account has been unfrozen."

account1 = BankAccount("Osamu Dazai", "6767", 1000, False)
account2 = BankAccount("Nakahara Chuuya", "4621", 5000, True)

print("")
print("----- CURRENT STATUS OF ACCOUNTS -----")
print("Account Balance of Account 1:", account1.displayBalance("6767"))
print("Account Balance of Account 2:", account2.displayBalance("4621"))

print("")
print("----- DEPOSITING 500 TO ACCOUNT 1 -----")
print("Account Balance of Account 1:", account1.deposit(500, "6767"))

print("")
print("----- UNFREEZING ACCOUNT 2 -----")
print("Account Status of Account 2:", account2.unfreezeAccount())

print("")
print("----- WITHDRAWING 2000 FROM ACCOUNT 2 -----")
print("Account Balance of Account 2:", account2.withdraw(2000, "4621"))

print("")
print("----- AFTER TRANSACTIONS -----")
print("Account Balance of Account 1:", account1.displayBalance("6767"))
print("Account Balance of Account 2:", account2.displayBalance("4621"))