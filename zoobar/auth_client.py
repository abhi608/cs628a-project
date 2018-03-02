from debug import *
from zoodb import *
import rpclib

client_connect = rpclib.client_connect("/authsvc/sock")

def login(username, password):
    ## Fill in code here.
    obj = {
        'username' : username,
        'password' : password
    }
    return client_connect.call('login', **obj)

def register(username, password):
    ## Fill in code here.
    obj = {
        'username' : username,
        'password' : password 
    }
    return client_connect.call('register', **obj)

def check_token(username, token):
    ## Fill in code here.
    obj = {
        'username' : username,
        'token' : token
    }
    return client_connect.call('check_token', **obj)
