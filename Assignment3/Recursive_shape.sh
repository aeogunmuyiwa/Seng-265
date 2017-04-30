# process command line arguments, if agv is not 3 print error message
if [ $# -ne 3 ]; then
	echo "Syntax: bash Recursive_shape.sh  sides colour number"
	exit
fi


sides=$1
colour=$2
number=$3

#generate the shapes at (150,150) vertex and  user specified sides
python generate_shapes.py 150 150 $sides > Shapes.txt
python rotate_scale_translate.py -x 0.0 -y 0.0 -f 1.0 -n 1 <Shapes.txt > Shapes_1.txt


#generate the recursive shapes with user specied number of recursion and colour
python Recursive_shape.py $number $colour < Shapes.txt > Shapes_done.txt
python lines_to_svg_colour.py Shapes_done.txt > Shapes_done.svg
