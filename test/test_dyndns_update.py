'''
Created on 27 Dec 2013

@author: davidal-kanani
'''
import unittest
from dyndnsup.dyndns_update import DynDnsInteract
from dyndnsup.dyndns_update import InvalidLoginException
from dyndnsup import dyndns_update
from requests import RequestException

class TestDynDnsUpdate(unittest.TestCase):

    def testInvalidUrl(self):
        interact = DynDnsInteract('www.url.bad', 'test@mail.com', 'username', 'password')
        with self.assertRaises(RequestException):
            interact.login()
    
    def testValidLogin(self):
        (validuser, validpasswd) = dyndns_update.load_logins()
        interact = DynDnsInteract('https://account.dyn.com/entrance/', 'david.alkanani@gmail.com', validuser, validpasswd)
        interact.login()
        self.assertEqual(interact.browser.title, 'My Dyn Account')
        
    def testInvalidLogin(self):
        interact = DynDnsInteract('https://account.dyn.com/entrance/', 'david.alkanani@gmail.com', 'bad', 'login')
        with self.assertRaises(InvalidLoginException):
            interact.login()

if __name__ == '__main__':
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()