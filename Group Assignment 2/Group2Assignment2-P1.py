'''
Group2Assignment2-P1.py
Addison Lewandowski (TODO: ADD GROUP NAMES HERE LATER)
Programming Strategies Part:1 
Started: 2026-10-26 | Finished: 2026-XX-XX

NOTE: Any comments with "#TEST" can be deleted if you want, 
but it helps with understanding what's going on so TODO: Delete #TEST when finished.
'''
# Variables and Constants
minimum_down_payment_check = False
minimum_down_payment = float()
client_down_payment = float()
mortgage_interest_rate = float()

# Inputs
client_name = str(input("Enter client's name: "))
client_address = str(input("Enter client's address: "))
client_purchase_price = float(input("Enter client's purchase price: "))

# Minimum Down Payment Check Loop
while minimum_down_payment_check == False:
    minimum_down_payment_check = True
    client_down_payment_percentage = float(input("Enter client's down payment (in %): ")) * 0.01
    client_down_payment = client_purchase_price * client_down_payment_percentage #Technically don't need to make this a varibale, but helps with readability. Sorta. Kinda.. Sorry...
    #Calculate minimum down payment
    if client_purchase_price <= 400000:
        minimum_down_payment = 0.05 * client_purchase_price
    elif (client_purchase_price > 400000) and (client_purchase_price <= 900000):
        minimum_down_payment = (0.05 * 400000) + (0.10 * (client_purchase_price - 400000))
    elif client_purchase_price > 900000:
        minimum_down_payment = 0.20 * client_purchase_price
    #Minimum down payment flag check
    if (client_down_payment) < (minimum_down_payment):
        minimum_down_payment_check = False
        print(f"${(client_down_payment):,.0f} is less than ${minimum_down_payment:,.0f}") #TEST PRINT
        print(f"Expecting minimum percentage: {(minimum_down_payment / client_purchase_price) * 100}%") #TEST PRINT
    
# Mortgage Default Insurance Component
premium_insurance_rate = 0.0
if client_down_payment_percentage >= 0.05 and client_down_payment_percentage < 0.10:
    premium_insurance_rate = 0.05
if client_down_payment_percentage >= 0.10 and client_down_payment_percentage < 0.15:
    premium_insurance_rate = 0.04
if client_down_payment_percentage >= 0.15 and client_down_payment_percentage < 0.20:
    premium_insurance_rate = 0.03
if client_down_payment_percentage >= 0.20:
    premium_insurance_rate = 0.0

# Calculations
insurance_cost = (client_purchase_price - client_down_payment) * premium_insurance_rate #TODO: NEEDS a better name.
principle_amount = client_purchase_price - client_down_payment + insurance_cost #TODO: NEEDS a better variable name.
print(f"Down payment amount: ${client_down_payment:,.0f}") #TEST PRINT
print(f"Insurance cost: ${insurance_cost:,.0f}") #TEST PRINT
print(f"Principle amount: ${principle_amount:,.0f}") #TEST PRINT

# Morgage Payment Component
mortgage_term = int(input("Enter Mortgage Term (years): "))
match(mortgage_term):
    case 1:
        mortgage_interest_rate = 0.059
    case 2:
        mortgage_interest_rate = 0.058
    case 3, 4:
        mortgage_interest_rate = 0.055
    case 5:
        mortgage_interest_rate = 0.053
    case 10:
        mortgage_interest_rate = 0.06