#Day 2
print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill?" + " " +"$"))

total_tip = int(input("How much tip would you like to give? 10, 12, or 15? "))\

total_people = int(input("How many people to split the bill?"))

bill_after_tax = total_bill + (total_bill * (total_tip/100))

bill_split = round((bill_after_tax / total_people), 2)

print(f"Each person should pay: ${bill_split}")


