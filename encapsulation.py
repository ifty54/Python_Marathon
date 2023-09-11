<!--Usage of @property decorator-->
## Getter
class Person:
  def __init__(self, name):
    self._name = name
  
  @property
  def name(self):
    return self._name
  
c = Person("Al Amin")
print(c.name)

## Setter
class Person:
  def __init__(self, name):
    self._name = name
  
  @property
  def name(self):
    return self._name
  
  @name.setter
  def name(self, new_name):
    self._name = new_name
  
c = Person("Papon")
print(c.name)
c.name = "Ifty"
print(c.name)

# Ex 02
class Person:
  def __init__(self, name, age):
    self._name = name
    self._age = age
  
  @property
  def name(self):
    return self._name
  
  @name.setter
  def name(self, new_name):
    self._name = new_name
    
  @property
  def age(self):
    return self._age
  
  @age.setter
  def age(self, new_age):
    self._age = new_age
  
c = Person("Calvin", "6")
print(c.name)
print(c.age)
c.age = -17
c.name = False
print(c.name)
print(c.age)

<!--Usage of property method-->
class Person:
  def __init__(self, name):
    self._name = name
  
  def get_name(self):
    return self._name
  
  name = property(get_name)
  
c = Person("Al Amin")
print(c.name)

# Ex 02
class Person:
  def __init__(self, name):
    self._name = name
  
  def get_name(self):
    return self._name
  
  def set_name(self, new_name):
    self._name = new_name
  
  name = property(get_name, set_name)
  
c = Person("Papon")
print(c.name)
c.name = "Ifty"
print(c.name)
