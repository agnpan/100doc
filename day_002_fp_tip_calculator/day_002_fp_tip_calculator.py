# TIP CALCULATOR

print("Welcome to the tip calculator.")

# 1. We ask the user about the total bill.
total_bill = float(input("What was the total bill? $"))

# 2. We ask the user about the percentage.
percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))

# 3. We ask how many people would split the bill.
people = int(input("How many people to split the bill? "))

# 4. We calculate the final amount per person.
amount_per_person = total_bill * ((percentage * 0.01) + 1) / people
# We use {:.2f} to round up to two decimal points no matter what.
amount_per_person = "{:.2f}".format(amount_per_person)

# 5. We put all the data in a string.
print(f"Each person should pay: ${amount_per_person}")
