class Category:
    def __init__(self, name: str):
        self.name = name
        self.ledger = []
        self.balance = 0
        self.deposits = []
        self.withdrawls = []

    def deposit(self, amount: int, description=""):
        """
        Accepts an amount and description. If no description is given
        is should default to an empty string. The method should append
        an object to the ledger in the form {"amount": amount, "description": description}.
        """
        self.balance += amount
        self.ledger.append({"amount": amount, "description": description})
        self.deposits.append(amount)
        
    def withdraw(self, amount, description=""):
        """
        Similar to deposit, but the amount passed in
        should be stored in the ledger as a negative
        number. If there are not enough funds nothing should be
        added to the ledger. This method should return True if the 
        withdrawl took place and False otherwise.
        """
        if self.check_funds(amount):
            self.withdrawls.append(amount)
            self.balance -= amount
            amount *= -1
            self.ledger.append({"amount": amount, "description": description})
            
        
    def get_balance(self):
        """
        Returns the current balance of the budget category based
        on deposits and withdrawls that have occurred.
        """
        return self.balance
    
    def transfer(self, amount, cat):
        """
        method that accepts an amount and another budget category as arguments. The method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]". The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]". If there are not enough funds, nothing should be added to either ledgers. This method should return True if the transfer took place, and False otherwise.
        """

    def check_funds(self, amount: int):
        """
        accepts an amount as an argument. It returns False if the amount is greater than the balance of the budget category and returns True otherwise. This method should be used by both the withdraw method and transfer method.
        """
        if self.balance < amount:
            return False
        else:
            return True

    def __str__(self):
        pass
        
def create_spend_chart(categories):
    pass

if __name__ == "__main__":

    food = Category("Food")
    food.deposit(1000, "initial deposit")
    food.withdraw(10.15, "groceries")
    food.withdraw(15.89, "restaurant and more food for dessert")
    print(food.get_balance())
    clothing = Category("Clothing")
    food.transfer(50, clothing)
    # clothing.withdraw(25.55)
    # clothing.withdraw(100)
    # auto = budget.Category("Auto")
    # auto.deposit(1000, "initial deposit")
    # auto.withdraw(15)

    # print(food)
    # print(clothing)

    # print(create_spend_chart([food, clothing, auto]))

    # # Run unit tests automatically
    # main(module='test_module', exit=False)