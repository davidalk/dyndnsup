'''
Created on 27 Dec 2013

@author: davidal-kanani
'''

from selenium import webdriver
import requests

def main():
    pass

class DynDnsInteract:
    
    phantomjs_bin = '/usr/local/bin/phantomjs'
    
    def __init__(self, url, notify_email, username, passwd):
        self.url = url
        self.notify_email = notify_email
        self.username = username
        self.passwd = passwd
        self.browser = None
        
        
    def login(self):
        # Use requests module to check valid url as
        # selenium webdriver doesn't have this function!
        r = requests.get(self.url)
        r.raise_for_status()
         
        self.browser = webdriver.PhantomJS(DynDnsInteract.phantomjs_bin)
        self.browser.get(self.url)
         
        username = self.browser.find_element_by_name('username')
        password = self.browser.find_element_by_name('password')
        submit = self.browser.find_element_by_name('submit')
         
        username.send_keys(self.username)
        password.send_keys(self.passwd)
        submit.click()
        if self.browser.title != 'My Dyn Account':
            raise InvalidLoginException('Login failed, browser title: ' + self.browser.title)


class InvalidLoginException(Exception):
    
    def __init__(self, message):
        self.message = message

if __name__ == '__main__':
    main()