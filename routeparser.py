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

from xml.dom import minidom
from route import Route
from direction import Direction
from location import Location
from decimal import Decimal

class RouteParser(object):

    def __init__(self, file):
        self.file = file

    def parse(self):
        route = Route()

        kmldoc = minidom.parse(self.file)
        placemarks = kmldoc.getElementsByTagName('Placemark')

        for x in xrange(len(placemarks)):
            direction = self.getDirection(placemarks[x])
            route.addDirection(direction)

        return route

    def getDirection(self, placemark):
        speed = self.__getSpeed(placemark)
        latitude = self.__getLatitude(placemark)
        longitude = self.__getLongitude(placemark)
        # name = self.__getName(placemark)

        # print(name)
        # print(speed)
        # print(latitude)
        # print(longitude)

        direction = Direction(Location(latitude, longitude), speed)

        return direction

    def __getSpeed(self, placemark):
       return float(placemark.getElementsByTagName('description')[0].firstChild.data)

    def __getLatitude(self, placemark):
        return Decimal(placemark.getElementsByTagName('coordinates')[0].firstChild.data.split(',')[1])

    def __getLongitude(self, placemark):
        return Decimal(placemark.getElementsByTagName('coordinates')[0].firstChild.data.split(',')[0])

    def __getName(self, placemark):
        return placemark.getElementsByTagName('name')[0].firstChild.data
