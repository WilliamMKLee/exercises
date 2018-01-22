GALLON_TO_SQUARE_FEET = 350


def strToPostiveNumber(n):
    try:
        number = int(n)
    except ValueError:
        raise ValueError('the value {} can not convert to integer'.format(n))

    if number < 0:
        raise ValueError('the value {} is must larger than 0'.format(n))

    return number


def askPrompt():
    feet_to_paint = strToPostiveNumber(
        input('How name feet you neet to paint?'))
    gallons = feet_to_paint // GALLON_TO_SQUARE_FEET
    if feet_to_paint % GALLON_TO_SQUARE_FEET != 0:
        gallons += 1
    print(
        'You will need to purchase {} gallons of paint to cover {} square feet.'.
        format(gallons, feet_to_paint))


if __name__ == '__main__':
    askPrompt()
