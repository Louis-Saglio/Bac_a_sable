import this


def gene():
    for i in 'ab cd':
        if i == ' ':
            b = yield from '123'
        else:
            b = yield i
        print(b)

a = gene()
next(a)

while True:
    try:
        a.send('haha')
    except (StopIteration, AttributeError) as e:
        if isinstance(e, StopIteration):
            print(e.value)
            break
