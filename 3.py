import sys

try:
    file = open('CabDetails.txt','r')
except FileNotFoundError:
    print("File does not exists!")


def prog(name):
    for i in file:
        if name in i:
            l = i.split(" ")
            print("Status of car {} is : {}".format(name,(l[-1]).strip(" ")))
            return
    print("No car available of name {}".format(name))
            
def validateInput(name):
    if not name:
        print("Name of car cannot be empty")
        sys.exit(0)

name=input("Enter the car name you want the status of:    ")
name=name.upper()
validateInput(name)
prog(name)
        
