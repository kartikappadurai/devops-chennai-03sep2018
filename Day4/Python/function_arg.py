#!/usr/bin/python

def sayHello( msg ):
   print ( str( type(msg) ) + ' ==> ' +  str( msg )  )

def doMathOperations (val1, val2):
    sum = val1 + val2
    diff = val1 - val2
    product = val1 * val2
    division = val1 / val2

    return sum, diff, product, division

def main():
    sayHello( 'Hello Python!' )
    sayHello( 10 )
    sayHello( 1.0 )
    sayHello( 'a' )

    number1 = 20
    number2 = 30

    result1, result2, result3, result4 = doMathOperations( number1, number2 )

    print ( 'Sum of ' + str (number1) + ' and ' + str(number2) + ' is ' + str(result1) )
    print ( 'Difference of ' + str (number1) + ' and ' + str(number2) + ' is ' + str(result2) )
    print ( 'Product of ' + str (number1) + ' and ' + str(number2) + ' is ' + str(result3) )
    print ( 'Division of ' + str (number1) + ' and ' + str(number2) + ' is ' + str(result4) )

main()
