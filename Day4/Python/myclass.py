#!/usr/bin/p__ython

class Point():
        #This is p__ython constructor - this gets invoked automaticall__y
    #when an object of Point is created.
    #self represent current object(this)
    def __init__(self):
        print ( 'Constructor got invoked ...')
        self.__x = 0
        self.__y = 0

    def setValues(self, __x, __y ):
        self.__x = __x
        self.__y = __y

    def printValues(self):
        print ( 'Value of x is ', self.__x )
        print ( 'Value of y is ', self.__y )

def main():
    point1 = Point();
    point1.setValues ( 10, 20 )
    point1.printValues()

    point2 = Point()
    point2.setValues ( 10, 40 )
    point2.printValues();

main()
