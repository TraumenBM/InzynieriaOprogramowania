def parse_token(token):
    """
    This function parses a token.
    TODO: write a decent docstring :-)
    """

    if token == '\\and':
        do_something()

    elif token == '\\or':
        do_something_else() #asjadkjad

#jakiś tam tekscik.txt

    elif token == '\\xor':
        '''
        Note that we still need to provide support for the deprecated
        token \xor. Hopefully we can drop support in libfoo 2.0.
        '''
        do_a_different_thing()

    else:
        raise ValueError