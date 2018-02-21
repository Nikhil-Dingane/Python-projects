import random

randnum=int(random.randint(0,20))
numtry=0

def takeaguess(randnum1,numtry1):
  guess=0
  
  while guess != randnum1:
    print('Take a guess')
    guess=int(input())
    
    if guess < randnum1:
      print('Your guess is lower')
      numtry1+=1
      continue
      
    elif guess > randnum1:
      print('Your guess is higher')
      numtry1+=1
      continue
      
    else:
      break
  
  if guess == randnum1:
      print("You've guessed it right boi! In "+ str(int(numtry1)+1) + " number of tries congrats!")
  else:
    print('Nope i was guessing'+str(randnum1))
      


print(randnum) 
takeaguess(randnum,numtry)      

