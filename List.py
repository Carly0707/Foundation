import unittest

class Basic(unittest.TestCase):

    def setUp(self):
        self.list1 = ['physics', 'chemistry', 1997, 2000];
        self.list2 = [1, 2, 3, 4, 5, 6, 7 ];

    def tearDown(self):
        pass

    def test_acess(self):
        print "list1[0]: ", self.list1[0]
        print "list2[1:5]: ", self.list2[1:5]

    def test_update(self):
        print "Value available at index 2 : ",
        print self.list1[2]
        self.list1[2] = 2001
        print "New value available at index 2 : ",\
        self.list1[2]

    def test_del(self):
        print self.list1
        del self.list1[2]
        print "After deleting value at index 2: "
        print self.list1
