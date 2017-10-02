import ./confirmTx
import pytest

#Test suite for the confirmTx script
def testConfirmTx():


#Monitors the blockchain.info websocket for incoming Txs
#at @param btc_addr.
def testMonitorSocket():



#Continually retrieves the websocket data
#@returns dictionary that represents a bitcoin transaction
def testGetSocketData():




#Checks whether a transaction contains an output
#that corresponds to the purchase made
#@param outputs array of outputs of a given transaction
#@param btc_addr the bitcoin address of the owner
#@param satValue the satoshi value of the purchase
#@returns boolean
def testContainsOutput():




#Confirm that there is a tx fee greater than a threshold
def testTxFeeCheck():
