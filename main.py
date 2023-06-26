##98 Programming Solutions

#1 Print Operation
print("Hello World")

#2 Adding Two Numbers
num1 = 4
num2 = 5
sum = num1 + num2
print(f"The sum of {num1} and {num2} is: {sum}")

#3 Finding Square Root
a = 9
sqrt_a = a**0.5
print(f"The square root of {a} is: {sqrt_a}")

#4 Area of Triangle (1st Approach)

base = float(input("Enter: "))
height = float(input("Enter: "))
hypotenuse = float(input("Enter: "))

triangle_area1 = (1 / 2) * base * height

print(f"The 01 triangle area is: {triangle_area1}")

#4 Area of Triangle (2nd Approach)
b = float(input("Enter: "))
c = float(input("Enter: "))
d = float(input("Enter: "))

s = ((b + c + d) / 2)

triangle_area2 = (s * (s - b) * (s - c) * (s - d))**0.5

print(f"The 02 triangle area is: {triangle_area2:.1f}")

#5 Quadratic Eqn (ax2+bx+c=0),(-b±(b**2-4*a*c)**0.5)/(2*a)

import cmath

a1 = 1
b1 = 5
c1 = 6

determinant = ((b1**2) - (4 * a1 * c1))

solution01 = (-b1 + cmath.sqrt(determinant)) / (2 * a1)

solution02 = (-b1 - cmath.sqrt(determinant)) / (2 * a1)

print(f"The two solutions : {solution01} & {solution02}")

#6 Swapping 2 variables

var1 = 4
var2 = 9

temp = var1
var1 = var2
var2 = temp

print(f"the result after swapping: {var1} & {var2}")

#7 Random Number

import random

print(random.randint(0, 100))

#8 Convert: km to miles

km = 5
conv_factor = 0.621
miles = km * conv_factor
print(f"The miles will be: {miles}")

#9 Convert: Celcius to Fahrenheit

cel = 98
fahr = (cel * (9 / 5)) + 32
print(f"Fahrenheit: {fahr}")

#10 Number +, - or zero (if else)

number1 = float(input("Enter your number: "))

if number1 > 0:
  print("It's positive")
elif number1 == 0:
  print("It's zero")
else:
  print("It's Negative")

#10 Number +, - or zero (Nested if)

number2 = float(input("Enter your number: "))

if number2 >= 0:
  if number2 == 0:
    print("Zero")
  else:
    print("Positive")
else:
  print("Negative")

#11 Number Even or Odd

value = float(input("Enter your Number: "))

if ((value % 2) == 0):
  print(f"{value} is even")
else:
  print(f"{value} is odd")

#12 Leap Year
year = int(input("Enter Year: "))

if (year % 400 == 0 and year % 100 == 0):
  print(f"{year} is LEAP")
elif (year % 4 == 0 and year % 100 != 0):
  print(f"{year} is LEAP")
else:
  print(f"{year} is Not LEAP")

#13 Largest Number

val1 = int(input("Enter your 1st value: "))
val2 = int(input("Enter your 2nd value: "))
val3 = int(input("Enter your 3rd value: "))

if (val1 >= val2 and val1 >= val3):
  largest = val1
elif (val2 >= val1 and val2 >= val3):
  largest = val2
else:
  largest = val3

print(f"{largest} is the largest number")

#14 Prime Number

flag = False

num = int(input("Enter Number: "))

if num == 1:
  print(f"{num} is not a prime")
elif num > 1:
  for i in range(2, num):
    if (num % i) == 0:
      flag = True
      break
  if flag:
    print(f"{num} is not a prime number")
  else:
    print(f"{num} is a prime number")

#15 Prime in Range Interval

lower = 300
upper = 400

print(f"Primes between {lower} & {upper} are: ")

for numb in range(lower, upper):
  if numb >= lower:
    for value in range(2, numb):
      if (numb % value) == 0:
        break
    else:
      print(numb)

#16 Factorial

fact_num = int(input("Enter your number: "))

factorial = 1

if fact_num < 0:
  print("No Factorial")
elif fact_num == 0:
  print("Factorial is 1")
else:
  for id in range(1, fact_num + 1):
    factorial = factorial * id
  print(f"{factorial} is the factorial")

#17 Multiplication Table

m = int(input("Enter your number: "))

for n in range(1, 11):
  print(f"{m}*{n}={m*n}")

#18 Fibonacci Series

nterms = int(input("How many terms you want: "))

n1 = 0
n2 = 1

count = 0

if nterms <= 0:
  print("Enter a positive number")
elif nterms == 1:
  print(n1)
else:
  print("This is Fibonacci Number")
  while count < nterms:
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1

#19 Armstrong Number

your_num = int(input("Enter: "))

pow = len(str(your_num))
sum1 = 0

temp1 = your_num
while temp1 > 0:
  digit = temp1 % 10
  sum1 += digit**pow
  temp1 //= 10

