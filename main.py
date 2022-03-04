print("Welcome to the Tip Calculator")
total_bill_amount = float(input("What was the total Bill? $"))
no_of_people = float(input("How many people to split the bill? "))
percent_tip = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
amount_with_tip = total_bill_amount + (total_bill_amount * percent_tip / 100)
amount_per_person = amount_with_tip / no_of_people
print(f"Each person should pay: ${amount_per_person}")
