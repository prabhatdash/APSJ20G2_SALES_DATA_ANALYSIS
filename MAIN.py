

print("Welcome to sales Analysis")
import mysqlconnector
mysqlconnector.login()
import functions
while True:
	print("Enter 1 to print the total sales")
	print("Enter 2 to print the total number of items sold all throughout")
	print("Enter 3 to print the average sales")
	print("Enter 4 to print the TOP 5 SALES BY PRICE")
	print("Enter 5 to print the 5 MOST SELLING PRODUCTS")
	print("Enter 6 to print the total revenue itemwise")
	print("Enter 7 to print the total revenue category wise")
	print("Enter 8 to print the total revenue per customer")
	print("Enter 9 to print the MOST VALUABLE CUSTOMER")
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
	else:
		functions.mostvalueablecustomer()
	print('#' * 50)
	print("To continue printing results press 0")
	inpu=int(input())
	if inpu!=0:
		break
print("#"*50)
print('THANKYOU!')
print('#'*50)