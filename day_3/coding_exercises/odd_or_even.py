# Exercise 8 - Odd or Even? Introducing the Modulo

number = int(input())

remainder = number % 2

if remainder >= 1:
  print("This is an odd number.")
else:
  print("This is an even number.")

# Streamlined Solution

number = int(input())

if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")