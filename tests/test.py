'''
Test script
*WARNING* Don't run this on a production bitcoin server! *WARNING*
Only on the test network.
'''
import sys
sys.path.append('../src')

import bitcoin
from bitcoin.exceptions import BitcoinException,InsufficientFunds

if __name__ == "__main__":
    conn = bitcoin.connect_to_local()

    assert(type(conn.getblockcount()) is int)
    assert(type(conn.getblocknumber()) is int)
    assert(type(conn.getconnectioncount()) is int)
    assert(type(conn.getdifficulty()) is float)
    assert(type(conn.getgenerate()) is bool)
    conn.setgenerate(True)
    conn.setgenerate(True, 2)
    conn.setgenerate(False)
    assert(type(conn.gethashespersec()) is int)
    account = "testaccount"
    account2 = "testaccount2"
    bitcoinaddress = conn.getnewaddress(account)
    conn.setaccount(bitcoinaddress, account)
    address = conn.getaccountaddress(account)
    address2 = conn.getaccountaddress(account2)
    assert(conn.getaccount(address) == account) 
    addresses = conn.getaddressesbyaccount(account)
    assert(address in addresses)
    #conn.sendtoaddress(bitcoinaddress, amount, comment=None, comment_to=None)
    conn.getreceivedbyaddress(bitcoinaddress)
    conn.getreceivedbyaccount(account)
    conn.listreceivedbyaddress()
    conn.listreceivedbyaccount()
    #conn.backupwallet(destination)
    x = conn.validateaddress(address)
    assert(x.isvalid == True)
    x = conn.validateaddress("invalid")
    assert(x.isvalid == False)

    info = conn.getinfo()
    print "Blocks: %i" % info.blocks
    print "Connections: %i" % info.connections
    print "Difficulty: %f" % info.difficulty


