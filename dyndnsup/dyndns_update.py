'''
Created on 27 Dec 2013

@author: davidal-kanani
'''

import requests
from bs4 import BeautifulSoup
import re

def main():
    pass

class DynDnsInteract:
    
    def __init__(self, url, notify_email):
        self.url = url
        self.notify_email = notify_email
        
    def login(self):
        r=requests.get(self.url)
        r.raise_for_status()

if __name__ == '__main__':
    main()