class Category:
  def __init__(self):
    self.ledger = []

    def deposit(self, amount: int, description=None):
        """
        Accepts an amount and description. If no description is given
        is should default to an empty string. The methos should append
        an object to the ledger in the form {"amount": amount, "description": description}.
        """
        if description == None:
            ledger.append({"amount": amount, "description": ""})
        else:
            ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount):
        """
        Similar to deposit, but the amount passed in
        should be stored in the ledger as a negative
        number. If there are not enough funds nothing should be
        added to the ledger. This method should return True if the 
        withdrawl took place and False otherwise.
        """
    def get_balance(self):
        """
        Returns the current balance of the budget category based
        on deposits and withdrawls that have occurred.
        """

    def transfer(self, amount, cat):
        """
        method that accepts an amount and another budget category as arguments. The method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]". The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]". If there are not enough funds, nothing should be added to either ledgers. This method should return True if the transfer took place, and False otherwise.
        """

    def check_funds():
        """
        accepts an amount as an argument. It returns False if the amount is greater than the balance of the budget category and returns True otherwise. This method should be used by both the withdraw method and transfer method.
        """

def create_spend_chart(categories):
    pass