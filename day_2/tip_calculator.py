# Project 2 - Tip Calculator
print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people are you splitting the bill with? "))

bill_with_tip = ((tip / 100) * bill + bill) / people
bill_per_person = round(bill_with_tip, 2)
bill_per_person = "{:.2f}".format(bill_per_person)

print(f"Each person should pay: ${bill_per_person}")