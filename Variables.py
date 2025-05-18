class Bank:
    # Class variable shared by all instances
    bank_name = "Default Bank"

    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def display_info(self):
        print(f"Account Holder: {self.account_holder}, Bank: {Bank.bank_name}")

# Create instances
acc1 = Bank("Faheem")
acc2 = Bank("Ali")

# Display initial bank name
acc1.display_info()
acc2.display_info()

# Change the bank name using class method
Bank.change_bank_name("National Bank")

# Display updated bank name for all instances
acc1.display_info()
acc2.display_info()
