name = str(input("Name: "))
print(f"Good morning {name}, We hope you enjoyed your meal?")
print("a." "Yes")
print("b." "No")
response = str(input(""))
if response == "a" or response == "Yes":
    print("we are glad you did")
else:
    print("We are sorry! ")
meal_cost = float(input("How much is your meal:$ "))
tip = 0.3 * meal_cost
print(f"Our company charges 3 percent of your total purchase, which is ${tip}")
total_cost = meal_cost + tip
print("Are you making a single or joint payment?")
print("a." "Single payment")
print("b." "Joint payment")
payment_type = str(input(""))
if payment_type == "a" or payment_type == "Single payment":
    print(f" You are to pay ${total_cost}")
elif payment_type == "b" or payment_type == "Joint payment":
    num_pay = float(input("How many of you are Paying: "))
    print(f"Your total payment is ${total_cost}")
    each_pay = total_cost/num_pay
    print(f"You are to pay ${each_pay} each")
else:
    print("invalid input!")
print(f"Thank you for your patronage {name}, see you next time")
