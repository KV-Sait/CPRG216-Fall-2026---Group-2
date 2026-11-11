'''

File Name: Assignment2-Part2.py 
Started: 2026-10-26 | Finished: 2026-11-11

Group Members: 
    Addison Lewandowski 
    Russell Belmonte 
    Jordan La 
    Kenny Vo

Assignment: Programming Strategies 
Part 2: The Amortization Schedule

Program Description: The purpose of this program is to calculate monthly
mortgage payments and produce an amortization schedule for selected mortgage
terms. The program description will be split into two parts for better
readability.

Part 1: When running the program it asks for the clients name, their address and
the purchase price of the property as inputs. It calculates the minimum down
payment price by applying a percentage to the purchase price values depending on
the range that the purchase price value falls into. Following this the program
will calculate the minimum down payment percentage using the minimum down
payment and the purchase price. It then asks the user to input a down payment
percentage. The program will continue to ask the user for a valid down payment
percentage if they input a value less than the minimum down payment percentage
or a value greater than 100 percent. A message will also be displayed to the
user to reflect an invalid input. After receiving a valid down payment
percentage the program will calculate the mortgage insurance premium based where
the inputted down payment percent falls in a given set of ranges. Furthermore,
the program will calculate values for down payment, insurance cost and principal
amount displaying them as rounded values. The program will then ask for a valid
mortgage term where the input value has to be a value part of the tuple called
allowed mortgage values. Otherwise it will display the message please enter a
valid choice and continue to ask the user for a valid input. Next the program
will get the mortgage amortization period input using the same logic as used in
getting the mortgage term input. Then the program will use a match statement
using the mortgage term to determine the mortgage interest rate displaying the
value to 2 decimal places. The program will then calculate the number of monthly
payments and effective monthly rate (EMR) to find the monthly payment amount.
One thing to note is that in the EMR calculation the program multiples mortgage
interest rate divided by 2 by a factor of 0.01. This is to convert the interest
rate from a percentage to a decimal value for calculation purposes. The program
will then display the monthly payment amount to 2 decimal places. 

Part 2: For the second part the program will ask the user if they want to see
the amortization schedule. If the user inputs y or Y then the program will
calculate the amortization schedule for the inputted number of mortgage terms.
To do so it will calculate values for opening balance, monthly interest, monthly
principal and closing balance, storing them as key value pairs into a dictionary
called monthly amortization. This dictionary is then added to a list called
amortization schedule. It will do this for each month up to the inputted
mortgage term in months. After all the processing it will then iterate through
the amortization schedule list accessing each dictionary and their respective
keys and values to display the amortization schedule data in a table format. At
the bottom of the table it will also display totals for the principal and
interest. In the event that the user inputs n or N the program will stop and not
display the amortization schedule.

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
print(f"Down payment amount is ${down_payment:.0f}")
print(f"Mortgage insurance price is ${insurance_cost:.0f}")
print(f"Total mortgage amount is ${principal_amount:.0f}")

# Morgage Payment Component

# Input mortgage term

mortgage_term = int(input("Enter mortgage term (1, 2, 3, 5, 10): "))
while mortgage_term not in MORTGAGE_TERM_ALLOWED:
    print("Please enter a valid choice")
    mortgage_term = int(input("Enter mortgage term (1, 2, 3, 5, 10): "))

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

# Mortgage Payment Amount
num_monthly_payments = mortgage_amortization_period * 12
effective_monthly_rate = ((1 + (mortgage_interest_rate/2 * 0.01)) ** 2) ** (1/12) - 1 # Multiplication by 0.01 to convert percentage to decimal value
monthly_payment = principal_amount * ((effective_monthly_rate * ((1 + effective_monthly_rate) ** num_monthly_payments)) / (((1 + effective_monthly_rate) ** num_monthly_payments) - 1))

# Print Mortgage Payment Amount

print(f"Monthly payment amount is: ${monthly_payment:.2f}")

# Part 2

# Amortization schedule
schedule = input('Would you like to see the amortization schedule? (Y/N): ')
if schedule.upper() == 'Y':
    print(f'{"Monthly Amortization Schedule":^84}\n')
    print(f'{"Month"}{"Opening Bal":>16}{"Payment":>16}{"Principal":>16}{"Interest":>16}{"Closing Bal":>16}')

    amortization_schedule = []
    balance = principal_amount

    # Calculate Amortization Schedule
    for month in range (1, mortgage_term * 12 + 1):

        # Get balance
        opening_balance = balance
        
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
        print(f'{data["Month"]:>5}{data["Opening Bal"]:>16.2f}{data["Payment"]:>16.2f}{data["Principal"]:>16.2f}{data["Interest"]:>16.2f}{data["Closing Bal"]:>16.2f}')

    total_principal =sum(data["Principal"] for data in amortization_schedule)
    total_interest = sum(data["Interest"] for data in amortization_schedule)
    print("=====================================================================================")
    print(f"{'Total':<37}{total_principal:>16.2f}{total_interest:>16.2f}")
