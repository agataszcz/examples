#!/usr/bin/env python
'''Read and write a string as a file-like object.'''

from sklearn.externals.six import StringIO

# create a sample
mysample = StringIO()
mysample.write('My first testing line.')
print(mysample) #this only will indicate the location of the file in the memory

# retrieve contents using getvalue()
content = mysample.getvalue()
print(content)

# close my sample
mysample.close()