print("Welcome to tip calculator")
bill = float(input("What was your total bill?"))
tip = float(input("What percentage tip would you like to give?"))
people = int(input("How many people to split the bill?"))
calculated_bill = bill * (tip / 100)
final_bill = round(calculated_bill / people, 2)
print(f"Each person should pay {final_bill}")
