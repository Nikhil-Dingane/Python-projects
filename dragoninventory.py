def displayInventory(inventory):
    print("Inventory:")
    itemtotal = 0
    for k, v in inventory.items():
        print(str(v)+" "+k)
        itemtotal+=v
    print("Total number of items: " + str(itemtotal))


def addToInventory(inventory, addedItems):
    for i in range(0,len(addedItems)):
            if addedItems[i] in inventory:
                inventory[addedItems[i]]+=1
            else:
                inventory[addedItems[i]]=1
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
