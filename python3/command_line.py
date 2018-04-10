#!/usr/bin/env python
import sys
'''
Command line parameters (setting up and flagging errors)
'''
def greeting(name):
	print("Hello " + name)


if __name__ == "__main__":

	#print(sys.argv)
	#print(len(sys.argv))

	if len(sys.argv) == 2:
		greeting(sys.argv[1])
	#Note: sys.argv[0] always refers to the program's location

	if len(sys.argv) < 2: 
		print("Error: Missing parameter.")
		sys.exit(1)

	if len(sys.argv) > 2:
		greeting(sys.argv[1])
		print("Warning: The following parameters have been ignored: {}".format(sys.argv[2:]))