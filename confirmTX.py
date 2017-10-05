#!/usr/bin/env python

#Confirm Transactions for the Bitcoin Point of Sale
#@Author Thomas Tumiel
#@Version 0.1.1


from websocket import create_connection
import json

##########################################
###              FUNCTIONS             ###
##########################################

def confirmTx(randValue,btc_addr):
    #get the exchange rate from the data file and
    #convert the @param randValue to a btc_value
    if type(randValue)!=float:
        return null
    with open("current_xrate.txt","r") as f:
        xrate = float(f.read())
    f.close()
    btc_value = round(randValue/xrate,8)

    result = monitorSocket(btc_addr)

    tx_fee = TxFeeCheck(result)
    if tx_fee > 5e4: #Minimum transaction fee = 50 000 Satoshi
        return True #Success! Payment Confirmed
    else:
        return False #Transaction fee too low


#Monitors the blockchain.info websocket for incoming Txs
#at @param btc_addr.

def monitorSocket(btc_addr, satValue):
    while True:
        result = getSocketData(btc_addr)
        if result != null:
            if containsOutput(result["out"],btc_addr,satValue):
                return result



#Continually retrieves the websocket data
#@returns dictionary that represents a bitcoin transaction
def getSocketData(btc_addr):
    ws = create_connection("wss://ws.blockchain.info/inv")
    ws.send(json.dumps({"op":"addr_sub", "addr":btc_addr}))
    result =  ws.recv()
    ws.close()
    return json.loads(result)["x"]



#Checks whether a transaction contains an output
#that corresponds to the purchase made
#@param outputs array of outputs of a given transaction
#@param btc_addr the bitcoin address of the owner
#@param satValue the satoshi value of the purchase
#@returns boolean
def containsOutput(outputs,btc_addr,satValue):
    for out in outputs:
        if satValue-1<=out["value"]<=satValue+1 and out["addr"]==btc_addr:
            return True
    return False



#Confirm that there is a tx fee greater than a threshold
def TxFeeCheck(resultTx):
    #Sum the inputs
    total_in = 0
    for inpt in resultTx["inputs"]:
        total_in += inpt["prev_out"]["value"]

    #Sum the Outputs
    total_out = 0
    for outpt in resultTx["out"]:
        total_out += outpt["value"]

    #Check leftover amount i.e. Tx fee
    return total_in - total_out #> 5e4: #Minimum transaction fee = 50 000 Satoshi
    #     return True #Success! Payment Confirmed
    # else:
    #     return False #Transaction fee too low
