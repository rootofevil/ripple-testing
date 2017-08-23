import requests
import json
import pprint

url = "http://10.1.11.102:8080/"
headers = {'content-type': 'application/json'}

def server_info():
    # Example echo method
    payload = {
        "method": "server_info",
        "params": [
        {}
        ]
    }
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    pprint.pprint(response.json())
    #return response
def account_info():
    payload = {
        "method": "account_info",
        "params": [
            {
            "account": "rG1QQv2nh2gr7RCZ1P8YYcBUKCCN633jCn",
            "strict": "true",
            "ledger_index": "current",
            "queue": "true"
            }
        ]
    }
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    pprint.pprint(response.json())
    
def main():
    server_info()
    print "=========================="
    account_info()

if __name__ == "__main__":
    main()
