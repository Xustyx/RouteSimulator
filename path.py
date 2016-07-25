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

from location import Location

class Path(object):

    def __init__(self, start, speed, end = None):
        self.start = start
        self.speed = speed
        self.setEnd(end)

    def setEnd(self, end):
        self.end = end
        self.__doPath()

    def __doPath(self):
        locations = []

        locations.append(self.start)

        if self.end is not None:
            d = self.start.distance(self.end)
            nSteps = int(d / self.speed)

           # print(d)
           # print(nSteps)

            if nSteps > 0:
                dStepLon = (self.end.longitude - self.start.longitude) / nSteps
                dStepLat = (self.end.latitude - self.start.latitude) / nSteps

                for x in xrange(int(nSteps) - 1):
                    rLon = (x + 1) * dStepLon + self.start.longitude
                    rLat = (x + 1) * dStepLat + self.start.latitude
                    nLocation = Location(rLat,rLon)
                    locations.append(nLocation)

        self.locations = locations