with open('hello.txt') as f:
    for line in f:
        print(repr(line))
items = {'beans': 20, 'rice': 10, 'yam': 40}
print(list(items))