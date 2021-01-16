import requests

name = input('Enter name: ')

while True:
    text = input('Enter text: ')

    response = requests.post(
        'http://127.0.0.1:5000/send',
        json={'name':name,'text':text}
    )