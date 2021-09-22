# this program is designed to demonstrate some proficiency
# with dictionaries. Inspired partly by my Friday-night D and D games,
# and also by the Dictionaries chapter in Automate the Boring Stuff,
# which suggests writing a program to store the inventory for a fantasy game.
my_stuff = {'axe': 1, 'cloak': 2, 'arrow': 14, 'scroll': 5}

def displayInventory(inventory):
    print('Inventory:')
    total_items = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        total_items += v
    print('Total items: ' + str(total_items))

def addToInventory(inventory, added_items):
    # check if item is in inventory, if so, update value
    # if item is NOT in inventory, then add to dictionary 



if __name__ == '__main__':
    displayInventory(my_stuff)
