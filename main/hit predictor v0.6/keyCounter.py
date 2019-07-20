import sys
import csv
import ast

maxInt = sys.maxsize
decrement = True

while decrement:
    # decrease the maxInt value by factor 10 
    # as long as the OverflowError occurs.

    decrement = False
    try:
        csv.field_size_limit(maxInt)
    except OverflowError:
        maxInt = int(maxInt/10)
        decrement = True


d = {}

with open("lyricSet2.csv",encoding='utf-8') as fp:
	csv_reader = csv.reader(fp)
	for row in csv_reader:
		row = ast.literal_eval(row[0])
		row = set(row)

		for word in row:
			if word not in d:
				d[word] = 1
			else:
				d[word] += 1	

for key, value in sorted(d.items(), key=lambda x: x[1],reverse=True):
	try:
		print(key,value)			
	except:
		print("error")