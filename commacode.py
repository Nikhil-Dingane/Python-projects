#spam = ['apples', 'bananas', 'tofu', 'cats']
output=''
spam=[]
while True:
  print('Enter the element you want to enter or enter nothing to stop')
  inp=input()
  if inp=='':
    break
  spam=spam+[inp]

def func(spam,output):
	for i in range(0,len(spam)-1):
	  output=output+spam[i]+', '

	output=output+'and '+spam[-1]+'.'  
	return output

print(func(spam,output))

