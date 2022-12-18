import json
import time

card_amount_on_win = json.loads(open("win.json","r").read())["card_amount_on_win"]

count = 0
for x in card_amount_on_win:
    count += x

print(count/len(card_amount_on_win))
