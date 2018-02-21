import re
import pyperclip

siteregex=re.compile(r'''(
http #start
s? #s
:// #start done
[A-Za-z0-9-_?=&+#/.]+ #words
(\s|\n)  #End
)''',re.VERBOSE)

matches=[]
text=pyperclip.paste()

for groups in siteregex.findall(text):
    matches.append(groups[0])

if len(matches)>1:
    sites='\n'.join(matches)
    print(sites)
    pyperclip.copy(sites)
else:
    print('No match found!')

