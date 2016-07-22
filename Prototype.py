from math import radians, cos, sin, asin, sqrt
from random import randint

def haversine(point1, point2):
	lon1 = point1['lon']
	lat1 = point1['lat']
	lon2 = point2['lon']
	lat2 = point2['lat']

	# Convert decimal degrees to radians 
	lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

	# Haversine formula 
	dlon = lon2 - lon1 
	dlat = lat2 - lat1 
	a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
	c = 2 * asin(sqrt(a)) 
	r = 6371000 # Radius of earth in meters. Use 3956 for miles
	return c * r

def doRoute(vectorList):
	routeList = []
	
	for x in xrange(len(vectorList)-1):
		v1 = vectorList[x]
		v2 = vectorList[x+1]
		routeList += route(v1['point'],v2['point'],v1['speed'])
		
	return routeList
	
	
def route(point1, point2, speed):
	d = haversine(point1, point2)
	nSteps = d / speed
	
	dStepLon = (point2['lon'] - point1['lon']) / nSteps
	dStepLat = (point2['lat'] - point1['lat']) / nSteps

	routeList = []
	
	for x in xrange(int(nSteps)):
		rLon = (x+1) * dStepLon + point1['lon']
		rLat = (x+1) * dStepLat + point1['lat']
		routeList.append([rLat,rLon])
	
	return routeList

def doNoise(points, noise):
	nPoints = []
	
	for x in xrange(len(points)):
		nPoints.append(addNoise(points[x], noise))
	
	return nPoints

def addNoise(point, noise):
	nPoint = []
	
	nPoint.append(point[0] + randomNoise(noise))
	nPoint.append(point[1] + randomNoise(noise))
	
	return nPoint
	
def randomNoise(noise):
	if randint(0,2):
		z = -1
	else:
		z = 1
	
	rNoise = (randint(0,noise) / 1000000.0) * z
	
	return rNoise
	
def routePrint(routeList):
	for x in xrange(len(routeList)):
		print("{0},Step,{1},{2}").format(x,routeList[x][0],routeList[x][1])
	
	
def main():
	vectors =[
	{'point':{'lat':41.967782,'lon':2.837736},'speed':1.3},
	{'point':{'lat':41.967691,'lon':2.837481},'speed':0.1},
	{'point':{'lat':41.967657,'lon':2.837486},'speed':1},
	{'point':{'lat':41.967175,'lon':2.836808},'speed':1.3},
	{'point':{'lat':41.967418,'lon':2.836306},'speed':0}
	]
	
	routeList = doRoute(vectors)
	nRouteList = doNoise(routeList,20)
	routePrint(nRouteList)

if __name__ == "__main__":
	main()
