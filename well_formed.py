def well_formed(expressions):
    """
    INPUT: a list of string expressions consisting of parentheses, curly braces, or square brackets
    OUTPUT: 1 if the expression is well-formed; 0 otherwise
    """
    open_set = set("({[")
    match_set = set([('(', ')'),('{', '}'), ('[', ']')])
    stack = []
    for expression in expressions:
        if len(expression) % 2 != 0:
            print 0
        else:
            for i in xrange(len(expression)):
                if expression[i] in open_set:
                    stack.append(expression[i])
                else: 
                    if len(stack) == 0:
                        #print 0
                        pass
                    last = stack.pop()
                    if (last, expression[i]) not in match_set:
                        print 0
                    else: 
                        print 1

