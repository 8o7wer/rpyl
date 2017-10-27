import math
import sys
file = open(sys.argv[1],'r')
code = file.read().split()
file.close()

stack = []

for s in code:
	if(s == "+"):
		stack.insert(0, stack[0] + stack[1])
		for i in range(0,2):
			del stack[1]
	elif(s == "-"):
		stack.insert(0,stack[1] - stack[0])
		for i in range(0, 2):
			del stack[1]
        elif(s == "*"):
                stack.insert(0, stack[0] * stack[1])
                for i in range(0,2):
                        del stack[1]
        elif(s == "/"):
                stack.insert(0, stack[1] / stack[0])
                for i in range(0,2):
                        del stack[1]
        elif(s == "**"):
                stack.insert(0, stack[0] ** stack[1])
                for i in range(0,2):
                        del stack[1]
        elif(s == "sqrt"):
                stack.insert(0, math.sqrt(stack[0]))
                del stack[1]

	elif(s == "print"):
		print(stack)
	else:
		stack.insert(0, float(s))
