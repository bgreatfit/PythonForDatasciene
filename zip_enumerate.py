items = ['yam', 'beans', 'rice']
weights = [20, 30, 40, 60, 20]
scores = [1, 1, 2, 2, 3, 3, 3, 3, 4]
freq = []




for index, item in enumerate(scores):
    print('Index:{} - Item:{}, Scores:{}'.format(index, item, sum(scores)))
#freq

age = [5, 3, 4]
for item, weight in zip(items, weights):
    print('{}: {}'.format(items, ','.join(items)))
box = list(zip(range(len(items)), items))
box1 = iter(box)

# print(box)
# enumerate()
# print(box1.__next__())
# print(box1.__next__())
# item, weight = zip(*box)