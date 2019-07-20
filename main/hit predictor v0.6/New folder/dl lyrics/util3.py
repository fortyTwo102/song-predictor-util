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

keywords = ['you','a','me','in','it','my','on','all','your','be','for','know','just','like','is','with',"don't",'this','when','up','we','what','got','no','can','love','out','go','one','down',"can't",'take','say','how',"you're",'back',"ain't",'wanna','some','too','night','good','around',"we're","let's","em'",'tonight','of','at','&','that','but','get','if','now','see','make','never','was','way','right',"that's",'about','real','stop',"didn't",'do','time','let','want','come','feel','need','tell','baby','gonna','girl','heart',"you'll",'think','give','keep','off',"won't","there's",'really',"what's","you've",'ride',"i'm",'shit','ya','oh','gotta','hit','bitch','crazy',"'cause'",'fuck','yeah',"i'd","i've"]
songs = {}
database = {}
rank = {}

#all the lyrical keywords are now selected

with open("songfeatures1.csv", encoding='utf-8',errors='ignore') as fp3:
	csv_reader1 = csv.reader(fp3)

	for song in csv_reader1:
		key = (song[0],song[1])
		songs[key] = song[2:]
	
		 
#all the songs are now in a dictionary 
count = 0
with open('trainLyricsPart2 - Copy.csv',encoding='utf-8') as fp2:
	csv_reader = csv.reader(fp2)
	for row in csv_reader:
		try:
			row = ast.literal_eval(row[0])
			row = list(row)
			if len(row) == 3:
				k = (row[0],row[1])
				if k in songs:										
					setofkeys = set(row[2].split())			
					songs[k].insert(-1,str(len(setofkeys.intersection(keywords))))
										
				else:
					print(k)	

			
		except Exception as e:
			if type(e).__name__ == 'SyntaxError':
				pass
			else:
				pass	 

songfeat = []

for key in songs.keys():
	song = list(key) + songs[key]
	songfeat.append(song)

with open('newSongfeat1.csv','w',encoding='utf-8',newline='') as fp:
	csv_writer = csv.writer(fp)
	for song in songfeat:
		csv_writer.writerow(song)

