import csv;

with open('ptdata2.csv') as f:
	reader = csv.reader(f)
	element_list = list(reader)
	del element_list[0]

def elementify(i_string):

	strlen = len(i_string)
	elements = []

	if strlen <= 2:
		for element in element_list:
			# print "Checking element ", element[1], " against ", i_string
			if (i_string == element[1].lower().strip()):
				# print "Got element ", element
				return [element]
		return None
	
	for i in range(1, strlen):
		part1 = i_string[0:i]
		part2 = i_string[i:strlen]
		
		result1 = elementify(part1)
		result2 = elementify(part2)
		
		if result1 == None or result2 == None:
			continue
			
		for element in result2:
			result1.append(element)
			
		return result1

def print_elementified(i_elements):
	element_symbols = []
	element_names = []
	
	if (type(i_elements) is list):
		for element in i_elements:
			element_symbols.append(element[1].strip())
			element_names.append(element[2].strip())
		print ''.join(element_symbols), " (", ', '.join(element_names), ")"
	else:
		print "Not able to build word!"
	
	
while True:
	string_input = raw_input("Type in a word:")
	result = elementify(string_input)
	print_elementified(result)




