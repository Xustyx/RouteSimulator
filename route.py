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

from path import Path

class Route(object):

    def __init__(self, paths = None):
        self.paths = paths

    def addDirection(self, direction):
        if self.paths == None:
            self.paths = []
            self.paths.append(Path(direction.location,direction.speed,None))
        else:
            self.paths[len(self.paths) - 1].setEnd(direction.location)
            self.paths.append(Path(direction.location,direction.speed,None))

    def getLocations(self, stepMultiplier = 1):
        locations = []

        for x in xrange(len(self.paths)):
            pLocations = self.paths[x].locations
            for y in xrange(len(pLocations)):
                if y % stepMultiplier == 0:
                    locations.append(pLocations[y])

        return locations