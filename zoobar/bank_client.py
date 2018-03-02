from debug import *
from zoodb import *
import rpclib

client_connect = rpclib.client_connect("/banksvc/sock")

def setup(username):
    obj = {
        'username' : username
    }
    return client_connect.call('setup', **obj)

def transfer(sender, recipient, zoobars, token):
    obj = {
        'sender' : sender,
        'recipient' : recipient,
        'zoobars' : zoobars,
        'token' : token
    }
    return client_connect.call('transfer', **obj)

def balance(username):
    obj = {
        'username' : username
    }
    return client_connect.call('balance', **obj)

def get_log(username):
    obj = {
        'username' : username
    }
    return client_connect.call('get_log', **obj) 
