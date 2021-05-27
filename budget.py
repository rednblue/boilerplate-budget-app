class Category:

  def __init__(self,category):
    self.category = category
    self.ledger = []
    self.balance = 0
  
  def __str__(self):
    output = ""
    l = int((30 - len(self.category)) / 2)
    
    output += self.add_asterisks(l)
    output += self.category
    output += self.add_asterisks(l) + "\n"

    for entry in self.ledger:
      output += entry["description"][:23] + (" " * (23 - len(entry["description"][:23])))
      output += " "
      a = format(entry["amount"], '.2f')
      output += " " * (7 - len(str(a))) + a + "\n"
    
    output += "Total: " + str(self.balance)
    return output

  def add_asterisks(self, l):
    return "*" * l

  def deposit(self, amount, description = None):
    if description is None:
      description = ""
    self.ledger.append({"amount":amount,"description":description})
    self.balance += amount

  def withdraw(self, amount, description =None):
    if self.check_funds(amount):
      if description is None:
        description = ""
      self.ledger.append({"amount":-amount,"description":description})
      self.balance -= amount
      return True
    return False

  def get_balance(self):
    return self.balance

  def transfer(self, amount, budget):
    if self.check_funds(amount):
      self.withdraw(amount, "Transfer to " + budget.category)
      budget.deposit(amount, "Transfer from " + self.category)
      return True
    return False
      

  def check_funds(self, amount):
    if amount > self.balance:
      return False
    else:
      return True


def create_spend_chart(categories):
  output = "Percentage spent by category\n"
  spent = []
  lens = []
  total = 0

  for c in categories:
    spent.append(c.balance)
    lens.append(len(c.category))
    total += c.balance

  maxL = max(lens)

  for i in range(len(spent)):
    spent[i] = approximate_10(int((spent[i] / total) * 100))

  for i in range(100, 0, -10):
    output += " " * (3 - len(str(i))) + str(i) + "| "
    for j in spent:
      if j >= i:
        output += "o "
      else:
        output += " " * 2
    output += "\n"

  output += (" " * 4) + "----------" + "\n"

  for i in range(0, maxL):
    output += (" " * 5)
    for c in categories:
      try:
        output += c.category[i] + " "
      except:
        output += " " * 2
    output += "\n"

  #print(spent)

  return output

def approximate_10(n):
  #print(n)
  r = n % 10
  if r < 5:
    return n - r
  return n - r + 10