picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}

def printpicnic(itemsDict,leftWidth,rightWidth):
    print('Picnic Items'.center(leftWidth+rightWidth,'-'))
    for k,v in itemsDict.items():
        print((k).ljust(leftWidth,'.')+(str(v)).rjust(rightWidth))

printpicnic(picnicItems,20,6)
printpicnic(picnicItems,12,5)        
