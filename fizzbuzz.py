def fizzbuzz():
    """
    INPUT: nothing
    OUTPUT: a list of numbers from 1 to 100
            if the number is a multiple of 3, it prints "fizz"
            if the number is a multiple of 5, it prints "buzz"
            if the number is a multiple of 3 and 5, it prints "fizzbuzz"
    """
    for i in xrange(1,100):
        if i % 3 == 0:
            if i % 5 == 0:
                print "fizzbuzz"
            else: 
                print "fizz"
        elif i % 5 == 0:
            print "buzz"
        else:
            print i


