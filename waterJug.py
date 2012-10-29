#Water jug problem in Python
import sys

jugs = [0,0]
queue = []
queue.append(jugs)
over = []
counter = 1
# Rules

X = int(raw_input("Jug 1: "))
Y = int(raw_input("Jug 2: "))
Z = int(raw_input("Final in jug 1: " ))

def Solve(queue, counter):
	jugs = queue.pop(0)
	over.append(jugs)
	#print jugs, queue
	#print counter
	#a = raw_input()
	counter += 1
	if (jugs[0] == Z and jugs[1] == 0):
		print "Solution found!"
		print "Approx count: ", counter
		return
	ApplyRule(jugs, queue)
	Solve(queue, counter)

def Append(queue, temp):
	if not (temp in queue) and not (temp in over):
		queue.append(temp)
	#print "Queue: ", queue
	
def ApplyRule(jugs, queue):
	#print jugs
	x = jugs[0]
	y = jugs[1]
	
	if x < 4: 
		print "Rule 1"
		Append(queue, [X,y])
		
	if y < 3: 
		print "Rule 2"
		Append(queue, [x,Y])
		
	if x > 0: 
		print "Rule 5"
		Append(queue, [0,y])
		
	if y > 0: 
		print "Rule 6"
		Append(queue, [x,0])
	
	if x + y >= X and y > 0: 
		print "Rule 7"
		Append(queue, [X,y-X+x])
		
	#if x + y >= Y and x > 0: 
		#print "Rule 8"
		#Append(queue, [x-Y+y,Y])
		
	if x + y <= X and y > 0: 
		print "Rule 9"
		Append(queue, [x+y,0])
		
	#if x + y <= Y and x > 0: 
		#print "Rule 10"; Append(queue, [0,x+y])
		
	if x == 0 and y == Z: 
		print "Rule 11"
		Append(queue, [Z,0])	
	
Solve(queue, 0)

