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


songs = []
#keywords = set(l)

with open("lyricsDBF2.csv",encoding='utf-8') as fp1:
	csv_reader = csv.reader(fp1)
	for row in csv_reader:
		try:
			row = ast.literal_eval(row[0])
			row = list(row)
			setofkeys = set(row[2].split())
			songs.append(setofkeys)
			#print(setofkeys)
		except:
			print("Error")

with open("lyricsDBF.csv",encoding='utf-8') as fp2:
	csv_reader = csv.reader(fp2)
	for row in csv_reader:
		try:
			row = ast.literal_eval(row[0])
			row = list(row)
			setofkeys = set(row[2].split())
			songs.append(setofkeys)
			#print(setofkeys)
		except:
			print("Error")			

with open("lyricSet2.csv",'a+',encoding='utf-8',newline="") as fp3:
	csv_writer = csv.writer(fp3)
	for song in songs:
		song = [x.lower() for x in song]	
		csv_writer.writerow([song])
		