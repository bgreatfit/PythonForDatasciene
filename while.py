card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
hand = []
while sum(hand) <= 17:
    hand.append(card_deck.pop())
    print(sum(hand))
print(hand)

items = {'beans': 20, 'rice': 10, 'yam': 40}
print(items.items())
new_box = []
weight = 0
for key in items:
    if weight >= 30:
        break
    else:
        new_box.append(key)
        weight += items[key]
print(new_box)
print(weight)
