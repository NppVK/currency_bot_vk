import json
import requests

r = requests.get(f'https://openexchangerates.org/api/latest.json?app_id=17b739cb48e3496a8de81cceb9b0af7f\
                      &base=USD&symbols=RUB')
total_base = json.loads(r.content)

# Или без использования библиотеки JSON

rr = requests.get(f'https://openexchangerates.org/api/latest.json?app_id=17b739cb48e3496a8de81cceb9b0af7f\
                    &base=USD&symbols=RUB').json()
ttotal_base = rr['rates']

print(total_base)

print(ttotal_base)

# r = requests.get(f'https://openexchangerates.org/api/latest.json?app_id=17b739cb48e3496a8de81cceb9b0af7f\
#               &base={quote_ticker}&symbols={base_ticker}')
# total_base = json.loads(r.content)['rates'][base_ticker]

# Или без использования библиотеки JSON
# r = requests.get(f'https://openexchangerates.org/api/latest.json?app_id=17b739cb48e3496a8de81cceb9b0af7f\
#                    &base={quote_ticker}&symbols={base_ticker}').json()
# total_base = r['rates'][base_ticker]
