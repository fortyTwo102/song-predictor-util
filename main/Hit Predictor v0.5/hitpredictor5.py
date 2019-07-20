import os
import numpy as np
import matplotlib.pyplot as plot
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics, preprocessing
from scipy import stats
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

database = {}

def featureNorm(X):
	mean = []
	std = []

	for i in range(X.shape[1]):
		col = X[:,i]

		mean.append(np.mean(col))
		std.append(np.std(col))

		X[:,i] = (col - np.mean(col))  / np.std(col)

	return X	

def getSongFeatures(trackID):

	client_credentials_manager = SpotifyClientCredentials(client_id='ad3b6e58606c4b1d91832ecd0c160557',client_secret='e3f68c9f1c2b42e5a48a1d61e10fa0ab')
	sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

	data = []
	#FETCHING TRACK NAME AND ARTIST NAME
	try:

		#FETCHING POPULARITY
		respTrack = sp.track(trackID)

		artistID = respTrack['artists'][0]['id']

		respArtist = sp.artist(artistID)
		data.append(respArtist['popularity'])


		#FETCHING AUDIO FEATURES

		respFeature = sp.audio_features(trackID)
		featureFields = list(respFeature[0].keys())

		for key in featureFields:
			if key in {'type','track_href','uri','id','analysis_url'}:
				pass
			else:	
				data.append(respFeature[0][key])
	


		#FETCHING AUDIO ANALYSIS

		respAnalysis = sp.audio_analysis(trackID)
		chorusHit = respAnalysis['sections'][2]['start']
		sections = len(respAnalysis['sections'])
		data.append(chorusHit)
		data.append(sections)
		
	except e:
		print("Error in fetching "+ trackID)
		
		
	return data

def Predict(feature):

	
	data = np.loadtxt('songdatabase1.txt', delimiter='\t')
	
	
	#Removing Outliers
	z = np.abs(stats.zscore(data))
	data = data[(z < 3).all(axis=1)]

	feature = np.array(feature)
	data = np.vstack((data,feature)) #adding the test song


	X, y = data[:, :16], data[:, 16]

	X = featureNorm(X) 
	print(X.shape)
	feature = X[-1,:] #getting the scaled feature

	X = X[:-1,:] #shedding the test song
	y = y[:-1] #shedding the test song

	feature = feature.reshape(-1,feature.shape[0])

	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3, random_state=1)

	model = LogisticRegression(solver='lbfgs')

	model.fit(X_train, y_train)

	#feature = feature.reshape(-1,feature.shape[0])

	

	y_pred = model.predict(feature)

	probability = model.predict_proba(feature)
	print(probability)


	y_pred = y_pred.reshape(y_pred.shape[0],-1)
	y_test = y_test.reshape(y_test.shape[0],-1)


songFeature = getSongFeatures('spotify:track:32bBRB8ozevGWTyhwb0vm0') + [1]

Predict(songFeature)	

#[52, 0.405, 0.793, 0, -5.556, 1, 0.0383, 0.00597, 0.127, 0.117, 0.117, 118.164, 319400, 4, 37.32593, 12]
