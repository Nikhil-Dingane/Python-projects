dict={'Mohan':'Apr21','Swapnil':'July24','Vaishnavi':'Jan29'}
while True:
	print('What is your name?(Enter nothing to exit)')
	name=input()
	if name=='':
		break
	if name in dict:
		print('Hello, '+name+ ' your birthday is on ' + dict[name])
	else:
		print('I dont know you when is your birthday?')
		bday=input()
		dict[name]=bday
		print('Repository updated successfully!')
