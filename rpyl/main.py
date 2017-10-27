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
		f = open("functions/"+s)
		exec(f.read())
		f.close
