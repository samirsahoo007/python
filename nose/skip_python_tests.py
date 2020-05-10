import unittest2 as unittest
from nose.plugins.skip import SkipTest


# if skipping a single test in a class, ok to use unittest.skip
# even if you run tests with nosetests:

@unittest.skip('skippping test_something')
def test_something(self):
    print("I'm not going to be run")
    
    
    
# if skipping a whole class and running the tests with nosetests,
# HAVE to use nosetests plugin instead of unittest.skip
# (otherwise setUpClass / tearDownClass are still run):

@SkipTest
class Tests(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("I'm not going to be run")
    
    def test_something(self):
        print("I'm not going to be run")

