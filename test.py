import csv


d = {'hey':[1,2], 'yo':[6,7], 'Lol':[8,4]}

row = list(d.keys())
oneRow = []
for key in d:
	oneRow.append(d[key][-1])

print(oneRow)	
