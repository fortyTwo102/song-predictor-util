import csv

with open('test1.csv',encoding='utf-8') as fp1, open('test3.csv','w',encoding='utf-8',newline="") as fp3:			
	csv_reader1 = csv.reader(fp1)
	
	csv_writer = csv.writer(fp3)

	for row1 in csv_reader1:
		csv_writer.writerow([row1])


with open('test2.csv',encoding='utf-8') as fp2, open('test3.csv','a',encoding='utf-8',newline="") as fp3:
	csv_reader2 = csv.reader(fp2)
	csv_writer = csv.writer(fp3)

	for row2 in csv_reader2:
		csv_writer.writerow([row2])