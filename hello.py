def print_hello():
    """
    print formatted string with i if i is even.
    else, print i is odd.
    """
    for i in range(1,10+1):
        if i%2==0:
            print('hello, git for {}th time(s)!'.format(i))
        elif i%3==0:
            print('Oh, {} is odd but, hello!'.format(i))
        else:
            print('nope, i is odd..')

if __name__=='__main__':
    print_hello()

