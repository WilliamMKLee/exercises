SLICE_PER_PIZZA = 8


def strToPostiveNumber(n):
    try:
        number = int(n)
    except ValueError:
        raise ValueError('the value {} can not convert to integer'.format(n))

    if number < 0:
        raise ValueError('the value {} is must larger than 0'.format(n))

    return number


def askPrompt():
    amount_of_people = strToPostiveNumber(input('How many people?'))
    amount_of_pizza = strToPostiveNumber(input('How many pizzas do you have?'))

    total_slice = SLICE_PER_PIZZA * amount_of_pizza

    slices_per_one = total_slice // amount_of_people
    left_pizza = total_slice % amount_of_people
    print('{} people with {} pizzas'.format(amount_of_people, amount_of_pizza))
    if slices_per_one > 1:
        print('Each person gets {} pieces of pizza.'.format(slices_per_one))
    else:
        print('Each person gets {} piece of pizza.'.format(slices_per_one))
    print('There are {} leftover pieces.'.format(left_pizza))


if __name__ == '__main__':
    askPrompt()