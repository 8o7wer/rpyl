import math
import sys
file = open(sys.argv[1],'r')
code = file.read().split()
file.close()

stack = []

def isfloat(x):
	try:
		a = float(x)
	except ValueError:
		return False
	else:
		return True


for s in code:
	if(isfloat(s)):
		stack.insert(0, float(s))
	else:
		if(s == '/'):
			s = 'div'
		if(s == '*'):
			s = 'mult'
		if(s == '-'):
			s = 'sub'
		f = open('functions/'+s+'.f')
		exec(f.read())
		f.close
