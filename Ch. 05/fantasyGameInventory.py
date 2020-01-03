#! python3
# Automate Boring Stuff Practice Project - Chapter 5
# fantasyGameInventory.py - displays a fantasy game inventory summary from a
# given dictionary object

def displayInventory(anyInventory):
  print('Inventory:')
  item_total = 0
  for k, v in anyInventory.items():
    item_total += int(v)
    print(str(v) + ' ' + str(k))
  print('Total number of items: ' + str(item_total))

stuff = {'rope': 1,  'torch': 6, 'gold coin': 42, 'dagger': 1,  'arrow': 12}

displayInventory(stuff)
