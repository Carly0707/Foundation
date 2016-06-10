import unittest

# Built-in String Methods
class Basic(unittest.TestCase):
    def setUp(self):
        self.str = "this is string example....wow!!!"

    def tearDown(self):
        pass

    def test_cap(self):
        print "str.capitalize() : ",  self.str.capitalize()

    def test_center(self):
        print "str.center(40, 'a') : ", self.str.center(40, 'x')

    def test_count(self):
        sub = 'i'
        print "str.count(sub, 4, 40) : ", self.str.count(sub, 4, 40)
        sub = "wow";
        print "str.count(sub) : ", self.str.count(sub)



if __name__ == '__main__':
    unittest.main()