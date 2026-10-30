'''
File Name: Assignment2-Part1.py

Group Members:
Addison Lewandowski
Russell Belmonte
Jordan La
Kenny Vo

Assignment: Programming Strategies
Part 1: Monthly Payment Calculator

Started: 2026-10-26 | Finished: 2026-XX-XX

NOTE: Any comments with "#TEST" can be deleted if you want, 
but it helps with understanding what's going on so TODO: Delete or cleanup #TEST when finished.

Test inputs:
a
a
800000
10
15
3
'''

# Minimum Down Payment Component

# Variables and Constants
client_down_payment = float()
mortgage_interest_rate = float()

# Initial User Inputs
client_name = str(input("Enter client name: "))
address = str(input("Enter address of property: "))
purchase_price = float(input("Enter purchase price: "))

# Calculate minimum down payment
if purchase_price <= 400000:
    min_down_payment = 0.05 * purchase_price # Minimum Down Payment = 5%
elif (400000 < purchase_price <= 900000):
    min_down_payment = 20000 + (0.10 * (purchase_price - 400000)) # Minimum Down Payment = 5% of $400 000 (= $20 000) + 10% of the Remainder
elif purchase_price > 900000:
    min_down_payment = 0.20 * purchase_price # Minimum Down Payment = 20%

# Calculate minimum down payment percentage
min_down_payment_percent = float(min_down_payment / purchase_price) * 100

# Input for down payment percentage
down_payment_percentage = float(input(f"Enter down payment percentage (minimum {min_down_payment_percent}): ")) * 0.01
while down_payment_percentage < min_down_payment_percent:
    down_payment_percentage = float(input(f"Enter down payment percentage (minimum {min_down_payment_percent}): ")) * 0.01 

# Mortgage Default Insurance Component

premium_insurance_rate = 0.0
if down_payment_percentage >= 0.05 and down_payment_percentage < 0.10:
    premium_insurance_rate = 0.05
if down_payment_percentage >= 0.10 and down_payment_percentage < 0.15:
    premium_insurance_rate = 0.04
if down_payment_percentage >= 0.15 and down_payment_percentage < 0.20:
    premium_insurance_rate = 0.03
if down_payment_percentage >= 0.20:
    premium_insurance_rate = 0.0

# Calculations
client_down_payment = purchase_price * down_payment_percentage
insurance_cost = (purchase_price - client_down_payment) * premium_insurance_rate #TODO: NEEDS a better name.
principle_amount = purchase_price - client_down_payment + insurance_cost #TODO: NEEDS a better variable name.
print(f"Down payment amount: ${client_down_payment:,.0f}") #TEST PRINT TODO: Make a bit cleaner of a print or delete?
print(f"Insurance cost: ${insurance_cost:,.0f}") #TEST PRINT TODO: Make a bit cleaner of a print or delete?
print(f"Principle amount: ${principle_amount:,.0f}") #TEST PRINT TODO: Make a bit cleaner of a print or delete?

# Morgage Payment Component
mortgage_term = int(input("Enter Mortgage Term (years): "))
mortgage_amortization_period = int(input("Enter mortgage amortization period (every 5 years): ")) #TODO: Make this better pls, ik this is ass lmao.
mortgage_amortization_years = mortgage_amortization_period * 5 #TODO: Delete this I hate this... I hope my suffering is funny to you tho, sorry I'm not actually going into detail and making you waste time by reading this exact sentence.
mortgage_amortization_months = mortgage_amortization_years * 12

match(mortgage_term):
    case 1:
        mortgage_interest_rate = 0.059
    case 2:
        mortgage_interest_rate = 0.058
    case 3 | 4:
        mortgage_interest_rate = 0.055
    case 5 | 6 | 7 | 8 | 9:
        mortgage_interest_rate = 0.053
    case 10:
        mortgage_interest_rate = 0.06

# Morgage Payment Calculations
print(mortgage_interest_rate)
monthly_rate = ((1 + (mortgage_interest_rate/2)) ** 2) ** (1/12) - 1
monthly_payment = principle_amount*(monthly_rate*(1 + monthly_rate)**(mortgage_amortization_months))/((1 + monthly_rate)**(mortgage_amortization_months) - 1)

print(f"Monthly Rate: {monthly_rate}") #TEST PRINT. Not needed tbh. TODO: Delete.
print(f"Monthly Payment: ${monthly_payment:,.2f}") #TEST PRINT. TODO: Clean up.