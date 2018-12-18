import json


s = {'lista': ['elt1', 2, 'elt3'], 'liczba': 42}
print(repr(s))  # funkcja repr() formatuje trochę inaczej, ułatwiając rozpoznawanie typów
json_s = json.dumps(s)
print(repr(json_s))
parsed_s = json.loads(json_s)
print(repr(parsed_s))


print('1')
print(1)
print(repr('2'))
print(repr(2))


for i in sorted([5, 2, 1, 3, 4]):
    print(i)


l = {'a': 5, 'b': 'a'}, {'a': 2, 'b': 'o'}, {'a': 1, 'b': 'z'}, {'a': 3, 'b': 's'}, {'a': 4, 'b': 'i'}

for i in sorted(l, key=lambda x: x['a']):
    print(i['b'])
