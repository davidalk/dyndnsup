'''
Created on 27 Dec 2013

@author: davidal-kanani
'''
import unittest
from dyndnsup.dyndns_update import DynDnsInteract
from requests import RequestException


class TestDynDnsUpdate(unittest.TestCase):


    def testInvalidLogin(self):
        interact = DynDnsInteract("http://www.url.bad", "test@mail.com")
        self.assertRaises(RequestException, interact.login())


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()