#Water jug problem in Python
import sys

jugs = [0,0]
queue = []
queue.append(jugs)
over = []
counter = 1
# Rules

J1 = int(raw_input("Jug 1: "))
J2 = int(raw_input("Jug 2: "))
rem = int(raw_input("Final in jug 1: " ))

def Solve(queue, counter):
	jugs = queue.pop(0)
	over.append(jugs)
	#print jugs, queue
	#print counter
	#a = raw_input()
	counter += 1
	if (jugs[0] == rem and jugs[1] == 0):
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
	
	if x < J1: 
		print "Rule 1"
		Append(queue, [J1,y])
		
	if y < J2: 
		print "Rule 2"
		Append(queue, [x,J2])
		
	if x > 0: 
		print "Rule 5"
		Append(queue, [0,y])
		
	if y > 0: 
		print "Rule 6"
		Append(queue, [x,0])
	
	if x + y >= J1 and y > 0: 
		print "Rule 7"
		Append(queue, [J1,y-J1+x])
		
	#if x + y >= J2 and x > 0: 
		#print "Rule 8"
		#Append(queue, [x-J2+y,J2])
		
	if x + y <= J1 and y > 0: 
		print "Rule 9"
		Append(queue, [x+y,0])
		
	#if x + y <= J2 and x > 0: 
		#print "Rule 10"; Append(queue, [0,x+y])
		
	if x == 0 and y == rem: 
		print "Rule 11"
		Append(queue, [rem,0])	
	
Solve(queue, 0)

