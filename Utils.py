#The MIT License (MIT)
#
#Copyright (c) 2016 Xustyx
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

from math import radians, cos, sin, asin, sqrt
from random import randint
import simplekml
import csv

def haversine(location1, location2):
    lon1 = location1.longitude
    lat1 = location1.latitude

    lon2 = location2.longitude
    lat2 = location2.latitude

    # Convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # Haversine formula
    dLon = lon2 - lon1
    dLat = lat2 - lat1
    a = sin(dLat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dLon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371000  # Radius of earth in meters. Use 3956 for miles
    return c * r


def randomNoise(noise):
    if randint(0, 2):
        z = -1
    else:
        z = 1

    rNoise = (randint(0, noise) / 1000000.0) * z

    return rNoise

def exportXml(locations, filePath = "export.kml"):
    kml = simplekml.Kml()

    for x in xrange(len(locations)):
        location = locations[x]
        kml.newpoint(name=str(x),coords=[(location.longitude,location.latitude)])

    #print(kml.kml())
    kml.save(filePath)

def exportCsv(locations, filePath = "export.csv"):
    oFile = open(filePath, "wb")
    writer = csv.writer(oFile,delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(["Step","latitude","longitude"])

    for x in xrange(len(locations)):
        location = locations[x]
        writer.writerow([x,location.latitude,location.longitude])

    oFile.close()


