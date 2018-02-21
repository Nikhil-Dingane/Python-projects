allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
            'Bob': {'ham sandwiches': 3, 'apples': 2},
            'Carol': {'cups': 3, 'apple pies': 1}}

def totalbought(guests, item):
    numbought=0
    for k,v in guests.items():
        numbought=numbought+v.get(item,0)
    return numbought

while True:
    item=input('Of what item do you need the information of?')
    if item=='n' or item=='N':
        break
    else:
        nb=totalbought(allGuests,item)
        print('The total number of '+str(item)+' are '+str(nb))
    
