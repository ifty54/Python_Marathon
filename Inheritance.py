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
