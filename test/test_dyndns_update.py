'''
Created on 27 Dec 2013

@author: davidal-kanani
'''
import unittest
from dyndnsup import dyndns_update
from dyndnsup.dyndns_update import DynDnsInteract
from dyndnsup.dyndns_update import InvalidLoginError
from urllib import error

class TestDynDnsUpdate(unittest.TestCase):

    def testUnreachableUrl(self):
        interact = DynDnsInteract('http://www.url.bad', 'test@mail.com', 'username', 
                                  'password', 'my.dn.com', '/usr/local/bin/phantomjs')
        with self.assertRaises(error.URLError):
            interact.login()
    
    def testValidLogin(self):
        (validuser, validpasswd, config) = dyndns_update.load_settings()
        interact = DynDnsInteract(config['DynDnsUrl'], config['Email'], validuser, 
                                  validpasswd, config['Hostname'], config['PhantomJS'])
        interact.login()
        self.assertEqual(interact.browser.title, 'My Dyn Account')
        
    def testInvalidLogin(self):
        interact = DynDnsInteract('https://account.dyn.com/entrance/', 'david.alkanani@gmail.com', 'bad', 
                                  'login', 'my.dn.com', '/usr/local/bin/phantomjs')
        with self.assertRaises(InvalidLoginError):
            interact.login()

if __name__ == '__main__':
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()