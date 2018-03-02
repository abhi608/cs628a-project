#!/usr/bin/python
#
# Insert bank server code here.
#
import rpclib
import sys
import bank
from debug import *
from sqlalchemy.orm import class_mapper

class BankRpcServer(rpclib.RpcServer):
    ## Fill in RPC methods here.
    # pass
    def rpc_setup(self, username):  
        bank.setup(username)

    def rpc_transfer(self, sender, recipient, zoobars):
        return bank.transfer(sender, recipient, zoobars)

    def rpc_balance(self, username):
        return bank.balance(username)
    
    def rpc_get_log(self, username):
        modified_log = []
        for log in bank.get_log(username):
            obj = {}
            for tmp in class_mapper(log.__class__).columns:
                obj[tmp.key] = getattr(log, tmp.key)
            modified_log.append(obj)
        return modified_log

(_, dummy_zookld_fd, sockpath) = sys.argv

s = BankRpcServer()
s.run_sockpath_fork(sockpath)
