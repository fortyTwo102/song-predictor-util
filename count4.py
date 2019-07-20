import csv
import ast
import spotipy
from pprint import pprint
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(client_id='ad3b6e58606c4b1d91832ecd0c160557',client_secret='e3f68c9f1c2b42e5a48a1d61e10fa0ab')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

l1 = []
l2 = []
flopTracks = set(l1)
hitTracks = set(l2)

'''artistName = 'Dr. Dre'
trackName = 'I Need A Doctor'

track = sp.search(q='artist:' + artistName+' track:'+trackName,type='track',limit=1)
pprint(track)'''
#uri = track['tracks']['items'][0]['uri']



with open('flopTracks1.csv','r',encoding="utf-8") as fp:
	csv_reader = csv.reader(fp)
	for rows in csv_reader:
		for row in rows:
			row = ast.literal_eval(row)
			row = tuple(row)
			flopTracks.add(row)

print(len(flopTracks))

with open('billBoardNEW.csv','r',encoding="utf-8") as fp:
	csv_reader = csv.reader(fp)
	for rows in csv_reader:
		for row in rows:
			row = ast.literal_eval(row)
			row = tuple(row)
			hitTracks.add(row)


flopTracks -= set(flopTracks.intersection(hitTracks))
print(len(flopTracks))


with open('flopTracks.csv','w+',newline='',encoding="utf-8") as fp1:
	csv_writer = csv.writer(fp1)

	for row in flopTracks:
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


