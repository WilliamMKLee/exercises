def printQuote():
    quote_prompt = 'What is the quote?'
    author_prompt = 'Who said it?'

    quote = input(quote_prompt)
    author = input(author_prompt)

    print('{author} says, \"{quote}\"'.format(author=author, quote=quote))


if __name__ == '__main__':
    printQuote()