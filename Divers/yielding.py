def gen():
    a = "abcdefghijklmnopqrstuvwxyz"
    for lettre in a:
        yield lettre

for i in gen():
    print(i, end=" ")
