def exp_eval(t):
    """

    >>> exp_eval( [ 42 ] )
    42
    >>> exp_eval( [ '*', [ '+', [1], [2] ], [ '+', [3], [4]]] )
    21
    """
    if len(t) == 1:
        return t[0]

    op = t[0]
    lhs = exp_eval(t[1])
    rhs = exp_eval(t[2])

    if op == '+':
        return lhs + rhs

    if op == '*':
        return lhs * rhs

def unparse(t):
    """
    >>> unparse( [ '*', [ '+', [1], [2] ], [ '+', [3], [4]]] )
    '((1+2)*(3+4))'
    """
    if len(t) == 1:
        return str(t[0])

    op = t[0]
    lhs = unparse(t[1])
    rhs = unparse(t[2])

    return '({l}{o}{r})'.format(l=lhs, o=op, r=rhs)

def PPN_parse(tokens):
    """
    >>> PPN_parse( [ '42' ] )
    [42]

    >>> PPN_parse( [ '+', '1', '2' ] )
    ['+', [1], [2]]
    """

    t = tokens.pop(0)

    try:
        r = int(t)
        return [ r ]
    except ValueError:
        pass

    return [ t, PPN_parse(tokens), PPN_parse(tokens) ]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
