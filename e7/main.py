def square(length, width):
    return length * width


def feetTometherArea(feet_area):
    return feet_area * 0.09290304


def meterToFeetArea(meter_area):
    return meter_area / 0.09290304


def strToPostiveNumber(n):
    try:
        number = int(n)
    except ValueError:
        raise ValueError('the value {} can not convert to integer'.format(n))

    if number < 0:
        raise ValueError('the value {} is must larger than 0'.format(n))

    return number


def askMeterOrFeet():
    unit = input('choice unit is meter or feet?')
    if unit not in ('meter', 'feet'):
        raise ValueError('please choice meter or feet')
    return unit


def askPrompt():

    unit = askMeterOrFeet()

    if unit == 'meter':
        pass
    length = strToPostiveNumber(input('What is the length of the room?'))
    width = strToPostiveNumber(input('What is the width of the room?'))

    print(
        'You entered dimensions of {length} {unit} by {width} {unit}.'.format(
            length=length, width=width, unit=unit))

    print('The area is')

    area = square(length, width)
    if unit == 'meter':
        print('{} square methers'.format(area))
        print('{} square feet'.format(meterToFeetArea(area)))
    else:
        print('{} square feet'.format(area))
        print('{} square methers'.format(feetTometherArea(area)))


if __name__ == '__main__':
    askPrompt()