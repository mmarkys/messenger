import time
from datetime import datetime
import requests

def print_message(message):
    # TODO beautify time
    message_time = datetime.fromtimestamp(message['time'])
    message_time = message_time.strftime('%Y/%m/%d %H:%M:%S' )
    print(message_time, message['name'])
    print(message['text'])
    print()

def print_messages(db):
    for message in db:
        print_message(message)
after = 0

while True:
    response = requests.get(
        'http://127.0.0.1:5000/messages',
        params={'after':after}
    )
    messages = response.json()['messages']
    for message in messages:
        print_messages(messages)
        after = message['time']

    time.sleep(1)