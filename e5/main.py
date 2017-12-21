def inputToInt(question_prompt):
    string = input(question_prompt)
    try:
        return int(string)
    except ValueError:
        raise ValueError(
            'your input {} is invalid, not possbile convert to integer'.format(
                string))


def printArithmetic(num1, num2):
    print('{} + {} = {}'.format(num1, num2, num1 + num2))
    print('{} - {} = {}'.format(num1, num2, num1 - num2))
    print('{} * {} = {}'.format(num1, num2, num1 * num2))
    print('{} / {} = {}'.format(num1, num2, num1 / num2))


def simpleMath():
    first_number = inputToInt('What is the first number?')
    second_number = inputToInt('What is the second number?')
    if first_number < 0 or second_number < 0:
        raise ValueError('the input not accept negative number')
    printArithmetic(first_number, second_number)


if __name__ == '__main__':
    simpleMath()