'''
purpose
	reads data from the stdin: generates shapes depending on the sides
	the shapes are then scaled ,rotated 
	
preconditions
	stdin contains a legal line file
'''

import sys
import copy
import math
import Line_Point



'''
purpose
	convert the lines in stdin to a list of Line objects
	return the list
preconditions
	file_object is a reference to a readable file containing legal lines
'''
def load_line_file(file_object):
	line_objects = [ ]
	for line in file_object:
		# convert text line to a Line object
		line_object = line.split()
		point0 = Line_Point.Point(float(line_object[1]), float(line_object[2]))
		point1 = Line_Point.Point(float(line_object[3]), float(line_object[4]))
		line_object = Line_Point.Line(point0, point1)

		line_objects.append(line_object)

	return line_objects


# ***** process command line arguments

if len(sys.argv) < 2:
	print >> sys.stderr, 'Syntax: ' + sys.argv[0] + ' number_of_sides_in_polygon'
	sys.exit(1)
try:
	number = int(sys.argv[1])
	colour = str(sys.argv[2])
	
except ValueError:
	print >> sys.stderr, 'Syntax: ' + sys.argv[0] + ' number_of_sides_in_polygon'
	sys.exit(2)
if number < 1 or number > 1000:
	print >> sys.stderr, 'Syntax: ' + sys.argv[0] + ' number_of_sides_in_polygon'
	sys.exit(3)

L = load_line_file(sys.stdin)
def draw_shapes(L):

	
	for x in L:
		x.scale(0.99)
		x.rotate(3000.0)
		print 'line', x, colour

for i in range(number):
	draw_shapes(L)
