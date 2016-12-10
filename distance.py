import numpy as np
from itertools import groupby

def distance(point1, point2):

	deltaX = point2[0] - point1[0]
	deltaY = point2[1] - point1[1]
	
	return np.sqrt(deltaX*deltaX + deltaY*deltaY)


def binding(emberek,antennak):

	asd = []
	for ember in emberek:
		distances = []
		for antenna in antennak:
			dist = distance(ember,antenna)
			distances.append(dist)
		asd.append(antennak[distances.index(min(distances))])
	
	return asd



def makeCluster(data):
	return [len(list(group)) for key, group in groupby(data)]




def test():
    emberek = ([1,1],[2,2],[3,3],[4,4])
    antennak = ([5,5],[3,3])
    data = binding(emberek,antennak)
    print(makeCluster(data))




