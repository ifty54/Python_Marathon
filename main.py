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

triangle_area1 = (1/2) * base * height

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

#19 Armstrong Number

your_num = int(input("Enter: "))

pow = len(str(your_num))
sum1 = 0

temp1 = your_num
while temp1 > 0:
  digit = temp1 % 10
  sum1 += digit ** pow
  temp1 //= 10

if your_num == sum1:
  print("This is Armstrong")
else:
  print("It's not Armstrong")

#20 Armstrong in Interval

low_limit = 200
up_limit = 1000

for your_num2 in range(low_limit, up_limit+1):
  order = len(str(your_num2))
  sum2 = 0
  temp2 = your_num2
  while temp2 > 0:
    digit2 = temp2 % 10
    sum2 += digit2 ** order
    temp2 //= 10
  if your_num2 == sum2:
    print(sum2)

#21 Natural Num Sum

total = int(input("enter number: "))

if total < 0:
  print("Enter a positive number")

else:
  total_sum = 0
  while(total > 0):
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
for no_i in range(1, smaller+1):
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
  if((greater % lcm1 == 0) and (greater % lcm2 == 0)):
    lcm = greater
    break 
  greater = greater + 1

print(f"LCM is {lcm}")

#28 Factors of A Number

num0 = int(input("Number: "))
factors = []

for i0 in range(1, num0 + 1):
  if(num0%i0==0):
    factors.append(i0)
print(f"the factors of {num0} are: {factors}")

#29 Calculator

print("Select Operation")
print("1 for add, 2 for sub, 3 for mul, 4 for div")
choice = input("Enter Choice(1,2,3,4): ")

if choice in ("1","2","3","4"):
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
  
