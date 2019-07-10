import requests
import json

addresses = []
balances = []

with open('burn_address.txt', 'r') as f:
    addresses.append(f.read())

addresses = addresses[0].split('\n')
addresses.pop()

for address in addresses:
    page = requests.get('https://blockchain.info/rawaddr/' + str(address))
    data = json.loads(page.content)
    balances.append(data['final_balance'])

sum = 0
for balance in balances:
    sum += balance
print(sum)