import sys

text=input('Enter your text:').lower()
flag=True
count=-1

for i in range(0,len(text)):
    if text[i]==text[count]:
         flag=True
         count-=1
    else:
        flag=False
        print('Not Anagram!')
        sys.exit()

if flag==True:
    print('String is Anagram')