if your_num == sum1:
  print("This is Armstrong")
else:
  print("It's not Armstrong")

#20 Armstrong in Interval

low_limit = 200
up_limit = 1000

for your_num2 in range(low_limit, up_limit + 1):
  order = len(str(your_num2))
  sum2 = 0
  temp2 = your_num2
  while temp2 > 0:
    digit2 = temp2 % 10
    sum2 += digit2**order
    temp2 //= 10
  if your_num2 == sum2:
    print(sum2)

#21 Natural Num Sum

total = int(input("enter number: "))

if total < 0:
  print("Enter a positive number")

else:
  total_sum = 0
  while (total > 0):
    total_sum += total
    total -= 1
  print(f"The sum is {total_sum}")

#22 Power of 2

term = int(input("How many terms?: "))
print(f"Total terms are: {term}")

result = list(map(lambda x: 2**x, range(term)))

for i_term in range(term):
  print(f"{result[i_term]}")

#23 Divisibility
my_list = [12, 65, 54, 39, 102, 339, 220]

outcome = list(filter(lambda x: (x % 19 == 0), my_list))
print(f"Numbers divisible by 19 are:  {outcome}")

#24 Dec-Bin-Hexa-Oct

dec = int(input("Enter your decimal number: "))

print(f"Binary will be: {bin(dec)}")
print(f"Binary will be: {oct(dec)}")
print(f"Binary will be: {hex(dec)}")

#25 ASCII

my_input = "i"

print(f"ASCII value of {my_input} is {ord(my_input)}")

#26 HCF & GCD

hcf1 = int(input("first: "))
hcf2 = int(input("second: "))

if (hcf1 > hcf2):
  smaller = hcf2
else:
  smaller = hcf1
for no_i in range(1, smaller + 1):
  if ((hcf1 % no_i == 0) and (hcf2 % no_i == 0)):
    hcf = no_i
print(f"The HCF is {hcf}")

#27 LCM

lcm1 = int(input("First: "))
lcm2 = int(input("Second: "))

if lcm1 > lcm2:
  greater = lcm1
else:
  greater = lcm2
while (True):
  if ((greater % lcm1 == 0) and (greater % lcm2 == 0)):
    lcm = greater
    break
  greater = greater + 1

print(f"LCM is {lcm}")

#28 Factors of A Number

num0 = int(input("Number: "))
factors = []

for i0 in range(1, num0 + 1):
  if (num0 % i0 == 0):
    factors.append(i0)
print(f"the factors of {num0} are: {factors}")

#29 Calculator

print("Select Operation")
print("1 for add, 2 for sub, 3 for mul, 4 for div")
choice = input("Enter Choice(1,2,3,4): ")

if choice in ("1", "2", "3", "4"):
  try:
    val01 = float(input("1st number: "))
    val02 = float(input("2nd number: "))
  except ValueError:
    print("Invalid")

  if choice == "1":
    print(f"{val01 + val02}")
  elif choice == "2":
    print(f"{val01 - val02}")
  elif choice == "3":
    print(f"{val01 * val02}")
  elif choice == "4":
    print(f"{val01 / val02}")
  else:
    print("Invalid Input")

#30 Shuffle Deck of Cards

import itertools, random

deck = list(
  itertools.product(range(1, 14), ['spade', 'heart', 'diamond', 'club']))

random.shuffle(deck)

print("You have got: ")
for i_deck in range(5):
  print(deck[i_deck][0], "of", deck[i_deck][1])

#31 Calendar

import calendar

yy = 2023
mm = 6

print(f"{calendar.month(yy,mm)}")

#32 Fibonacci through Recursion


def fib(n):
  if n <= 1:
    return n
  else:
    return (fib(n - 1) + fib(n - 2))


nos = 20

if nos <= 0:
  print("Enter any positives")
else:
  print("Fibonacci Sequence")
  for i_fib in range(nos):
    print(fib(i_fib))


#33 Natural Number Recursion
def nat(n):
  if n <= 1:
    return 1
  else:
    return n + nat(n - 1)


tot = 10

if tot < 0:
  print("Enter a positive number")
else:
  print(f"the sum is {nat(tot)}")

#34 Factorial Recursion


def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)


ex = 5

if ex < 0:
  print("print something positive")
else:
  print(f"{ex}'s has the factorial of {factorial(ex)}")


