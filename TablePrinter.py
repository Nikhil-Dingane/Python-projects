tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

maxWidth=[0] * len(tableData)

def printTable(table,maxWidth):
    for i in range(0,len(table)):
        for j in range(0,len(table[0])):
            if len(table[i][j])>maxWidth[i]:
                maxWidth[i]=len(table[i][j])
    printnow(table,maxWidth)

def printnow(table,maxWidth):
    print('TABLE'.center(21,'-'))
    for i in range(len(table[0])):
        count=0
        for j in range(len(table)):
            print(' '+table[j][i].rjust(maxWidth[count]),end='')
            count+=1
        print()
            
printTable(tableData,maxWidth)
