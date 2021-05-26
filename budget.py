import builtins as __builtin__



class Entry: 
  amount = 0
  description = ""

  def __init__(self, amount,description):
    amount = amount
    description = description



class Category:
  ledger = []
  _category = None
  _balance = 0

  def __init__(self,category):
    _category = category
  
  def __str__(self):
    return "My overridden print() function!"

  def deposit(self, amount, description):
    entry = Entry(amount, description)
    ledger.append(entry)
    _balance += amount

  def withdraw(amount, description):
    if this.check_funds(amount):
      return False
    else:
      entry = Entry(-amount, description)
      ledger.append(entry)
      _balance -= amount
      return True

  def get_balance():
    return _balance

  def transfer(amount, budget):
    if check_funds(amount):
      return False
    else:
      this.withdraw(amount, "Transfer to " + budget._category)
      budget.deposit(amount, "Transfer from " + _category)
      return True

  def check_funds(amount):
    if amount > _balance:
      return False
    else:
      return True


def create_spend_chart(categories):
  return ""