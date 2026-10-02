'''

File Name: Assignment1.py
Date: October 1st, 2026
Authors:
   Russell Belmonte
   Jordan La
   Addison Lewandowski
   Kenny Vo

Program Description: 
This is a gas station program that calculates the cost of oil or gas
 purchases. First it prompts the user to select the type of purchase. 
They can either type 'o/O' for oil or 'g/G' for gas. If the user inputs
 anything other than what is listed it displays ‘Invalid input.’ If the
 user inputs ‘o/O’ the program will ask them to enter the number of 
 cases of oil they’d like to purchase. Likewise if the user inputs 
 ‘g/G’ it will ask them to input the number of litres of gas. If the 
 user inputs a number that is 0 or fewer for the number of litres of 
 gas or cases of oil then the program tells the user that the value 
 inputted should be greater than 0 and exits. It then asks the user to
 enter 2 letters representing the abbreviation of province so that the
 program knows which GST rate to apply. The program then displays the
 relevant purchase information. Such as the product type either gas or
 oil, the number of liters of gas or cases of oil, the price before the
 discount, the price after the discount, GST, and the total price. 

Assignment: Programming Basics
Oil/Gas Station Scenario

'''

#constants
OIL_RATE = 1.25
OIL_CASE_SIZE = 12
OIL_DISCOUNT_LIMIT = 6
GAS_RATE = 1.05
GAS_DISCOUNT_LIMIT = 2000
DISCOUNT_AMOUNT = 0.10
GST_AB_AND_BC = 5
GST_ON = 13
GST_OTHER = 15

#display
print('---------------------------------------------\n'
      '*** Welcome to Gas Station Program! ***\n'
      '---------------------------------------------' )
print('Please Select the type of Purchase:\n'
      'G: Gas\n'
      'O: Oil')
product = input('>>> ').lower()

#validate input
if product != 'g' and product != 'o':
   print('Invalid input, you should enter g/G or o/O')
else:
   
   #if oil
   if product == 'o':
      product_name = 'Oil'
      number_of_oil_cases = float(input('Enter # of cases of Oil: '))
      
      #validate 
      if number_of_oil_cases <= 0:
         print('Number of oil cases should be > 0')
         exit()
         
      #convert cases to litres
      number_of_litres = int(number_of_oil_cases * OIL_CASE_SIZE)

      price_before_discount = OIL_RATE * number_of_litres

      #calculate oil
      if number_of_oil_cases > OIL_DISCOUNT_LIMIT:
         price_after_discount = price_before_discount - (price_before_discount * DISCOUNT_AMOUNT)
      else:
         price_after_discount = price_before_discount


   #if gas
   if product == 'g':
      product_name = 'Gas'
      number_of_litres = int(input('Enter the number of litres of gas: '))

      #validate litres
      if number_of_litres <= 0:
         print('Number of litres should be > 0')
         exit()

      price_before_discount = GAS_RATE * number_of_litres

      #calculate gas
      if number_of_litres > GAS_DISCOUNT_LIMIT:
         price_after_discount = price_before_discount - (price_before_discount * DISCOUNT_AMOUNT)
      else:
         price_after_discount = price_before_discount


   province = input('Please enter the 2 letters province abbreviation: ').lower()

   #check GST
   match province:
      case 'ab' |'bc':
         gst_rate = GST_AB_AND_BC / 100
      case 'on':
         gst_rate = GST_ON / 100
      case _:
         gst_rate = GST_OTHER / 100

   #calculate
   gst = price_after_discount * gst_rate
   total = price_after_discount + gst

   #output
   print('----------------------------------------------------------------------------------------------------\n'
         f'Product\t # of Liters\t Price Before Discount\t Price After Discount\t   GST\t\tTotal Price\n'
         f'{product_name:^8}{number_of_litres:^12}{price_before_discount:^30.1f}{price_after_discount:^20.1f}{gst:^15.2f}{total:^20.2f}\n'
         '----------------------------------------------------------------------------------------------------\n'
         'Thanks for your business, Good Bye')