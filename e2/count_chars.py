def countChars():
    question_prompt = 'What is the input string?'
    string = input(question_prompt)
    while (string == ''):
        string = input('Must input someting.' + question_prompt)
    print('{} has {} characters.'.format(string, len(string)))


if __name__ == '__main__':
    countChars()