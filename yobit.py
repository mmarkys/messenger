import requests


def get_btc():
    url = 'https://yobit.net/api/2/btc_usd/ticker'
    response = requests.get(url).json()
    price = response['ticker']['last']
    lost_price = price
    print(price)

    return str(price) + ' usd' 
print(get_btc())