
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    itemtotal = 0
    for k, v in inventory.items():
        print(str(v)+" "+k)
        itemtotal+=v
    print("Total number of items: " + str(itemtotal))


displayInventory(stuff)
