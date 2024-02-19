print("Hello, Welocome to our restaurant")
print("How much is your total purchase")
total_purchase = float(input(""))
print("Are you using Bank or Cash payment")
print("a." "Cash payment")
print("b." "Bank payment")
payment_type = str(input("")).lower()
if payment_type == "a" or payment_type == "Cash payment":
    print("Cash Payment")
    cash_payment = float(input("How much cash are you paying: "))
    tip = 0.3 * total_purchase
    print(f"We will charge 3% of your total purchase, which is tip ${tip}")
    total_cost = tip + total_purchase
    print("Are you making a Single payment or Joint")
    print("a." "Single payment")
    print("b." "Joint payment")
    payment_nature = str(input(""))
    if payment_nature == "a" or payment_nature == "Single payment":
        print(f"Your total payment is ${total_cost}")
        Balance = cash_payment - total_cost
        print(f" Your balance is ${Balance}")
    elif payment_nature == "b" or payment_nature == "Joint payment":
        print("How many of you are paying? ")
        num_of_ppl = int(input(""))
        each_pay = total_cost / num_of_ppl
        Balance = cash_payment - total_cost
        print(f"You are to pay ${each_pay} each")
        print(f" Your balance is ${Balance}")
    else:
        print("invalid payment request")

    Balance = cash_payment-total_cost
    if Balance == 0 :
        print("You dont have any Balance")
    elif  total_purchase > cash_payment :
        print("insurficient fund")
    else:
        print("invalid input!")

 # logic for Bank
    
elif payment_type == "b" or payment_type == "Bank Payment":
    print("Bank payment")
    Bank_name = str(input("Bank Name: "))
    Bank_payment = float(input("How much deposit are you making: "))
    tip = 0.3 * total_purchase
    print(f"We will charge 3% of your total purchase, which is tip ${tip}")
    total_cost = tip + total_purchase
    print("Are you making a Single payment or Joint")
    print("a." "Single payment")
    print("b." "Joint payment")
    payment_nature = str(input(""))
    if payment_nature == "a" or payment_nature == "Single payment":
        print(f"Your total payment is ${total_cost}")
        Balance = Bank_payment - total_cost
        print(f"Your balance is ${Balance}")
    elif payment_nature == "b" or payment_nature == "Joint payment":
        print("How many of you are paying? ")
        num_of_ppl = int(input(""))
        each_pay = total_cost / num_of_ppl
        Balance = Bank_payment - total_cost
        print(f"You are to pay ${each_pay} each")
        print(f"Your balance is ${Balance}")
    else:
        print("invalid payment request")
else:
    print("invalid input")
print("Thank you for your Patronage")
    



