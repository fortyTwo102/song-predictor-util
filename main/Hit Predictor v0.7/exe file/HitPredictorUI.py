from tkinter import * 
from PIL import ImageTk, Image
import numpy as np
from sklearn.linear_model import LogisticRegression
from scipy import stats
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

database = {}

trackFetched = "" 
artistFetched = ""

def getSongID(artistName, trackName):

	

	client_credentials_manager = SpotifyClientCredentials(client_id='ad3b6e58606c4b1d91832ecd0c160557',client_secret='e3f68c9f1c2b42e5a48a1d61e10fa0ab')
	sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

	try:
		track = sp.search(q='artist:' + artistName+' track:'+trackName,type='track',limit=1)
		uri = track['tracks']['items'][0]['uri']
		return uri
	except:
		try:
			track = sp.search(q='track:'+trackName,type='track',limit=1)
			uri = track['tracks']['items'][0]['uri']
			return uri
		except:
			print(trackName+ " is not found.")	
	

def featureNorm(X):
	mean = []
	std = []

	for i in range(X.shape[1]):
		col = X[:,i]

		mean.append(np.mean(col))
		std.append(np.std(col))

		X[:,i] = (col - np.mean(col))  / np.std(col)

	return mean, std, X	

def getSongFeatures(trackID):

	global trackFetched
	global artistFetched

	

	client_credentials_manager = SpotifyClientCredentials(client_id='ad3b6e58606c4b1d91832ecd0c160557',client_secret='e3f68c9f1c2b42e5a48a1d61e10fa0ab')
	sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

	data = []
	#FETCHING TRACK NAME AND ARTIST NAME
	try:

		#FETCHING POPULARITY
		respTrack = sp.track(trackID)

		artistID = respTrack['artists'][0]['id']

		artistFetched = respTrack['artists'][0]['name']
		trackFetched =  respTrack['name']

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
		
	except:
		print("Error in fetching "+ trackID)
		
		
	return data

def Predict(feature):
	
	global trackFetched
	global artistFetched

	if len(feature) == 18:
		trackFetched = feature[-2]
		artistFetched = feature[-1]
		feature = feature[:-2]
	
	
	data = np.loadtxt('songdatabase1.txt', delimiter='\t')
	
	#Removing Outliers
	z = np.abs(stats.zscore(data))
	data = data[(z < 3).all(axis=1)]

	X, y = data[:, :16], data[:, 16]

	mean, sigma, X = featureNorm(X)

	feature = np.array(feature)
	mean = np.array(mean)
	sigma = np.array(sigma) 

	feature = (feature - mean) / sigma #getting the scaled feature
	feature = feature.reshape(-1,feature.shape[0])

	#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3, random_state=1)

	model = LogisticRegression(solver='lbfgs')

	model.fit(X, y)

	#feature = feature.reshape(-1,feature.shape[0])

	

	y_pred = model.predict(feature)

	probability = round((model.predict_proba(feature)[0][1])*100,1)
	#print("There's a",probability,"% chance of "+trackFetched + " by "+artistFetched+ " being a hit!")

	return probability, trackFetched, artistFetched

def main(track, artist):

	print("Fetching Track URI from Spotify....",end="")
	spotifyURI = getSongID(artist, track)
	print("Fetched!")
	print("Fetching Track features from Spotify....",end="")
	songFeature = getSongFeatures(spotifyURI)
	print("Fetched!")

	r, t, a = Predict(songFeature)

	return r, t, a	

def getUserData():

	param1 = enterTitle.get()
	param2 = enterArtist.get()
	result, track, artist = main(param1, param2)
	DisplayResults(result, track, artist)

