import datetime


def calculateRetireYear(current_year, retire_year):
    return retire_year - current_year


def shiftYears(years):
    now = datetime.datetime.now()
    return now.year + years


def strToPostiveNumber(n):
    try:
        number = int(n)
    except ValueError:
        raise ValueError('the value {} can not convert to integer'.format(n))

    if number < 0:
        raise ValueError('the value {} is must larger than 0'.format(n))

    return number


def askRetirePrompt():
    current_age = strToPostiveNumber(input('What is your current age?'))
    retire_age = strToPostiveNumber(
        input('At what age would you like to retire?'))

    before_retire_years = calculateRetireYear(current_age, retire_age)
    current_year = datetime.datetime.now().year

    print('You have {} years left until you can retire.'.format(
        before_retire_years))
    print('It\'s {current_year}, so you can retire in {retire_year}.'.format(
        current_year=current_year,
        retire_year=shiftYears(before_retire_years)))


if __name__ == '__main__':
    askRetirePrompt()