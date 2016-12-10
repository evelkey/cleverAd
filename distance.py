import numpy as np

def distance(point1, point2):

	deltaX = point2[0] - point1[0]
	deltaY = point2[1] - point1[1]
	return np.sqrt(deltaX*deltaX + deltaY*deltaY)



emberek = ([1,1],[2,2],[3,3],[4,4])
antennak = ([5,5],[3,3])

tavolsag = {}
for ember in emberek:
	distances = []
	for antenna in antennak:
		dist = distance(ember,antenna)
		distances.append(dist)

	print(min(distances))