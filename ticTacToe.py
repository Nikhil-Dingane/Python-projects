theBoard={'top-L':' ','top-M':' ','top-R':' ',
          'mid-L':' ','mid-M':' ','mid-R':' ',
          'low-L':' ','low-M':' ','low-R':' '}

turn='X'

def printBoard(board):
    print(board['top-L']+'|'+board['top-M']+'|'+board['top-R'])
    print('-+-+-')
    print(board['mid-L']+'|'+board['mid-M']+'|'+board['mid-R'])
    print('-+-+-')
    print(board['low-L']+'|'+board['low-M']+'|'+board['low-R'])
    
printBoard(theBoard)

for i in range(9):
    print('It is the turn of '+turn+' What space should you play?')
    move=input()
    theBoard[move]=turn
    if turn=='X':
        turn='O'
    else:
        turn='X'
    printBoard(theBoard) 
        