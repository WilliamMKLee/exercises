"""
the saying hello program
"""


def sayHello():
    name = input('What is your name?:')
    if name:
        return 'Hello {}, nice to meet you!'.format(name)
    else:
        return 'Hello World'


def stdSayHello():
    name = input('What is your name?:')
    if name:
        print('Hello {}, nice to meet you!'.format(name))
    else:
        print('Hello World')
