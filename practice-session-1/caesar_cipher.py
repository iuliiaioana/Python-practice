
# a-97
# z-122

def caesar_key(n,sir,l=''):
    for i in sir:
        if ord(i)+n in range(97,123):
            l=l+chr(ord(i)+n)
        elif ord(i) in range(97,123):
            l=l+chr(ord(i)-122+97-1+n)
        else:
            l=l+i
    return l



print(caesar_key(4,'abc dfzz'))
print(caesar_key(4,'abcd xyz'))


