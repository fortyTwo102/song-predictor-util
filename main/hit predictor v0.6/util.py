import csv
import ast
from acrcloud.recognizer import ACRCloudRecognizer
import requests
import rapidconnect
import lyricsgenius as genius

tracks = []

with open('billBoardNEW.txt','r',encoding='utf-8',errors='ignore') as fp:
	csv_reader = csv.reader(fp)

	for each in csv_reader:
		try:

			each = ast.literal_eval(each[0])
			each = list(each)
			tracks.append([each[0],each[1]])
		except:
			pass	

cred = "HmWgG6G-hjQvyberqpyPGT9rYXFYRwDYJmVSE3y-pFoJMTv7Rug37vuBuUzIa_gX"
api = genius.Genius(cred)

error = []

for row in tracks[1080:5500]:
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
		with open("lyricsDBF.csv",'a+',encoding="utf-8",newline='') as fp:
			csv_writer = csv.writer(fp)
			csv_writer.writerow([row])
	except:
		pass
			
	
print("KHATAM!")	

	

		

	
