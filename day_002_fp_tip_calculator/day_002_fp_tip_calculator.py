# TIP CALCULATOR

print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

amount_per_person = total_bill * ((percentage * 0.01) + 1) / people
amount_per_person = "{:.2f}".format(amount_per_person)

print(f"Each person should pay: ${amount_per_person}")
