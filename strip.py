import re

def stripit(text):
    text=strregex.sub('',text)
    print(text)

strregex=re.compile('\s*')

text=input('Enter you text to be trimed')
stripit(text)



