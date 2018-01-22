TAX_RATE = 0.055


def strToPostiveNumber(n):
    try:
        number = float(n)
    except ValueError:
        raise ValueError('the value {} can not convert to integer'.format(n))

    if number < 0:
        raise ValueError('the value {} is must larger than 0'.format(n))

    return number


def calculateGood(index):
    price = strToPostiveNumber(
        input('Enter the price of item {}:'.format(index)))
    quantity = strToPostiveNumber(
        input('Enter the quantity of item {}:'.format(index)))
    return price * quantity


def askPrompt():
    times = 3
    subtotal = 0
    for i in range(1, times+1):
        subtotal += calculateGood(i)
    tax = subtotal * TAX_RATE
    print('Subtotal: ${}'.format(subtotal))
    print('Tax: ${}'.format(tax))
    print('Total: ${}'.format(subtotal + tax))


if __name__ == '__main__':
    askPrompt()