def gene():
    print("first generator execution")
    for i in range(3):
        try:
            v = yield i
        except ValueError as err:
            print('ValueError caught', err)
        print('received value :', v)
    return 'Raise StopIteration via return. Accessible vie error.value'


a = gene()

next(a)
a.send('from caller')

a.throw(ValueError, '@@$raised')

a.close()
try:
    next(a)
except StopIteration as e:
    print(e.value)
