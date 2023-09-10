# Example 01:
class CelestialBody:
  def __init__(self, size, mass, composition, name):
    self.size = size
    self.mass = mass
    self.composition = composition
    self.name = name
    
# create the satellite class
class Satellite(CelestialBody):
  def __init__(self, size, mass, composition, name, host_planet):
    super().__init__(size, mass, composition, name)
    self.host_planet = host_planet

# create the planet class
class Planet(CelestialBody):
  def __init__(self, size, mass, composition, name, host_star):
    super().__init__(size, mass, composition, name)
    self.host_star = host_star

# Example 02:
## Creating the child class BlogPost and override the constructor so that the child class has the following attributes:
# parent class
class Book:
  def __init__(self, title, author, pages, genre):
    self.title = title
    self.author = author
    self.genre = genre

# child class
class BlogPost(Book):
  def __init__(self, website, title, author, word_count, genre, page_views):
    super().__init__(title, author, genre)
    self.website = website
    self.word_count = word_count
    self.page_views = page_views

# Example 03
class Parent1:
  def identify(self):
    return "This method is called from Parent1"
    
class Parent2:
  def identify(self):
    return "This method is called from Parent2"
    
# declare child class here
class Child(Parent2, Parent1):
  def identify(self):
    return "This method is called from Child"
  
  def identify2(self):
    return super().identify()

# Example 04
import sys
strings = [l.split(",") for l in sys.argv[1].split("*")]
accounts = [[int(n) for n in s] for s in strings]

class Bank:
  def __init__(self, name, customers, accounts):
    self.name = name
    self.customers = customers
    self.accounts = accounts
    
  def branch_total(self, accounts):
    total = 0
    for account in accounts:
      total += account
    return total

# Write your code here
class RegionalBank(Bank):
  def regional_total(self):
    total = 0
    for account in accounts:
      total += self.branch_total(account)
    return total
  
my_bank = RegionalBank("Bank of America", 9, accounts)
print(my_bank.regional_total())

# Example 05 
# The first parent is the Person class with some very generic information. The second class, CardHolder, is the class for a credit card holder. Create the child class PlatinumClient. This class inherits all of the attributes of both parent classes. In addition, the child class has the attributes cash_back and rewards. cash_back should be set to 0.02 and rewards should be set to 0. Override the process_sale method so that 2% of each sale is added to rewards.
# parent classes
class Person:
  def __init__(self, name, address):
    self.name = name
    self.address = address
    
  def get_info(self):
    return f"{self.name} lives at {self.address}."
  
class CardHolder:
  def __init__(self, account_number):
    self.account_number = account_number
    self.balance = 0
    self.credit_limit = 5000
    
  def process_sale(self, price):
    self.balance += price
    
  def make_payment(self, amount):
    self.balance -= amount
    
# declare child class here
class PlatinumClient(Person, CardHolder):
  def __init__(self, name, address, account_number):
    Person.__init__(self, name, address)
    CardHolder.__init__(self, account_number)
    self.cash_back = 0.02
    self.rewards = 0
    
  def process_sale(self, price):
    self.balance += price
    self.rewards += self.cash_back * price
