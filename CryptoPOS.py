#!/usr/bin/env python

#Crypto POS
#@Author Thomas Tumiel
#@Version 0.1.1

#Import dependencies for the project
from requests import get #<3
import ast



##########################################
###              FUNCTIONS             ###
##########################################

def getBTCAddress(name):
    if type(name)!=str:
        return null
    else:
        return addrs_dict[name]



##########################################
###               PROGRAM              ###
##########################################

#Data dictionary that will contain the customers bitcoin address
#And an updated bitcoin price
# data = {}

#Get the bitcoin addresses from a database (currently just using a text file)
with open("btc_addrs.txt","r") as BTC_Addrs:
    addrs_dict = ast.literal_eval(BTC_Addrs.read())

BTC_Addrs.close()

#Get customer's address
my_name = "Tom"
my_btc_addr = getBTCAddress(my_name)


#Get Luno price of Bitcoin in ZAR(South African Rand)
luno_xrate = get("https://api.mybitx.com/api/1/ticker?pair=XBTZAR").json()['ask']

# #Add address to data          #### Not Necessary
# data["address"] = my_btc_addr;
#Add current price to data
# data["price"] = luno_xrate;

#datafile = "data"+my_name+".txt"

#Write current luno price to data file periodically using cron
with open("current_xrate.txt","w") as f:
    f.write(str(luno_xrate));
f.close();
