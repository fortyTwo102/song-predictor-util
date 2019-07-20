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

keywords = []
songs = {}

with open("lyricsCount2.csv",encoding='utf-8') as fp:
	csv_reader = csv.reader(fp)
	for row in csv_reader:
		keywords.append(row[0].strip().split()[0])

#all the lyrical keywords are now selected

with open("songfeatures1.csv", encoding='utf-8',errors='ignore') as fp3:
	csv_reader1 = csv.reader(fp3)
	for song in csv_reader1:
		key = (song[0],song[1])
		songs[key] = song[2:]
		 
#all the songs are now in a dictionary 
count = 0
l=[]
with open('lyricsDBF - Copy.csv',encoding='utf-8') as fp2:
	csv_reader = csv.reader(fp2)
	for row in csv_reader:
		try:
			row = ast.literal_eval(row[0])
			row = list(row)
			if len(row) == 3:
				k = (row[0],row[1])
				if k in songs:
					l.append(k)
					count+=1
				else:
					print(k)	
			'''setofkeys = set(row[2].split())
			print(setofkeys.intersection(keywords))'''
			
		except Exception as e:
			if type(e).__name__ == 'SyntaxError':
				pass
			else:
				print("Error!")	 

print(count)