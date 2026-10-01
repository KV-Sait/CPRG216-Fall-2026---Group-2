'''

File Name: Assignment1.py
Authors:
   Russell Belmonte
   Jordan La
   Addison Lewandowski
   Kenny Vo

Program Description:
Assignment: Programming Basics
Oil/Gas Station Scenario

'''

#constant
OIL_RATE = 1.25
OIL_CASE_SIZE =12
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
      oil_case = float(input('Enter # of cases of Oil: '))
      
      #validate 
      if oil_case <= 0:
         print('Number of oil cases should be > 0')
         exit()
         
      #convert cases to litres
      litres = oil_case * OIL_CASE_SIZE

      price_before_discount = OIL_RATE * litres

      #calculate oil
      if oil_case > OIL_DISCOUNT_LIMIT:
         price_after_discount = price_before_discount - (price_before_discount * DISCOUNT_AMOUNT)
      else:
         price_after_discount = price_before_discount


   #if gas
   if product == 'g':
      product_name = 'Gas'
      litres = int(input('Enter the number of litres of gas: '))

      #validate litres
      if litres <= 0:
         print('Number of litres should be > 0')
         exit()

      price_before_discount = GAS_RATE * litres

      #calculate gas
      if litres > GAS_DISCOUNT_LIMIT:
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
         f'{product_name:^8}{litres:^12}{price_before_discount:^30.1f}{price_after_discount:^20.1f}{gst:^15.2f}{total:^20.2f}\n'
         '----------------------------------------------------------------------------------------------------\n'
         'Thanks for your business, Good Bye')