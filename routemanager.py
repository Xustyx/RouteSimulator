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

class RouteManager(object):

    def __init__(self, route, noise = 0, stepMultiplier = 1):
        self.route = route
        self.noise = noise
        self.stepMultiplier = stepMultiplier

    def applyEffects(self):
        locations = self.__doStepsMultiplier()
        locations = self.__doNoise(locations)
        return locations

    def __doNoise(self, locations):
        nLocations = locations

        if self.noise != 0:
            nLocations = []
            for x in xrange(len(locations)):
                nLocations.append(locations[x].noise(self.noise))

        return nLocations

    def __doStepsMultiplier(self):
        if self.stepMultiplier <= 0:
            self.stepMultiplier = 1

        return self.route.getLocations(self.stepMultiplier)

    def routePrint(self):
        locations = self.applyEffects()

        for x in xrange(len(locations)):
            print("{0},Step,{1},{2}").format(x, locations[x].latitude, locations[x].longitude)