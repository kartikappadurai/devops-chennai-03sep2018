#!/usr/bin/python
class IPhone6S:
    def __init__(self):
        print ('iPhone6S constructor invoked ...')

    def printSpec(self):
        print ('Vendor : ' + 'Apple')
        print ('Model  : ' + 'iPhone 6S')
        print ('Front Camera : ' + 'Yes' )

class IPhone7(IPhone6S):
    def __init__(self):
        IPhone6S.__init__(self)
        print ('iPhone7 constructor invoked ...')

    def printSpec(self):
        IPhone6S.printSpec(self)
        print ('Rear Camera : ' + 'Yes' )

def main():
    iPhone7 = IPhone7()
    iPhone7.printSpec()

main()
