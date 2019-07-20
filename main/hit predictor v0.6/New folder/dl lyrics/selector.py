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

keywords = ['i', 'you', 'a', 'me', 'in', 'it', 'my', 'that', 'on', 'of', 'all', 'your', 'be', "i'm", 'for', 'but', 'know', 'just', 'like', 'is', 'with', "don't", 'this', 'when', 'up', 'we', 'what', 'got', 'no', 'get', 'can', 'if', 'love', 'do', 'out', 'now', 'go', 'see', 'one', 'time', 'make', 'down', 'never', 'at', "can't", 'from', 'was', 'take', 'let', 'say', 'not', 'have', 'how', "you're", 'way', 'they', 'want', 'back', 'come', "ain't", 'right', 'wanna', 'are', 'feel', 'need', 'tell', 'been', 'baby', 'yeah', "that's", 'about', 'here', "i'll", 'could', 'then', 'by', 'some', 'think', 'me', 'she', 'will', 'there', 'give', 'more', 'life', 'too', 'keep', 'oh', 'where', 'her', 'yeah', 'through', 'every', 'only', 'night', 'still', 'look', 'had', 'good', 'gonna', 'who', 'girl', 'off', "'cause", 'man', 'day', 'around', 'heart', "i've", 'little', 'them', 'cause', 'put', 'why', 'world', 'said', 'over', 'oh', 'ever', 'even', "won't", 'he', 'would', 'than', 'these', 'away', 'always', 'gotta', "there's", 'mind', 'baby', 'call', 'things', 'an', 'better', 'really', 'long', 'hold', 'eyes', 'new', 'our', 'us', 'real', 'much', 'find', 'show', 'thing', 'made', 'were', 'into', 'nothing', 'turn', 'stop', 'leave', 'home', 'everything', 'up', 'again', 'hard', 'hit', 'before', 'hear', 'something', '&', 'try', 'shit', 'big', 'did', 'another', 'head', 'stay', 'last', 'going', 'should', 'face', 'live', 'ya', 'his', 'two', 'believe', 'run', 'play', "we're", "let's", 'well', 'money', 'bad', 'fuck', 'same', 'left', 'thought', "'em", 'talk', 'told', 'name', 'while', 'gone', 'other', 'first', 'without', 'might', 'boy', 'best', 'old', 'inside', 'done', "i'd", "you'll", 'came', 'light', 'him', 'high', 'break', 'place', 'walk', 'used', 'wrong', "what's", 'people', 'alone', 'start', 'feeling', 'change', 'fall', 'because', 'end', 'enough', 'tonight', 'mine', 'hand', 'looking', 'whole', 'side', 'young', 'bring', "you've", 'hands', 'lost', 'watch', 'move', 'true', 'after', 'work', 'next', "didn't", 'own', 'took', 'knew', 'has', 'seen', 'mean', 'heard', 'body', 'bitch', 'crazy', 'many', 'those', 'friends', 'care', 'please', 'everybody', 'game', 'song', 'black', 'ride', 'coming', 'close']
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
					comm = len(setofkeys.intersection(keywords))
					database[k] = comm
					count+=1
				else:
					print(k)	

			
		except Exception as e:
			if type(e).__name__ == 'SyntaxError':
				pass
			else:
				print("Error!")	 

with open('database.txt', 'w') as f:   
	for key in database.keys():
		print(key,","+str(database[key]),file=f)