def DisplayResults(result, track, artist):

	label1 = Label(window, text="there's a",bg='white',fg='grey')
	label1.config(font=('Ariel Bold',20))
	label1.place(anchor=CENTER, relx = 0.5, rely=0.51)

	label2 = Label(window, text=str(result)+'%',bg='white',fg='dark green')
	label2.config(font=('Courier',50))
	label2.place(anchor=CENTER, relx = 0.49, rely=0.6)

	label3 = Label(window, text="   chance of \n\n\n  being a hit!",bg='white',fg='grey')
	label3.config(font=('Ariel Bold',20))
	label3.place(anchor=CENTER, relx = 0.49, rely=0.74)

	l = Label(window,text=" "*1000,bg='green')
	l.place(anchor=CENTER, relx = 0.5, rely=0.743)

	label4 = Label(window, text=track+' by '+artist,bg='white',fg='dark green')
	label4.config(font=('Ariel Bold',20))
	label4.place(anchor=CENTER, relx = 0.5, rely=0.743)

def song1(enterTitle, enterArtist, predictButton):
	entry1.set("The Grammarian")
	entry2.set("Tigers On Trains")
	predictButton.config(command=preFetchedPredict1)


def song2(enterTitle, enterArtist, predictButton):
	entry1.set("Let It Be")
	entry2.set("The Beatles")
	predictButton.config(command=preFetchedPredict2)

def preFetchedPredict1():

	preFetched = [

		[12, 0.417, 0.339, 4, -11.463, 1, 0.0275, 0.651, 0.00184, 0.116, 0.119, 80.017, 284855, 4, 67.19927, 9,"The Grammarian", "Tigers On Trains"],
		[86, 0.443, 0.403, 0, -8.339, 1, 0.0322, 0.631, 0, 0.111, 0.41, 143.462, 243027, 4, 26.41694, 15, "Let It Be", "The Beatles"]

	]

	result, tRAck, arTist = Predict(preFetched[0])
	DisplayResults(result, tRAck, arTist)

def preFetchedPredict2():

	preFetched = [

		[12, 0.417, 0.339, 4, -11.463, 1, 0.0275, 0.651, 0.00184, 0.116, 0.119, 80.017, 284855, 4, 67.19927, 9,"The Grammarian", "Tigers On Trains"],
		[86, 0.443, 0.403, 0, -8.339, 1, 0.0322, 0.631, 0, 0.111, 0.41, 143.462, 243027, 4, 26.41694, 15, "Let It Be", "The Beatles"]

	]

	result, tRAck, arTist = Predict(preFetched[1])
	DisplayResults(result, tRAck, arTist)


window = Tk()
window.title("HIT PREDICTOR!")
window.configure(background='white')

entry1 = StringVar()
entry2 = StringVar()

img1 = ImageTk.PhotoImage(Image.open("title.png"))
titleLabel = Label(window, image=img1,bg='white')
titleLabel.place(anchor=CENTER, relx= 0.4, rely=0.21)

img2 = ImageTk.PhotoImage(Image.open("artist.png"))
artistLabel = Label(window, image=img2,bg='white')
artistLabel.place(anchor=CENTER, relx= 0.4, rely=0.28)

img3 = ImageTk.PhotoImage(Image.open("predict2.png"))
predictButton = Button(window)
predictButton.config(image=img3,command=getUserData)
predictButton.place(relx=0.5, rely=0.4, anchor=CENTER)

notice = Label(window, text="click and wait!",bg='white',fg='grey').place(anchor=CENTER, relx=0.75, rely=0.43)

enterTitle = Entry(window,textvariable=entry1)
enterTitle.place(anchor=CENTER, relx= 0.58, rely=0.214)

enterArtist = Entry(window,textvariable=entry2)
enterArtist.place(anchor=CENTER, relx= 0.58, rely=0.284)


q1 = Button(window, text="Prefetched Song #1",command=lambda: song1(enterTitle, enterArtist,predictButton), height=1,width=15)
q1.place(anchor=CENTER, relx=.88, rely=.1)

q1 = Button(window, text="Prefetched Song #2",command=lambda: song2(enterTitle, enterArtist,predictButton), height=1,width=15)
q1.place(anchor=CENTER, relx=.88, rely=.14)



window.geometry("600x700")
window.mainloop()