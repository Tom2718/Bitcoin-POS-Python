import confirmTx
import pytest
import json

#Load the testing data to be used in the tests
with open("dataMultipleInAndOut.txt","r") as multiTx:
    multiTxData = multiTx.read()

with open("dataSingleInSingleOut.txt","r") as singleTx:
    singleTxData = singleTx.read()

btc_addr = "1CGVT1BTV6Q2wpSm1R2vp8L4nCPgq4BuCQ"
satValue = 50000000;



#Test suite for the confirmTx script
# def testConfirmTx():



#Monitors the blockchain.info websocket for incoming Txs
#at @param btc_addr.
# def testMonitorSocket():



#Continually retrieves the websocket data
#@returns dictionary that represents a bitcoin transaction
# def testGetSocketData():




#Checks whether a transaction contains an output
#that corresponds to the purchase made
#@param outputs array of outputs of a given transaction
#@param btc_addr the bitcoin address of the owner
#@param satValue the satoshi value of the purchase
#@returns boolean
def testContainsOutput():
    outputs = json.loads(singleTxData)["x"]["out"]
    assert confirmTx.containsOutput(outputs, btc_addr, satValue) == True;


def testContainsOutputMulti():
    outputsMulti = json.loads(multiTxData)["x"]["out"]
    assert confirmTx.containsOutput(outputsMulti, btc_addr, satValue) == True;



#Confirm that there is a tx fee greater than a threshold
# def testTxFeeCheck():
