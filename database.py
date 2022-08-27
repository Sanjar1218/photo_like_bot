import json

class Count:
    like = 0
    dislike = 0

    def __init__(self, id) -> None:
        id = str(id)
        self.id = id
        f = open('data.json', 'r')
        data = json.load(f)
        print('ini', data)
        data.setdefault(id, {'👍': 0, '👎': 0})
        self.like = data[id]['👍']
        self.dislike = data[id]['👎']
        f.close()
        fl = open('data.json', 'w')
        json.dump(data, fl)
        fl.close()

    def add(self, txt):
        f = open('data.json', 'w')
        dct = {"1": {"\ud83d\udc4d": 11, "\ud83d\udc4e": 1}}
        if txt == '👍':
            self.like = 0 if self.like==1 else 1
        else:
            self.dislike = 0 if self.like==1 else 1
        print(dct)
        dct[self.id] = {}
        dct[self.id] = {}
        dct[self.id]['👍'] =self.like
        dct[self.id]['👎'] = self.dislike
        json.dump(dct, f)
        f.close()