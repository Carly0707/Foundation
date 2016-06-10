import unittest

class Basic(unittest.TestCase):
    def setup(self):
        pass

    def tearDown(self):
        pass

    def test_List(self):
        list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
        tinylist = [123, 'john']
        print list          # Prints complete list
        print list[0]       # Prints first element of the list
        print list[1:3]     # Prints elements starting from 2nd till 3rd
        print list[2:]      # Prints elements starting from 3rd element
        print tinylist * 2  # Prints list two times
        print list + tinylist # Prints concatenated lists

    def test_tuple(self):
        tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
        tinytuple = (123, 'john')
        print tuple           # Prints complete list
        print tuple[0]        # Prints first element of the list
        print tuple[1:3]      # Prints elements starting from 2nd till 3rd
        print tuple[2:]       # Prints elements starting from 3rd element
        print tinytuple * 2   # Prints list two times
        print tuple + tinytuple # Prints concatenated lists
        tuple2 = ( 'abcd', 789, [7,8,9] , 2.23, 'john', 70.2  )
        tuple2[2][2] = 10       #tuple generally cannot be updated, unless the element itslef is extensible (list)
        print tuple2

    def test_dictionary(self):
        dict = {}
        dict['one'] = "This is one"
        dict[2]     = "This is two"
        tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
        print dict
        print tinydict          # Prints complete dictionary
        print tinydict.keys()   # Prints all the keys
        print tinydict.values() # Prints all the values

    def test_Bitwise(self):
        a = 00111100    #a=60
        b = 00001101   #b=13
        print a&b, a|b, a^b, ~a

        def test_if(self):
            var1 = 100
            if var1: #????????
                print "1 - Got a true expression value"
            print var1

    def test_elif(self):
        var = 100
        if var == 200:
            print "1 - Got a true expression value"
            print var
        elif var == 150:
            print "2 - Got a true expression value"
            print var
        elif var == 100:
            print "3 - Got a true expression value"
            print var
        else:
            print "4 - Got a false expression value"
            print var
        print "Good bye!"

        var2 = 0
        if var2:
            print "2 - Got a true expression value"
            print var2
        else:
            print "2 - Got a false expression value"
            print var2
        print "Good bye!"

    def test_nestedif(self):
        var = 100
        if var < 200:
            print "Expression value is less than 200"
            if var == 150:
                print "Which is 150"
            elif var == 100:
                print "Which is 100"
            elif var == 50:
                print "Which is 50"
        elif var < 50:
            print "Expression value is less than 50"
        else:
            print "Could not find true expression"

        print "Good bye!"

    def test_while(self):
        count = 0
        while count < 5:
            print count, " is  less than 5"
            count = count + 1
        else:
            print count, " is not less than 5"


    def test_string(self):
        a= 'hello'
        if 'h' in a:
            print 'h' + ' is in' + a
        #%s - string conversion via str() prior to formatting
        #%d - signed decimal integer
        print "My name is %s and weight is %d kg!" % ('Zara', 21)

if __name__ == '__main__':
    unittest.main()



