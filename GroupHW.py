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
print('--------------------------------------- \n*** Welcome to Gas Station Program! ***\n---------------------------------------' )
print('Please Select the type of Purchase:\nG: Gas\nO: Oil')
product = input('Enter your Choice: ').lower()

#validate input
if product != 'g' and product != 'o':
   print('Invalid Input, you should enter g or o')
else:
   
   #if oil
   if product == 'o':
      product_name = 'Oil'
      oil_case = float(input('Enter Number of cases: '))
      
      #validate 
      if oil_case <= 0:
         print('Number of cases should be > 0')
         exit()
         
      #convert cases to liters
      liters = oil_case * OIL_CASE_SIZE

      price_before_discount = OIL_RATE * liters

      #calculate oil
      if oil_case > OIL_DISCOUNT_LIMIT:
         price_after_discount = price_before_discount - (price_before_discount * DISCOUNT_AMOUNT)
      else:
         price_after_discount = price_before_discount


   #if gas
   if product == 'g':
      product_name = 'Gas'
      liters = float(input('Enter the number of Liters: '))

      #validate liters
      if liters <=0:
         print('Number of liters should be > 0')
         exit()

      price_before_discount = GAS_RATE * liters

      #calculate gas
      if liters > GAS_DISCOUNT_LIMIT:
         price_after_discount = price_before_discount - (price_before_discount * DISCOUNT_AMOUNT)
      else:
         price_after_discount = price_before_discount


   province = input('Enter Province Abbreviation: ').lower()

   #check GST
   if province == 'ab' or province == 'bc':
      gst_rate = GST_AB_AND_BC / 100
   else:
      if province == 'on':
         gst_rate = GST_ON / 100
      else:
         gst_rate = GST_OTHER / 100

   #calculate
   gst = price_after_discount * gst_rate
   total = price_after_discount + gst

   #output
   print('----------------------------------------------------------------------------------------------------\n'
   f'Product\t # of Liters\t Price Before Discount\t Price After Discount\t   GST\t\tTotal Price\n'
   f'{product_name:^8}{liters:^12}{price_before_discount:^30.2f}{price_after_discount:^20.2f}{gst:^15.2f}{total:^20.2f}\n'
   '----------------------------------------------------------------------------------------------------\n'
   'Thanks for your business, Good Bye')