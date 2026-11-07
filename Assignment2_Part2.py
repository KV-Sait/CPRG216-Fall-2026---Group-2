'''
File Name: Assignment2-Part2.py

Group Members:
Addison Lewandowski
Russell Belmonte
Jordan La
Kenny Vo

Assignment: Programming Strategies
Part 2: The Amortization Schedule

Started: 2026-10-26 | Finished: 2026-XX-XX
'''

# Minimum Down Payment Component

# Variables and Constants
MORTGAGE_TERM_ALLOWED = (1, 2, 3, 5, 10)
MORTAGE_AMORTIZATION_ALLOWED = (5, 10, 15, 20, 25)

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
if min_down_payment_percent == 5 or min_down_payment_percent == 20:
    down_payment_percent = float(input(f"Enter down payment percentage (minimum {int(min_down_payment_percent)}): "))
else:
    down_payment_percent = float(input(f"Enter down payment percentage (minimum {min_down_payment_percent:.3f}): "))
while down_payment_percent < min_down_payment_percent or down_payment_percent > 100:
    print(f"Please enter a value between the minimum and 100")
    if min_down_payment_percent == 5 or min_down_payment_percent == 20:
        down_payment_percent = float(input(f"Enter down payment percentage (minimum {int(min_down_payment_percent)}): "))
    else:
        down_payment_percent = float(input(f"Enter down payment percentage (minimum {min_down_payment_percent:.3f}): "))

# Mortgage Default Insurance Component

# Required Mortgage Default Insurance
if 5 <= down_payment_percent < 10:
    mortgage_insurance_premium = 5
elif 10 <= down_payment_percent < 15:
    mortgage_insurance_premium = 4
elif 15 <= down_payment_percent < 20:
    mortgage_insurance_premium = 3
else:
    mortgage_insurance_premium = 0

# Recalculate
down_payment = purchase_price * down_payment_percent / 100
insurance_cost = (purchase_price - down_payment) * mortgage_insurance_premium / 100
principal_amount = purchase_price - down_payment + insurance_cost

# Print Calculations
print(f"Down payment amount is ${int(down_payment)}")
print(f"Mortgage insurance price is ${int(insurance_cost)}")
print(f"Total mortgage amount is ${int(principal_amount)}")

# Morgage Payment Component

# Input mortgage term

mortgage_term = int(input("Enter Mortgage Term (1, 2, 3, 5, 10): "))
while mortgage_term not in MORTGAGE_TERM_ALLOWED:
    print("Please enter a valid choice")
    mortgage_term = int(input("Enter Mortgage Term (1, 2, 3, 5, 10): "))

# Input mortgage amortization period

mortgage_amortization_period = int(input("Enter mortgage amortization period (5, 10, 15, 20, 25): "))
while mortgage_amortization_period not in MORTAGE_AMORTIZATION_ALLOWED:
    print("Please enter a valid choice")
    mortgage_amortization_period = int(input("Enter mortgage amortization period (5, 10, 15, 20, 25): "))

# Mortgage Interest Rate
match(mortgage_term):
    case 1:
        mortgage_interest_rate = 5.90
    case 2:
        mortgage_interest_rate = 5.80
    case 3:
        mortgage_interest_rate = 5.50
    case 5:
        mortgage_interest_rate = 5.30
    case 10:
        mortgage_interest_rate = 6.00

# Print Mortgage Interest Rate
print(f"Interest rate for the term will be {mortgage_interest_rate:.2f}%")

# Morgage Payment Amount
num_monthly_payments = mortgage_amortization_period * 12
effective_monthly_rate = ((1 + (mortgage_interest_rate/2 * 0.01)) ** 2) ** (1/12) - 1
monthly_payment = principal_amount * ((effective_monthly_rate * ((1 + effective_monthly_rate) ** num_monthly_payments)) / (((1 + effective_monthly_rate) ** num_monthly_payments) - 1))

# Print Mortgage Payment Amount

print(f"Monthly payment amount is: ${monthly_payment:.2f}")

#Part 2

# Amortization schedule
schedule = input('Would you like to see the amortization schedule? (Y/N): ')
if schedule.upper() == 'y' or schedule.upper() == 'Y':
    print(f'{"Monthly Amortization Schedule":^95}\n')
    print(f'{"Month":>10}{"Opening Bal":>18}{"Payment":>15}{"Principal":>15}{"Interest":>15}{"Closing Bal":>18}')

    amortization_schedule = []

    # Calculate Amortization Schedule
    for month in range (1, mortgage_term * 12 + 1):

        # Get balance
        opening_balance = principal_amount
        
        # Calculate Monthly Interest
        monthly_interest = opening_balance * effective_monthly_rate

        # Calculate Monthly Principal
        monthly_principal = monthly_payment - monthly_interest

        # Calculate Closing Balance
        closing_balance = opening_balance - monthly_principal

        # Amortization Schedule Dictionary
        monthly_amortization = {
            "Month": month,
            "Opening Bal": opening_balance,
            "Payment": monthly_payment,
            "Principal": monthly_principal,
            "Interest": monthly_interest,
            "Closing Bal": closing_balance
        }
        # Get Balance for Next Month
        balance = closing_balance

        amortization_schedule.append(monthly_amortization)
    
    # Print Amortization Schedule
    for data in amortization_schedule:
        print(f'{data["Month"]:>10}{data["Opening Bal"]:>18.2f}{data["Payment"]:>15.2f}{data["Principal"]:>15.2f}{data["Interest"]:>15.2f}{data["Closing Bal"]:>18.2f}')

    total_principal =sum(data["Principal"] for data in amortization_schedule)
    total_interest = sum(data["Interest"] for data in amortization_schedule)
    print("=" * 91)
    print(f"{'Total':<43}{total_principal:>15.2f}{total_interest:>15.2f}")



'''

Part 2 Task List:
Monthly Interest = Opening Balance at the start of the month * EMR (see above)
Monthly Principle Amount = Monthly Payment (see above) - Monthly interest amount
Closing Balance = Opening Balance - Monthly Principle

Other Requirements:
Validate three user inputs:
- Down Payment must be between the minimum on Table 1 and 100
- Mortgage Term must be values allowed on Table 3
- Amortization period must be one of the values on Table 4
  - Re-prompt them to try again
- Does not need validation of input's data type
When calculating the in-between down payment (Table 1 thing), round the percentage to 3 decimal places.

Formatting Requirements (Says tips on the doc, but they should be done):
- Good variables
- Use f-strings (variables, whitespace, columns, limiting characters) ----Part 2: Amortization Schedule
- Use Constants (TODO: Not done, guaranteed) --- lines 67-73
- Use compound data types   ---- line 138-150

'''