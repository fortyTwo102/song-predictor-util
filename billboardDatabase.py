import billboard
import csv
import pandas as pd

def getChartOf(weekOf):
	chart = billboard.ChartData('hot-100', weekOf)
	charts = []

	with open('billboardNEWDB.csv', 'w+', newline='') as csv_file:
		csv_writer = csv.writer(csv_file)
		date = str(chart.date)
		charts.append(date)
		for song in chart.entries:
			charts.append([song.title, song.artist])

		csv_writer.writerows([charts])



def allsaturdays(year):
    return pd.date_range(start='1990-01-06', end='2019-03-30', 
                         freq='7D').strftime('%Y-%m-%d').tolist()

saturdays = allsaturdays(1990)


while True:
	for saturday in saturdays:
		print(saturday)
		try:
			getChartOf(saturday)
		except:
			getChartOf(saturday)

	print("DONE!")
	break			
			