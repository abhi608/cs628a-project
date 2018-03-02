from zoodb import *
from debug import *

import time

def transfer(sender, recipient, zoobars):
    # persondb = person_setup()
    # senderp = persondb.query(Person).get(sender)
    # recipientp = persondb.query(Person).get(recipient)

    # sender_balance = senderp.zoobars - zoobars
    # recipient_balance = recipientp.zoobars + zoobars

    bankdb = bank_setup()
    senderb = bankdb.query(Bank).get(sender)
    recipientb = bankdb.query(Bank).get(recipient)

    sender_balance = senderb.zoobars - zoobars
    recipient_balance = recipientb.zoobars + zoobars

    if sender_balance < 0 or recipient_balance < 0:
        raise ValueError()

    # senderp.zoobars = sender_balance
    # recipientp.zoobars = recipient_balance
    # persondb.commit()
    
    senderb.zoobars = sender_balance
    recipientb.zoobars = recipient_balance
    bankdb.commit()

    transfer = Transfer()
    transfer.sender = sender
    transfer.recipient = recipient
    transfer.amount = zoobars
    transfer.time = time.asctime()

    transferdb = transfer_setup()
    transferdb.add(transfer)
    transferdb.commit()

def balance(username):
    # db = person_setup()
    # person = db.query(Person).get(username)
    # return person.zoobars
    log("test_msg")
    log(username)
    db = bank_setup()
    log(db)
    bank = db.query(Bank).get(username)
    log(bank)
    return bank.zoobars

def get_log(username):
    db = transfer_setup()
    return db.query(Transfer).filter(or_(Transfer.sender==username,
                                         Transfer.recipient==username))

def setup(username):
    log("test-2")
    log(username)
    db = bank_setup()
    bank = Bank()
    bank.username = username
    db.add(bank)
    db.commit()
