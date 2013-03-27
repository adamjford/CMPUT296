"""
Cmput 115/297 Quiz 7 - Expression trees

In this quiz you are asked to construct a simplify routine that takes an
arithmetic expression tree and does some algebraic simplifications on it.

It will require you to write a function for testing if two expression trees
are quivalent, and then write the function to manipulate the tree to produce a 
"simplified" expression tree.

Here is the inductive definition of an expression tree:

Number -  any integer value

Variable - any string composed of one or more of the letters: a-z A-Z and _

Operator - any element from the set operators.  operators is the union of the
    disjoint sets, commutative_operators and noncommutative_operators

Expression Tree:

    Base Case:  If x is a Number or a Variable, then [ x ] is a expression tree.

    Constructor Case:  If t1 and t2 are expression trees, and op is an Operator,
    then [ op, t1, t2 ] is an expression tree.

Examples:
    the expression "2" has the expression tree [ 2 ]

    the expression "(1+a) has the expression tree ['+', [1], ['a'] ]

    the expression "((a+b)*42))" has expression tree

        ['*', [ '+', [ 'a' ], [ 'b' ] ], [ 42 ] ]

Quiz Tasks:

1 - add the following binary operators to the exp_eval function

    - (subtraction), 
    // (integer division), 
    %  (integer mod)

2 - complete the code for the is_equivalent function 

3 - complete the code for the simplify_commute function

Challenge questions for your own amusement:

1 - add a simplify_sub function that simplifies expressions of the form
    ['-', t1, t2] to [0] when t1 and t2 are equivalent.

2 - add an = operator such that ['=', ['x'], t] inserts a variable called 'x'
    into the symbol table and propagates this to any further downstream 
    evaluations.  For example,
        ['+', ['=', ['x'], [2]], ['+', ['x'], [3]]]
    would have value 5.  
    Note, since a variable not in the symbol table has its name as its value,
    you can manufacture variable names and then assign to them!

3 - add an 'if' operator such that ['if', cond, true_case, false_case]
    evaluates the expression cond, and if the result is
    true, then evaluates the expression true_case and returns that value.  
    false, then evaluates the expression false_case and returns that value.  


"""

# definition of the valid binary operators in an expression.
commutative_operators = {'+', '*'}
non_commutative_operators = {"-", "//", "%"}

operators = set.union(commutative_operators, non_commutative_operators)

def infix_unparse(t):
    """
    Unparse an expession tree into a fully parenthesized infix expression

    >>> infix_unparse( [ '*', [ '+', [1], [2] ], [ '+', [3], [4]]] )
    '((1+2)*(3+4))'

    >>> t = ['+', ['+', ['+', ['A'], ['B']], ['+', ['C'], ['D']]], ['+', ['+', [1], [2]], ['+', [3], [4]]]]

    >>> infix_unparse(t)
    '(((A+B)+(C+D))+((1+2)+(3+4)))'
    """

    if len(t) == 1:
        return str(t[0])

    op = t[0]
    lhs = infix_unparse(t[1])
    rhs = infix_unparse(t[2])

    return "({l}{o}{r})".format(l=lhs, r=rhs, o=op)


import re
def str_to_tokens(s):
    """
    Convert an input string into a list of tokens for parsing

    >>> str_to_tokens("+ + // A Barney + C D + + 1 -22 + 3 4")
    ['+', '+', '//', 'A', 'Barney', '+', 'C', 'D', '+', '+', '1', '-22', '+', '3', '4']

    """

    # split the string s on delimiters that are a string of 1 or more 
    # whitespace characters.

    return re.split( r"\s+", s)

