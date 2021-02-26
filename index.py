import APSJ20G2_SALES_DATA_ANALYSIS.auth_user as au
import APSJ20G2_SALES_DATA_ANALYSIS.otp as otp
import APSJ20G2_SALES_DATA_ANALYSIS.reg_user as ru

def menu():
   import APSJ20G2_SALES_DATA_ANALYSIS.functions as functions
   while True:
      print("Enter 1 to print the total sales")
      print("Enter 2 to print the total number of items sold all throughout")
      print("Enter 3 to print the average sales")
      print("Enter 4 to print the TOP 5 SALES BY PRICE")
      print("Enter 5 to print the 5 MOST SELLING PRODUCTS")
      print("Enter 6 to print the total revenue item wise")
      print("Enter 7 to print the total revenue category wise")
      print("Enter 8 to print the total revenue per customer")
      print("Enter 9 to print the MOST VALUABLE CUSTOMER")
      print("Enter 10 to analyse top 5 sales by price graphically ")
      print("Enter 11 to analyse top 5 most selling products graphically ")
      print("Enter 12 to graphically represent revenue per customer")
      print("Enter 13 to graphically represent revenue per category")
      inp = int(input())
      print("#" * 50)
      if inp == 1:
         functions.totalsale()
      elif inp == 2:
         functions.itemsold()
      elif inp == 3:
         functions.avgsale()
      elif inp == 4:
         functions.topfivesalesbyprice()
      elif inp == 5:
         functions.mostsellingproducts()
      elif inp == 6:
         functions.revenueperitem()
      elif inp == 7:
         functions.revenuepercat()
      elif inp == 8:
         functions.revenuepercustomer()
      elif inp==9:
         functions.mostvaluablecustomer()
      elif inp == 10:
         functions.tfs_graph()
      elif inp == 11:
         functions.tfms_graph()
      elif inp == 11:
         functions.rpcu()
      else:
         functions.rpca()
      print('#' * 50)
      print("To continue printing results press 0")
      inpu = int(input())
      if inpu != 0:
         break
   print("#" * 50)
   print('THANKYOU!')
   print('#' * 50)

def dashboard():
   print("Welcome to sales Analysis")
   print("#" * 50)
   print("Enter 1 to Login for an already registered user or 2 to register for new users")
   print("#" * 50)
   start_input = int(input())
   if start_input == 1:
      print("Enter Your Email")
      email = input()
      auth_count = au.auth_user(email)
      if auth_count == 1:
         otp_count=otp.otpgeneration(email)
         if otp_count==1:
            print("LOGIN SUCCESSFUL")
            menu()
         if otp_count==0:
            print("ERROR")
            dashboard()
      else:
         print("ERROR INVALID MAIL ID")
         dashboard()
   elif start_input==2:
      ru.reg_user()
      dashboard()

dashboard()