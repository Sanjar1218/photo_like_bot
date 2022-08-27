import json

f= open('data.json', 'w')
dct = {
    "1": {"\ud83d\udc4d": 11, "\ud83d\udc4e": 1}
}
json.dump(dct, f)
f.close()