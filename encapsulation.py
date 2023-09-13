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


# Ex 03
class Dancer:
  def __init__(self, name, nationality, style):
    self._name = name
    self._nationality = nationality
    self._style = style
    
  def get_name(self):
    return self._name
  
  def set_name(self, new_value):
    self._name = new_value
    
  def get_nationality(self):
    return self._nationality
  
  def set_nationality(self, new_value):
    self._nationality = new_value
    
  def get_style(self):
    return self._style
  
  def set_style(self, new_value):
    self._style = new_value
    
  name = property(get_name, set_name)
  nationality = property(get_nationality, set_nationality)
  style = property(get_style, set_style)

# Ex 04
class Cyclist:
  def __init__(self, name, nationality, nickname):
    self._name = name
    self._nationality = nationality
    self._nickname = nickname
    
  @property
  def name(self):
    return self._name
  
  @name.setter
  def name(self, new_value):
    self._name = new_value
    
  @property
  def nationality(self):
    return self._nationality
  
  @nationality.setter
  def nationality(self, new_value):
    self._nationality = new_value
    
  @property
  def nickname(self):
    return self._nickname
  
  @nickname.setter
  def nickname(self, new_value):
    self._nickname = new_value
