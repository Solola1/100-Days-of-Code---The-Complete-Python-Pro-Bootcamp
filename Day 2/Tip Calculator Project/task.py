print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? \n$"))
tip = int(input("What percentage tip would you like to give? 10 12 15 \n"))
people = int(input("How many people to split the bill? \n"))
bill_with_tip = tip / 100 * bill + bill
bill_division = bill / people
total_amount = (round(bill_division, 1))
print(f"Each person should pay: {total_amount}")

