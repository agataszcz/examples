#!/usr/bin/env python
'''Importing data from websites. Requests package is an alternative to Urllib'''
import requests

r = requests.get('https://api.github.com/events')
#input a url

text = r.text
print(text)
#If you need a json object, use r.json()