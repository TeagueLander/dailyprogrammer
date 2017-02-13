import sys;
import csv;

with open('ptdata2.csv') as f:
	reader = csv.reader(f)
	element_list = list(reader)

for row in element_list:
	print row


def elementify(i_string):

	strlen = len(i_string)

	for i in range(1, strlen):
		part1 = i_string[0:i]
		part2 = i_string[i:strlen]
		
		print part1
		print part2
		print " "
		
		
elementify("hello")