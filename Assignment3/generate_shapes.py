import sys
import math
import Line_Point


'''
purpose
	write to stdout a regular polygon with s sides and first vertex at (x0,y0)
preconditions
	None
'''
# process the command line arguments
if len(sys.argv) < 3:
	print >> sys.stderr, 'Syntax: ' + sys.argv[0] + ' x0 y0 s'
	sys.exit(1)
try:
	x0 = float(sys.argv[1])
	y0 = float(sys.argv[2])
	s = int(sys.argv[3])
	
	
except ValueError:
	print >> sys.stderr, 'Syntax: ' + sys.argv[0] + ' x0 y0 s'
	sys.exit(2)
if s < 2:
	print >> sys.stderr, 'Syntax: ' + sys.argv[0] + ' x0 y0 s'


def next_Shape(L):
	for x in L:
		
		
		angle= math.pi
		x.scale(0.5)
		x.rotate(angle)

	return L

'''
purpose
	scale, rotate, and print lines 
preconditions

'''
def Draw_Shape(L, n):
	if (n == 0):
		return

	for x in L:
		print 'line', x

	Draw_Shape(next_Shape(L), n-1)



# generate s lines, each rotated by the central angle
sides = 2* math.pi / s
p0 = Line_Point.Point(x0, y0)


L = []
for i in range(s):
	
	p1 = Line_Point.Point(p0.x, p0.y)
	p1.rotate(sides)
	x = Line_Point.Line(p0, p1)
	L.append(x)
	p0 = p1
	

Draw_Shape(L,2)
