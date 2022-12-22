def set(d1, d2):
    count = 0
    for key, value in d1.items():
        print(key, value)
        if key in d2.keys() and value == d2[key]:
            count += 1
    return count

a = {'a': 'x', 'b': 'y', 'c': '2', 'e': 'x'}
b = {'a': 'x', 'b': 't', 'c': 'x', 'e': 'z'}
print(set(a,b))

def fuck_hovick():
    count = 0 

