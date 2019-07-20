import numpy as np
import os
import csv
import ast
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from pprint import pprint

#database = {'duration','key','mode','time_signature','acousticness','danceability','energy','instrumentalness'
#,'liveness','loudness','valence','tempo','popularity','followers','trackGenre','location','sections','firstSec'}

database = {}
global count
errors = []


def getSongFeatures(trackID):



	client_credentials_manager = SpotifyClientCredentials(client_id='ad3b6e58606c4b1d91832ecd0c160557',client_secret='e3f68c9f1c2b42e5a48a1d61e10fa0ab')
	sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

	
	#FETCHING TRACK NAME AND ARTIST NAME
	try:

		respTrack = sp.track(trackID)
		if 'title' not in database:
			database['title'] = []
			database['title'].append(respTrack['name'])  
		else: 
			database['title'].append(respTrack['name'])

		if 'artist' not in database:
			database['artist'] = []
			database['artist'].append(respTrack['artists'][0]['name'])  
		else: 
			database['artist'].append(respTrack['artists'][0]['name'])

			
		#FETCHING POPULARITY	

		artistID = respTrack['artists'][0]['id']
		respArtist = sp.artist(artistID)

		if 'popularity' not in database:
			database['popularity'] = []
			database['popularity'].append(respArtist['popularity'])
		else:
			database['popularity'].append(respArtist['popularity'])	

		#FETCHING AUDIO FEATURES

		respFeature = sp.audio_features(trackID)
		featureFields = list(respFeature[0].keys())

		for key in featureFields:
			if key in {'type','track_href','uri','id','analysis_url'}:
				pass
			else:	
				if key not in database:
					database[key] = []
					database[key].append(respFeature[0][key])
				else:
					database[key].append(respFeature[0][key])	


		#FETCHING AUDIO ANALYSIS

		respAnalysis = sp.audio_analysis(trackID)
		chorusHit = respAnalysis['sections'][2]['start']
		sections = len(respAnalysis['sections'])

		if 'chorusHit' not in database:
			database['chorusHit'] = []
			database['chorusHit'].append(chorusHit)
		else:
			database['chorusHit'].append(chorusHit)

		if 'sections' not in database:
			database['sections'] = []
			database['sections'].append(sections)
		else:
			database['sections'].append(sections)			
	except:
		print("Error in fetching "+ trackID)
		errors.append(trackID)		
		
	with open("SongFeaturesFlop.csv", 'a',newline='',encoding='utf-8')	as fp:
		csv_writer = csv.writer(fp)
		header = list(database.keys())
		#csv_writer.writerow(header)
		oneRow = []
		for attribute in database:
			oneRow.append(database[attribute][-1])

		try:	
			csv_writer.writerow(oneRow)
		except:
			pass	



	print(str(len(database['title'])) + ') ' + database['title'][-1] + ' by '+ database['artist'][-1] + ' is fetched.')
		


	return database	 
	
	#pprint.pprint(track)
	

#database = pd.read_csv("database.csv")

ID = []

with open('flopwithuri.csv',encoding='utf-8') as fp:
	csv_reader = csv.reader(fp)
	for row in csv_reader:
		try:
			row = ast.literal_eval(row[0])
			ID.append(row[2])
		except:
			pass

'''ids = ['spotify:track:0Ri0LzOMJmqi9HGZE5cRYV','spotify:track:3wx2kQWPn9p5UppQbNhPAk']

for Id in ids:
	getSongFeatures(Id)'''
while True:
	for Id in ID:
		try:
			getSongFeatures(Id)
		except:
			getSongFeatures(Id)


pprint(database)	

	 



