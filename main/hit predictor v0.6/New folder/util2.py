import sys
import csv
import ast

import requests
import rapidconnect
import lyricsgenius as genius

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


tracks = []

with open('trainLyricsPart1.csv','r',encoding='utf-8',errors='ignore') as fp:
	csv_reader = csv.reader(fp)

	for each in csv_reader:
		try:
			each = ast.literal_eval(each[0])
			each = list(each)
			if len(each) == 2:
				tracks.append(each)
		except:
			pass
			

cred = "0xKM6xBeUYQwPfuumxYDGDxd-1r_RbHev4sWMH2rR-HNAhjjHq9ZZfnAR_Z7L98U"
api = genius.Genius(cred)

error = []

print(tracks)




for row in tracks:
	try:
		while True:
			resp = api.search_song(row[0],row[1])
			try:
				lyrics  = resp.lyrics
				row.append(lyrics)
				break
			except:
				lyrics = "NOTXFOUNDX"
				row.append(lyrics)
				break	

	except:
		error.append(row)		
	
	try:
		with open("trainLyricsPart1.csv",'a',encoding="utf-8",newline='') as fp:
			csv_writer = csv.writer(fp)
			csv_writer.writerow([row])
	except:
		error.append(row)
			
	
print("KHATAM!",error)	

	

		

	
