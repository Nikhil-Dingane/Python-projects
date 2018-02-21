import pyperclip
import re

phoneregex=re.compile(r'''(
(\d{3}|\(\d{3}\))? #areaCode
(\s|-|\.)? #separator
(\d{3}) #first part
(\s|-|\.)? #separator
(\d{4}) #second part
(\s*(ext|x|ext.)\s*(\d{2,5}))? #extension
)''',re.VERBOSE)

mailregex=re.compile(r'''(
[a-zA-Z0-9._%+-]+  #first part
@ #@ symbol
[a-zA-z0-9.-]+  #domain name
(\.[a-zA-Z]{2-4})  #dot-something
)''',re.VERBOSE)

text=pyperclip.paste()
matches=[]
for groups in phoneregex.findall(text):
    phonenum='-'.join([groups[1],groups[3],groups[5]])
    if groups[8]!='':
        phonenum+=' x' + groups[8]
    matches.append(phonenum)
for groups in mailregex.findall(text):
    matches.append(groups[0])
    print(matches.append(groups[0]))

if len(matches)>0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard')
    print('\n'.join(matches))
else:
    print('No matches are found.!')
    
