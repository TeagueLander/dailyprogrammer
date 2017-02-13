import sys

#Open input file
with open(sys.argv[1]) as f:
	input = f.readlines()

#Parse the input
axis = [int(x) for x in input[0].split()]
columns_len = int(input[1])
columns = [ [y for y in x.split()] for x in input[2:len(input)] ]

#Create a dictionary with keys based on the first value in that row '140'
column_data = {}
for column in columns:
	column_data[str(column[0])] = int(column[2])

x_axis = [x for x in range(axis[0],axis[1] + 1, 10)] # 10 between each
y_axis = [x for x in range(axis[2],axis[3] + 1, 1)] # 1 between each

#Get the length of the highest digit for each axis (needed to append spaces)
x_digit_len = max(len(str(x)) for x in x_axis)
y_digit_len = max(len(str(x)) for x in y_axis)

print "Column data ", column_data
print '' # Gives us a line between our console

for y in reversed(y_axis):

	row_str = ''
	
	for x in [str(x) for x in x_axis]:
	
		cur_row_str_len = len(row_str)
		
		if x in column_data:
			if column_data[x] >= y:
				row_str += '*'.rjust(x_digit_len + 1)
				
		row_str = row_str.ljust(cur_row_str_len + x_digit_len + 1)
		
	print str(y).rjust(y_digit_len) + row_str
	
print ''.rjust(y_digit_len) + ' '.join(str(x).rjust(x_digit_len) for x in x_axis)