import csv
import ast

failedTracks = []

with open('failedtracks.csv','r',encoding="utf-8") as fp:
	csv_reader = csv.reader(fp)
	for rows in csv_reader:
		for row in rows:
			row = ast.literal_eval(row)
			row = list(row)
			failedTracks.append(row)

flopTracks = []


with open('flopTracks.csv','r',encoding="utf-8") as fp:
	csv_reader = csv.reader(fp)
	for rows in csv_reader:
		for row in rows:
			row = ast.literal_eval(row)
			row = list(row)
			flopTracks.append(row)

for each in failedTracks:
	for every in flopTracks:
		if [each[0],each[1]] == every:
			every = every.append(each[2])



with open('flopwithuri.csv','w+',newline='',encoding="utf-8") as fp1:
	csv_writer = csv.writer(fp1)

	for row in flopTracks:
		row=list(row)
		csv_writer.writerow([row])		
			