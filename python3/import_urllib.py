#!/usr/bin/env python
'''Importing data from websites with Urllib'''

import urllib.request 
#An easier and less wordy alternative is Requests module

url = 'https://www.google.de/'
#specify the url
x = urllib.request.urlopen(url)
print(x.read())
x.close()
#remember to close