while True:
    age=input('What is your age?')
    if age.isdecimal():
        print('Congrats noob you know how to enter your age now go party or something')
        break
    print('Enter your age as a number')

while True:
    password=input('Enter your password')
    if password.isalnum():
        print("Great Choice. \nI see you're a man of culture as well.")
        break
    print('Enter an alphanumeric password weakling.')
