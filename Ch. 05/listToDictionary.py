#! python3
# Automate Boring Stuff Practice Project - Chapter 5
# listToDictionary.py - adds the items in a list object to a dictionary object

def displayInventory(anyInventory):
  print('Inventory:')
  item_total = 0
  for k, v in anyInventory.items():
    item_total += int(v)
    print(str(v) + ' ' + str(k))
  print('Total number of items: ' + str(item_total))

def addToInventory(inventory, addedItems):
  for i in addedItems:
    inventory.setdefault(str(i), 0)
    inventory[str(i)] += 1
  return inventory 

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
