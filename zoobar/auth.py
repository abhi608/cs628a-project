from pbkdf2 import PBKDF2
from zoodb import *
from debug import *

import hashlib
import random
import os

#def newtoken(db, person):
#    hashinput = "%s%.10f" % (person.password, random.random())
#    person.token = hashlib.md5(hashinput).hexdigest()
#    db.commit()
#    return person.token

def newtoken(db, cred):
    hashinput = "%s%.10f" % (cred.password, random.random())
    cred.token = hashlib.md5(hashinput).hexdigest()
    db.commit()
    return cred.token

#def login(username, password):
#    db = person_setup()
#    person = db.query(Person).get(username)
#    if not person:
#        return None
#    if person.password == password:
#        return newtoken(db, person)
#    else:
#        return None

def login(username, password):
    db = cred_setup()
    cred = db.query(Cred).get(username)
    if not cred:
        return None
    #if cred.password == password:
    if cred.password == PBKDF2(password, cred.salt).hexread(32):
        return newtoken(db, cred)
    else:
        return None

#def register(username, password):
#    db = person_setup()
#    person = db.query(Person).get(username)
#    if person:
#        return None
#    newperson = Person()
#    newperson.username = username
#    newperson.password = password
#    db.add(newperson)
#    db.commit()
#    return newtoken(db, newperson)

def register(username, password):
    db_person = person_setup()
    db_cred = cred_setup()
    person = db_person.query(Person).get(username)
    cred = db_cred.query(Cred).get(username)
    if person or cred:
        return None
    newperson = Person()
    newcred = Cred()
    newperson.username = username
    newcred.username = username
    newcred.salt = os.urandom(8).encode('base-64')
    newcred.password = PBKDF2(password, newcred.salt).hexread(32)
    #newcred.password = password
    db_person.add(newperson)
    db_cred.add(newcred)
    db_person.commit()
    db_cred.commit()
    return newtoken(db_cred, newcred)

#def check_token(username, token):
#    db = person_setup()
#    person = db.query(Person).get(username)
#    if person and person.token == token:
#        return True
#    else:
#        return False

def check_token(username, token):
    db = cred_setup()
    cred = db.query(Cred).get(username)
    if cred and cred.token == token:
        return True
    else:
        return False
