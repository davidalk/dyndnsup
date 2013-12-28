'''
Created on 27 Dec 2013

@author: davidal-kanani
'''

from selenium import webdriver
import requests

def main():
    pass

class DynDnsInteract:
    
    phantomjs_bin = "/usr/local/bin/phantomjs"
    
    def __init__(self, url, notify_email, username, passwd):
        self.url = url
        self.notify_email = notify_email
        self.username = username
        self.passwd = passwd
        self.browser = None
        
        
    def login(self):
        # User requests to check valid url as
        # selenium doesn't have this function!
        r=requests.get(self.url)
        r.raise_for_status()
        
        self.browser = webdriver.PhantomJS(DynDnsInteract.phantomjs_bin)
        self.browser.get(self.url)


if __name__ == '__main__':
    main()