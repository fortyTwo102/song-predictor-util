import spotipy
import csv

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(client_id='ad3b6e58606c4b1d91832ecd0c160557',client_secret='e3f68c9f1c2b42e5a48a1d61e10fa0ab')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
tracks = []
def get_playlist_tracks(username,playlist_id):
	tracks = []
	for i in range(16):
		results = sp.user_playlist_tracks(username,playlist_id,offset=i*100)
		for track in results['items']:
			data = [track['track']['name'],track['track']['artists'][0]['name'],
			track['track']['uri']]
			tracks.append(data)

	with open('failedtracks.csv','w+',newline='',encoding="utf-8") as fp1:
		csv_writer = csv.writer(fp1)

		for row in tracks:
			row=list(row)
			try:
				csv_writer.writerow([row])
			except:
				print(row)			

	'''tracks = results['items']
	while results['next']:
		results = sp.next(results)
		print(results['items'][0]['track']['artists'][0]['name'])
		tracks.extend(results['items'][0]['track'])'''
	
	
		

		
print(get_playlist_tracks('oceancitypark97','3W9saC13obO37YgceBA6dg'))

