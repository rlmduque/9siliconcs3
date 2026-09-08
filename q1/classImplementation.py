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

    