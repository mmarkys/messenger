from flask import Flask, jsonify, request, abort
from collections import Counter
import time
import requests


app = Flask(__name__)

db = [
    {
        'text': 'Привет',
        'time': time.time(),
        'name': 'Nick1'
    },
    {
        'text': 'Привет, Nick',
        'time': 1610742279.1781394,
        'name': 'Jane1'
    }
]

def get_btc():
    url = 'https://yobit.net/api/2/btc_usd/ticker'
    response = requests.get(url).json()
    price = response['ticker']['last']
    return str(price) + ' usd'

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/status")
def status():
    count_text = Counter()
    for p in db:
        count_text[p['text']] += 1

    count_name = Counter()
    for p in db:
        count_name[p['name']] += 1

    message = {
        'all_text':len(count_text),
        'all_user':len(count_name),
        'status': True,
        'name': "Chat",
        'time': time.time(),
    }
    return jsonify(message)

@app.route('/send',methods=['POST'])
def send_messages():
    if not isinstance(request.json, dict):
        return abort(400)

    name = request.json.get('name')
    text = request.json.get('text')

    if not isinstance(name, str) or not isinstance(text, str) :
        return abort(400)
    if name == '' or text == '':
        return abort(400)
    if text == 'BTC':
        text = get_btc()

    message = {
        'text': text,
        'time': time.time(),
        'name': name
    }
    db.append(message)
    return {'ok':True}

@app.route('/messages')
def get_messages():
    try:        
        after = float(request.args['after'])

    except:
        return abort(400)

    messages = []
    for message in db:
        if message['time'] > after:
            messages.append(message)

    return {'messages': messages[:100]}




app.run()