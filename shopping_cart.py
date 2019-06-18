# shopping_cart.py

from pprint import pprint
import datetime
import gspread
import pandas as pd
import numpy as np

from oauth2client.service_account import ServiceAccountCredentials

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('my_cred.json', scope)
client = gspread.authorize(creds)

# Find a shopping cart worksheet by name and open the first sheet
sheet = client.open("Shopping Cart Project - Products Database").sheet1

#extract data as list and convert to dataframe
df = pd.DataFrame(sheet.get_all_values(), columns=['id','name','aisle','department','price'])

breakpoint()

#convert price from object to string
df["price"]= df["price"].astype(float)

#define variables
product_ids = []
total_price = 0
user_input = '' #string
now = datetime.datetime.now()
tax_usd = 0

#define functions
def to_usd(price):
    price_usd = "${:,.2f}".format(price)
    return price_usd

#Capture Inputs

while user_input is not "DONE":
    #ask user for product
    user_input = input("Please input a product identifier:")

    #validate input and handle errors
    if df['id'].isin([user_input]).any():
        product_ids.append(user_input) 
    elif user_input == "DONE":
        break
    elif user_input == "LIST":
        print(list(df['id']))
    else:   
        print(user_input + " is an invalid product code. Please input valid product code. When complete, type DONE. For list of product codes type LIST")

#print inputs 
print(product_ids)

print("---------------------------------")
print("THE NEW STORE")
print("51 WEST 4TH STREET")
print("NEW YORK, NY 10003")
print("212-555-5555")
print("WWW.THENEWSTORE.COM")
print("---------------------------------")
print("CHECKOUT AT: " + str(now.strftime("%Y-%m-%d %H:%M %p")))
print("---------------------------------")
print("SELECTED PRODCUTS:")

#print selected products
for i in product_ids:
    #matching_product = [p for p in products if str(p["id"]) == str(i)]
    matching_product = str(df.loc[df['id'] == str(i)]['name'].values)
        matching_product = matching_product.strip("['']")
    price = float(df.loc[df['id'] == str(i)]['price'])
    price_usd = to_usd(price)  #convert price to USD
    total_price = total_price + price
    print("... " + matching_product + " (" + str(price_usd) + ")")
 
#define tax and sub total
tax_usd = total_price * 0.0875
sub_usd = total_price + tax_usd
tax_usd = to_usd(tax_usd)
sub_usd = to_usd(sub_usd)
total_price = to_usd(total_price)

#print subtotals

print("---------------------------------")
print("SUBTOTAL: " + str(total_price))
print("TAX: " + str(tax_usd))
print("TOTAL: " + str(sub_usd))
print("---------------------------------")
print("THANKS, SEE YOU AGAIN SOON")
print("---------------------------------")