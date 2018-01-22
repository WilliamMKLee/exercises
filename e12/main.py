def strToPostiveNumber(n):
    try:
        number = float(n)
    except ValueError:
        raise ValueError('the value {} can not convert to integer'.format(n))

    if number < 0:
        raise ValueError('the value {} is must larger than 0'.format(n))

    return number


def askPrompt():
    principal = strToPostiveNumber(input('Enter the principal:'))
    interest = strToPostiveNumber(input('Enter the rate of interest:'))
    years = strToPostiveNumber(input('Enter the number of years:'))
    total = principal * (1 + interest * 0.01 * years)
    print('After {} years at {}%, the investment will be worth ${}.'.format(
        years, interest, total))


if __name__ == '__main__':
    askPrompt()