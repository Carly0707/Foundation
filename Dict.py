import unittest

class Basic(unittest.TestCase):

    def test_acess(self):
        dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

        print "dict['Name']: ", dict['Name']
        print "dict['Age']: ", dict['Age']
        print "dict['Alic']: ", dict['Alice']