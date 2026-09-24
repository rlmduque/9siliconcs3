class BankAccount:
    def __init__(self, account_holder, PIN, balance, frozen):
        self.account_holder = account_holder
        self._PIN = PIN
        self._balance = balance
        self.frozen = frozen
        self.cards = []

    def add_card(self, bank_number):
      new_card = DebitCard(self, bank_number)
      self.cards.append(bank_number)
      return new_card
    
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

class DebitCard:
    def __init__(self, bank_account, bank_number):
      self.bank_account = bank_account
      self.__bank_number = bank_number

    def display_info(self):
      return f"\nCard number: {self.__bank_number}\nOwner: {self.bank_account.account_holder}"

    def purchase(self, amount, PIN):
      return self.bank_account.withdraw(amount, PIN)

print("")
print(" -- BEFORE RELATIONSHIP -- ")
new_account = BankAccount("Gregor Samsa", "7396", 3000, False)
print(f"Account Holder: {new_account.account_holder}\nCards List: {new_account.cards}\nNo debit card connected.")

print("")
print(" -- DURING RELATIONSHIP --")
new_card = new_account.add_card("3141-5926-5358-9793")
print(f"Card created: {new_card.display_info()}")
print(f"Updated cards list: {new_account.cards}")

print("")
print(" -- AFTER RELATIONSHIP --")
print(f"Current balance: {new_account.displayBalance("7396")}")
print("")
print("PURCHASING ₱499 MEAL")
print(f"Balance after purchase: {new_card.purchase(499, "7396")}")
