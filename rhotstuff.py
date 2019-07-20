import csv

l = []
with open('hotstuff.csv') as fp:
	csv_reader = csv.reader(fp)

	for row in csv_reader:
		l.append(row)


reduced = l[166500:]
entry = []
for row in reduced:
	entry.append([row[1],row[2]])

with open("realhotstuff.csv","w+",newline='') as fp:
	csv_writer = csv.writer(fp)

	for row in entry:
		csv_writer.writerows([row])		