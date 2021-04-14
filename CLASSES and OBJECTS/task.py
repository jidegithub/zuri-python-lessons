class Budget:
  def __init__(self, name):
    self.name = name
    self.balance = 0
 

  def deposit(self, amount):
    self.balance += amount
    return f"your new balance is \u20A6{self.balance} in {self.name} budget"

  def withdraw(self, amount):
    if(self.balance < amount):
      return f"insufficient funds"
    else:
      self.balance -= amount
      feedback = f"withdrawal of \u20A6{amount} is successful\n"
      feedback += f"your new balance is \u20A6{self.balance} in {self.name} budget"
      return feedback
  
  def get_balance(self):
    feedback = f"the balance for {self.name} is \u20A6{self.balance}"
    return feedback

  def transfer(self, amount, destination_category):
    if(self.name == destination_category.name):
      feedback = f"you cannot transfer within the same category"
      return feedback
    else:
      if(self.balance < amount):
        return f"insufficient funds"
      else:
        self.balance -= amount
        destination_category.balance += amount
        account_balance = self.get_balance()
        feedback = "===**===\n"
        feedback += f"you have successfully transferred \u20A6{amount} to {destination_category.name}\n"
        feedback += f"{account_balance}\n"
        return feedback
  



Food = Budget("food")
Clothing = Budget("clothing")

print(Clothing.deposit(5000))
print(Food.deposit(15000))
print(Food.withdraw(5000))
print(Food.transfer(5000, Clothing))
print("destination \n ===*===")
print(Clothing.get_balance())