def PPN_parse(tokens):
    """
    Parse a Polish Prefix Notation expression into an expression tree.

    >>> PPN_parse([ '42' ])
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

    if t not in operators:
        return [ t ]
        
    return [ t, PPN_parse(tokens), PPN_parse(tokens) ]

#
#   Quiz Tasks Start Here
#

def exp_eval(t, sym_table = None):
    """
    Given expression tree t, and a dictionary sym_table that maps variables
    to their values, compute the result of evaluating the expression, and then
    returns that as an expression tree.

    If a variable, say 'X', does not have an entry in sym_tab, then it's value
    is just 'X'.  Then exp_eval will raise an exception.

    >>> exp_eval( [ 42 ] )
    42

    >>> exp_eval( [ '*', [ '+', [1], [2] ], [ '+', [3], [4]]] )
    21

    >>> exp_eval( [ '*', ['a'], ['+', [2], [4] ] ], { 'a': -10}  )
    -60

    >>> exp_eval( [ '-', [10], [3] ] )
    7

    >>> exp_eval( [ '*', [ '+', [1], [2] ], [ '-', [3], [4]]] )
    -3

    >>> exp_eval( [ '*', [ '+', [1], [2] ], [ '-', [4], [3]]] )
    3

    >>> exp_eval( [ '//', [10], [3] ] )
    3

    >>> exp_eval( [ '*', [ '//', [50], [10] ], [ '+', [3], [4]]] )
    35

    >>> exp_eval( [ '%', [6], ['//', [20], [4]] )
    1

    """
    if sym_table is None:
        sym_table = { }

    if len(t) == 1:
        # Assume it is a variable if it is in the symbol table
        v = t[0];
        if v in sym_table:
            # look up its value
            return sym_table[v]
        else:
            # v is its value.  So if 'x' is not in the symbol
            # table, then the value of ['+', ['x'], ['y']] is 'xy'
            return v

    # fetch the parts of the expression
    op = t[0]

    # evaluate the sub-expressions
    lhs = exp_eval(t[1], sym_table)
    rhs = exp_eval(t[2], sym_table)

    if op == '+':
        return lhs + rhs

    if op == '*':
        return lhs * rhs

    raise Exception("Unknown operator '{}'".format(op))

def is_equivalent(t1, t2):
    """
    Check if two expression trees are equivalent up to commutativity of
    + and *

    >>> is_equivalent([ 42 ], [ 42 ])
    True

    >>> is_equivalent([ 43 ], [ 42 ])
    False

    >>> is_equivalent([ 42 ], [ '+', [1], [42] ])
    False

    >>> is_equivalent([ '+', [1], [42] ], [ '+', [1], [42] ])
    True

    >>> is_equivalent([ '+', [42], [1] ], [ '+', [1], [42] ])
    True

    >>> is_equivalent(PPN_parse(str_to_tokens("+ + A B + A B + + A B + B A")), PPN_parse(str_to_tokens("+ + A B + B A + + A B + A B")) )
    True
    """

    if len(t1) != len(t2):
        return False

    if len(t1) == 1:
        return t1 == t2

    (op1, lhs1, rhs1) = t1
    (op2, lhs2, rhs2) = t2

    if op1 != op2:
        return False

    # (a op b) and (a op b) are equivalent
    if is_equivalent(lhs1, lhs2) and is_equivalent(rhs1, rhs2):
        return True

    # (a op b) and (b op a) are also equivalent when op is commutative
    if op1 in commutative_operators:
        pass

    return False


def simplify_commute(t):
    """
    Takes an expression tree t and simplifies it by replacing sub expressions
    of the form ( E1 + E1 ) and replacing them by ( 2 * E1 )

    BUT, also takes into account the commutativity of * and +, so that
    ( (A+B) + (B+A) ) is simplified to ( 2 * (A+B) )
    
    >>> simplify_commute(PPN_parse(str_to_tokens("+ + 2 1 + 1 2")))
    ['*', [2], ['+', [2], [1]]]

    >>> simplify_commute(PPN_parse(str_to_tokens("+ + A B + B A")))
    ['*', [2], ['+', ['A'], ['B']]]

    >>> simplify_commute(PPN_parse(str_to_tokens("+ + + A B + A B + + A B + B A")))
    ['*', [2], ['*', [2], ['+', ['A'], ['B']]]]

    """

    if len(t) <= 1: return t

    (op, lhs, rhs) = t

    lhs = simplify_commute(lhs)
    rhs = simplify_commute(rhs)

    # check for exact match of lhs and rhs, ignoring commutativity of + and *, 
    # and if they match return the tree that decsribes (2 * lhs)

    if op == '+' and is_equivalent(lhs, rhs) :
        pass
    
    # rebuild the same tree node as we had originally
    return [op, lhs, rhs]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    

