#1 Print Operation
print("Hello World")

#2 Adding Two Numbers
num1 = 4
num2 = 5
sum = num1 + num2
print(f"The sum of {num1} and {num2} is: {sum}")

#3 Finding Sq rt
a = 9
sqrt_a = a**0.5
print(f"The square root of {a} is: {sqrt_a}")

#4 Area of Triangle (1st Approach)

base = float(input("Enter: "))
height = float(input("Enter: "))
hypotenuse = float(input("Enter: "))

triangle_area1 = 0.5 * base * height

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

print(f"Result after swapping: {var1} & {var2}")

#7 Random Number

import random

print(random.randint(0, 100))

#8 Convert: km to miles

km = 5
conv_factor = 0.621371
miles = km * conv_factor
print(f"miles: {miles}")

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
  for i in range(2,num):
    if (num % i)==0:
      flag = True
      break
  if flag:
    print(f"{num} is not a prime number")
  else:
    print(f"{num} is a prime")

#15 Prime in Range Interval

lower = 300
upper = 400

print(f"Primes between {lower} & {upper} are: ")

for numb in range(lower,upper):
  if numb>=lower:
    for value in range(2,numb):
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
  for id in range(1,fact_num+1):
    factorial = factorial * id
  print(f"{factorial} is the factorial")

#17 Multiplication Table

m = int(input("Enter your number: "))

for n in range(1,11):
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