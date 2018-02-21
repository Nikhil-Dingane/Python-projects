#! /usr/bin/python3

#pw.py- AN insecure program to store your passwor dof all your accounts

passwords = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345',
             'facebook':'asdweasafasfefw2343r23rwqqw'}

import sys, pyperclip


if len(sys.argv)<2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]

for k,v in passwords.items():
    if account not in passwords:
        print('This account is not registered!')
        sys.exit()
    if account==k:
        pyperclip.copy(v)
        print('Password is copied!')
