#!/usr/bin/env python

#Confirm Transactions for the Bitcoin Point of Sale
#@Author Thomas Tumiel
#@Version 0.1.1


from websocket import create_connection
import json

##########################################
###              FUNCTIONS             ###
##########################################

def confirmTx(randValue):
    if type(randValue)!=float:
        return null
    with open("current_xrate.txt","r") as f:
        xrate = float(f.read())
    f.close()
    btc_value = round(randValue/xrate,8)
    
