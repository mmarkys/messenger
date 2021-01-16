from collections import Counter
import time
db = [
    {
        'text': 'Привет',
        'time': time.time(),
        'name': 'Nick1'
    },
    {
        'text': 'Привет, Nick',
        'time': 1610742279.1781394,
        'name': 'Jane'
    },
    {
        'text': 'Привет,n mn Nick',
        'time': 1610742279.1781394,
        'name': 'Jane1'
    }
]

count_text = Counter()
for p in db:
    count_text[p['text']] += 1;
print( 'There are', len(count_text), 'text.')

count_name = Counter()
for p in db:
    count_name[p['name']] += 1;
print( 'There are', len(count_name), 'name.')