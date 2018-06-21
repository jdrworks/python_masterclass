name = input('What is your name? ')
age = int(input('Hello {0}, how old are you? '.format(name)))
if 18 < age < 31:
    print('Welcome to the holiday, {0}!'.format(name))
else:
    print("I'm sorry {0}, this holiday is not for you".format(name))
