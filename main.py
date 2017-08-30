import requests
import json
import pprint
import sys

try:
    if sys.argv[1] == 'testnet':
        url = 'https://api.altnet.rippletest.net:51234'
    else:
        url = "http://10.1.11.102:8080/"
except:
    url = 'https://api.altnet.rippletest.net:51234'

headers = {'content-type': 'application/json'}

issuer = {'address': 'rKi6U9uqMMM79GtDdreqN9AvwyLg1HT4iu', 'secret': 'shmBkh3SBi7JzqpD5bBL48rVjw9a1'}

accounts = [{'address': 'rJi1XrePQQiDExHuYA8d7DUJvo6kwAkNeg', 'secret': 'sshDD15wL4m8m5AUDC6icH7LqTWSX'},
            {'address': 'rpirQbRqqHsb3cktdfKh18bUn8BdMawSNU', 'secret': 'sh7nM8JmX52orFLsJ1yGnn2xWS5nn'},
            {'address': 'rBmxDPHe7hmhQ1f4CMryKBphyZZCMXCdzJ', 'secret': 'ssHnqwkd8qwhyXV21DYq7UPSuivCf'}]

def send(payload, *args):
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    try:
        p = args[0]
    except:
        p = False
    if p:
        pprint.pprint(response.json())
    return response

def server_info():
    payload = {
        "method": "server_info",
        "params": [
        {}
        ]
    }
    #pprint.pprint(response.json())
    return payload
    
def account_info(account):
    payload = {
        "method": "account_info",
        "params": [
            {
            "account": account['address'],
            "strict": "true",
            "ledger_index": "current",
            "queue": "true"
            }
        ]
    }
    return payload

def payment(account1, account2, issuer):
    payload ={
        "method": "submit",
        "params": [
            {
                "offline": "false",
                "secret": account1['secret'],
                "tx_json": {
                    "Account": address1,
                    "Amount": {
                        "currency": "USD",
                        "issuer": issuer['address'],
                        "value": "1"
                    },
                    "Destination": account2['address'],
                    "TransactionType": "Payment",
                    "Sequence": get_sequence(account1),
                    "Fee": "100"
                },
                "fee_mult_max": 1000
            }
        ]
    }
    return payload
    
def trust(account1,account2):
    payload = {
        "method": "submit",
        "params": [
            {
            "offline": "false",
            "secret": account1['secret'],
            "tx_json": {
                "TransactionType": "TrustSet",
                "Account": account1['address'],
                "Fee": "12",
                "Flags": 262144,
                "LastLedgerSequence": 8007750,
                "LimitAmount": {
                    "currency": "USD",
                    "issuer": account2['address'],
                    "value": "100"
                },
                "Sequence": get_sequence(account1)
            }
            }
        ]
    }
    return payload

def account_currencies(account):
    payload = {
        "method": "account_currencies",
        "params": [
            {
            "account": account['address'],
            "ledger_index": "validated",
            "strict": "true"
            }
        ]
    }
    return payload
    
def account_lines(account):
    payload = {
        "method": "account_lines",
        "params": [
            {
            "account": account['address'],
            "ledger": "current"
            }
        ]
    }
    return payload

def get_sequence(account):
    r = send(account_info(account))
    if r.ok:
        data = r.json()
        s = data['result']['account_data']['Sequence']
        return s
    else:
        print "Error while get account sequence"
        exit(1)
        
    
def get_my_accounts():
    for key,acc in enumerate(accounts):
        print "Account %s: " % key
        send(account_info(acc), True)
        print "==============================================="
        send(account_currencies(acc), True)
        print "==============================================="
        send(account_lines(acc), True)
        print "==============================================="
        
    print "Issuer: "
    send(account_info(issuer), True)
    print "==============================================="
    send(account_currencies(issuer), True)
    print "==============================================="
    send(account_lines(issuer), True)
    print "==============================================="
    
def main():
    #server_info()
    print "=================================================="
    account_info()
    print "=================================================="

if __name__ == "__main__":
    main()
