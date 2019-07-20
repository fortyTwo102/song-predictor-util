import csv
import ast
from acrcloud.recognizer import ACRCloudRecognizer
import requests
import rapidconnect
import lyricsgenius as genius

tracks = []

with open('songfeatures1.csv','r',encoding='utf-8',errors='ignore') as fp:
	csv_reader = csv.reader(fp)

	for each in csv_reader:
		try:
			tracks.append([each[0],each[1]])
		except:
			pass	

cred = "0xKM6xBeUYQwPfuumxYDGDxd-1r_RbHev4sWMH2rR-HNAhjjHq9ZZfnAR_Z7L98U"
api = genius.Genius(cred)

error = []
print(tracks)



for row in tracks:
	try:
		resp = api.search_song(row[0],row[1])
		try:
			lyrics  = resp.lyrics
			row.append(lyrics)
		except:
			lyrics = "NOTXFOUNDX"
			row.append(lyrics)	

	except:
		try:
			resp = api.search_song(row[0],row[1])
			try:
				lyrics  = resp.lyrics
				row.append(lyrics)
			except:
				lyrics = "NOTXFOUNDX"
				row.append(lyrics)
		except:
			error.append(row)		
	
	
	try:
		with open("trainLyrics1.csv",'a+',encoding="utf-8",newline='') as fp:
			csv_writer = csv.writer(fp)
			csv_writer.writerow([row])
	except:
		pass
			
	
print("KHATAM!")	

	

		

	
