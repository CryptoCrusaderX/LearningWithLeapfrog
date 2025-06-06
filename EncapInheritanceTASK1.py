class BankAccount:
    def __init__(self, account_holder, account_type, balance):
        self.acc_holder = account_holder
        self._acc_type = account_type
        self.__balance = balance

    def display_acc_details(self):
        print(
            f"\nAccount Holder Name:{self.acc_holder}\n"
            f"Account Type:{self._acc_type}\n"
            f"Account Balance:{self.__balance}"
        )

    def _update_account_type(self, new_acctype):
        if new_acctype:
            self._acc_type = new_acctype
            print(
                f"\nYour account type has been sucsessfully changed to {new_acctype.upper()}"
            )
        else:
            raise ValueError("Account type can't be empty")

    def __validate_transaction(self, amount):
        if amount <= 0:
            print("Amount Must be positive")

    def deposit(self, amount):
        self.__validate_transaction(amount)
        self.__balance += amount
        print(f"Amount Rs.{amount} is deposited into your Account")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance = self.__balance - amount
            print(f"\n{amount} of money has been withdrawn from you bank account.")
        else:
            print("Withdrawl amount is more than than actual bank balance")

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, new_balance):
        self.__balance += new_balance


bank = BankAccount("Sarad", "Saving", 10000)
bank.display_acc_details()
bank._update_account_type("Current")
bank.deposit(20000)
print(f"Bank Balance:{bank.balance}")
bank.withdraw(5000)
print(f"Bank Balance after withdrawl:{bank.balance}")
