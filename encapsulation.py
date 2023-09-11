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
