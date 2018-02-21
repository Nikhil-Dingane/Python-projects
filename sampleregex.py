import re

pwd=input('Enter your password: ')

pwdregex=re.compile('(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$])')
mo=pwdregex.search(pwd)
print(mo)
