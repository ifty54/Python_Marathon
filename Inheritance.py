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