#35 Dec to Bin via Recursion
def dec_bin(n):
  if n > 1:
    dec_bin(n // 2)
  print(n % 2, end='')


dec = 34

dec_bin(dec)
print()

#36 Adding 2 Matrices
xx = [[1,2,3],[4,5,6],[7,8,9]]
yy = [[3,6,4],[4,1,7],[3,4,1]]

final = [[0,0,0],[0,0,0],[0,0,0]]

for ii in range(len(xx)):
  for jj in range(len(xx[0])):
    final[ii][jj] = xx[ii][jj] + yy[ii][jj]
for r in final:
  print(r)
  
#37 Transpose a Matrix
matrix = [[1,2],[3,6],[8,7]]

finale = [[0,0,0],[0,0,0]]
for i in range(len(matrix)):
  for j in range(len(matrix[0])):
    finale[j][i] = matrix[i][j]

for r in finale:
  print(r)

#38 Multiply two Matrices
xx = [[1,2,3],
      [4,5,6],
      [7,8,9]]

yy = [[3,6,4],
      [4,1,7],
      [3,4,1]]

final = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(xx)):
  for j in range(len(yy[0])):
    for k in range(len(yy)):
      final[i][j] += xx[i][k] * yy[k][j]

for r in final:
  print(r)

#39 Palindrome
my_string = "amMa"
my_string = my_string.casefold()

rev_string = reversed(my_string)

if list(my_string) == list(rev_string):
  print("It's Palindrome")
else:
  print("It's not Palindrome")

#40 Removing Punctuations
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

line = "hey!! Make it- simple!#"

no_punc = ""
for char in line:
  if char not in punctuations:
    no_punc = no_punc + char
print(no_punc)

#41 Sort Alphabetic Order
kw = input("Enter a string: ")

words = [word.lower() for word in kw.split()]

words.sort()

print("The words order will be:")
for word in words:
  print(word)

#42 Set operation
E = {0, 2, 4, 6, 8}
N = {1, 2, 3, 4, 5}

print(f"Union: {E|N}")
print(f"Intersection: {E & N}")
print(f"Difference: {E-N}")
print(f"Symmetric: {E^N}")

#43 Count Vowel
vow = 'aeiou'
line = input("Enter your line: ")

line = line.casefold()

count_vow = {}.fromkeys(vow, 0)

for character in vow:
  if character in count_vow:
    count_vow[character] += 1

print(count_vow)

#44 Merge Mails
with open("names.txt", "r", encoding="utf-8") as names_file:
  with open("body.txt", "r", encoding="utf-8") as body_file:
    body = body_file.read()
    for name in names_file:
      mail = "Hello" + name.strip() + "\n" + body
      with open(name.strip() + ".txt", "w", encoding="utf-8") as mail_file:
        mail_file.write(mail)


#45 Finding Image Size
def jpeg_res(filename):

  with open(filename,
            'rb') as img_file:  # open image for reading in binary mode

    img_file.seek(163)  # height of image (in 2 bytes) is at 164th position

    a = img_file.read(2)  # read the 2 bytes

    height = (a[0] << 8) + a[1]  # calculate height

    a = img_file.read(2)  # next 2 bytes is width

    width = (a[0] << 8) + a[1]  # calculate width

  print("The resolution of the image is", width, "x", height)


filename = "a.jpg"

jpeg_res(filename)

#46 Incomplete

#47 Pyramid Patterns

rows = int(input("enter rows: "))

for i_rows in range(rows):
  for j_rows in range(i_rows+1):
    print(j_rows+1, end=" ")
  print("\n")

#48 Dict Merging
dict1 = {1: "john", 2: "doe"}
dict2 = {2: "mark", 3: "chapel"}

print(dict1 | dict2)
print({**dict1, **dict2})

dict3 = dict1.copy()
dict3.update(dict2)
print(dict3)

#49 Nested Dict
from pathlib import Path
Path("D:/Computer").mkdir(parents =True, exist_ok=True)

#50 Trace index using loop
list = [1,2,4,6,7]
for index, val in enumerate(list):
  print(f"{index} : {val}")

#51 Flatten a nested list
list = [1,5,7,8,[5,7,8]]

for index in list:
  list_copy = list[-1]

list_final = list[:-1] + list_copy

print(list_final)

#52 Slice list
list = [1,4,6,7,8]

print(list[:2])

#53 Iterate over dict using loop
dict = {1:"a",2:"b",3:"c"}

for key, value in dict.items():
  print(key, value) ##Difference: in list, we mention enumerate(list)
  
#54 Sort dict by value
dict = {"1st":23,"2nd":45,"3rd":11}
sorted_dict = sorted(dict.values())
print(sorted_dict)

#55 Check empty list
list = [1,2]

if not list:
  print("it's empty")

print("It's not!")

#56 Detect exceptions in line
str = input("Enter: ")

try:
  num = int(input())
  print(str+num)
except (TypeError, ValueError) as e:
  print(e)

#57 Copy a file
from shutil import copyfile
copyfile("/root/a.txt", "/root/b.txt")

#58 Concatenate 2 lists
list1 = [3,5,6]
list2 = [1,9,8]
list1.extend(list2)
print(list1)

#59 Key in dict
dict = {1:"messi", 2:"ronaldo", 3:"haaland"}
if 2 in dict:
  print("present")

#60 Split list into chunks
import numpy as np
list = [1,2,3,4,6,7,8]

print(np.array_split(list,4))

