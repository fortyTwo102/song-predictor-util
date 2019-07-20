import csv
import ast
import spotipy
from pprint import pprint
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(client_id='ad3b6e58606c4b1d91832ecd0c160557',client_secret='e3f68c9f1c2b42e5a48a1d61e10fa0ab')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

l1 = []
l2 = []
songset1 = set(l1)
songset2 = set(l2)

'''artistName = 'Dr. Dre'
trackName = 'I Need A Doctor'

track = sp.search(q='artist:' + artistName+' track:'+trackName,type='track',limit=1)
pprint(track)'''
#uri = track['tracks']['items'][0]['uri']



with open('billboardDB1.csv','r') as fp:
	csv_reader = csv.reader(fp)
	for rows in csv_reader:
		for row in rows:
			row = ast.literal_eval(row)
			row = tuple(row)
			songset1.add(row)

with open('rhotstuff.csv','r') as fp:
	csv_reader = csv.reader(fp)
	for rows in csv_reader:
		for row in rows:
			row = ast.literal_eval(row)
			row = tuple(row)
			songset2.add(row)

songset3 = songset1.union(songset2)			

with open('billBoardNEW.csv','w+',newline='') as fp1:
	csv_writer = csv.writer(fp1)

	for row in songset3:
		row=list(row)
		csv_writer.writerow([row])		


'''with open('billboardDatabase.csv', 'w+',newline='') as fp:
	csv_writer = csv.writer(fp)
	for each in songset:
		song = list(each)

		trackName = song[0]
		artistName = song[1]

		try:
			track = sp.search(q='artist:' + artistName+' track:'+trackName,type='track',limit=1)
			uri = track['tracks']['items'][0]['uri']
			song.append(uri)
			print(song)
		except:
			try:
				track = sp.search(q='track:'+trackName,type='track',limit=1)
				uri = track['tracks']['items'][0]['uri']
				song.append(uri)
				print(song)
			except:
				print(" by ".join(song) + " is not found.")	
				
		
		csv_writer.writerow([song])

	track = sp.search(q='artist:' + artistName+' track:'+trackName,type='track',limit=1)
		uri = track['tracks']['items']['uri']
		#song.append(uri)'''
	

print("Done!")		


