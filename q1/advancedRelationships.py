class BankAccount:
    def __init__(self, account_holder, PIN, balance, frozen):
        self.account_holder = account_holder
        self._PIN = PIN
        self._balance = balance
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

class CheckAccount(BankAccount):
  def __init__(self, account_holder, PIN, balance, frozen, fee_rate=0.05):
    super().__init__(account_holder, PIN, balance, frozen)
    self.fee_rate = fee_rate

  def withdraw(self, amount, PIN):
    fee = amount * fee_rate
    totalamount = amount + fee

    if totalamount > self.balance:
      return f"Insufficient funds. Please try again."
      return super().withdraw(total_amount, PIN)

class DebitCard:
    def __init__(self, bank_account, bank_number):
      self.bank_account = bank_account
      self.__bank_number = bank_number

    def display_info(self):
      return f"\nCard number: {self.__bank_number}\nOwner: {self.bank_account.account_holder}"

    def purchase(self, amount, PIN):
      return self.bank_account.withdraw(amount, PIN)
