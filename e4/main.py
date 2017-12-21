def madLib():
    noun = input('Enter a noun:')
    verb = input('Enter a verb:')
    adj = input('Enter an adjective:')
    adv = input('Enter an adverb:')

    print('Do you {verb} your {adj} {noun} {adv}? That\'s hilarious!'.format(
        noun=noun, verb=verb, adj=adj, adv=adv))


if __name__ == '__main__':
    madLib()