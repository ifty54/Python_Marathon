#List Comprehension

list = [1,2,3,6,7]

square_for_list = [x**2 for x in list]

print(square_for_list)

#Lambda Function
##Anonymous and alternate to `def`
function = lambda x: x**2

result = function(4)

print(result)

#Filter
numbers = [1,3,4,6,7,8]

even_numbers = list(filter(lambda x: x%2==0, numbers))

print(even_numbers)

#Map
even_numbers_squared = list(map(lambda x: x**2, even_numbers))

print(even_numbers_squared)

#Reduce
from functools import reduce
sum = reduce(lambda a,b: a+b, even_numbers_squared)
