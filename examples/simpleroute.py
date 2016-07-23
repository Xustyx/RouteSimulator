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

from route import Route
from direction import Direction
from location import Location
from routemanager import RouteManager
from utils import *
import json


def as_direction(dct):
    return Direction(Location(dct['latitude'],dct['longitude']), dct['speed'])

def main():
    route = Route() # Creamos un objeto ruta

    # JSON con vectores de pruebas
    jDirections = [
        '{"latitude": 41.967782, "longitude": 2.837736, "speed": 1.3}',
        '{"latitude": 41.967691, "longitude": 2.837481, "speed": 0.1}',
        '{"latitude": 41.967657, "longitude": 2.837486, "speed": 1}',
        '{"latitude": 41.967175, "longitude": 2.836808, "speed": 1.3}',
        '{"latitude": 41.967418, "longitude": 2.836306, "speed": 0}'
    ]

    # Anadimos a la ruta
    for x in xrange(len(jDirections)):
        direction = json.loads(jDirections[x], object_hook = as_direction)
        route.addDirection(direction)

    # Creamos un manager con la ruta
    routeMgr = RouteManager(route)

    # Generamos las ubicaciones exportandolas a kml y csv.
    locations = routeMgr.applyEffects()
    exportXml(locations, "std-test.kml")
    exportCsv(locations, "std-test.csv")

    # Anadimos multiplicador de pasos y exportamos
    routeMgr.stepMultiplier = 4
    locations = routeMgr.applyEffects()
    exportXml(locations, "step-test.kml")
    exportCsv(locations, "step-test.csv")

    # Anadimos ruido y exportamos
    routeMgr.noise = 20
    locations = routeMgr.applyEffects()
    exportXml(locations, "step-noise-test.kml")
    exportCsv(locations, "step-noise-test.csv")

    # Quitamos multiplicador y dejamos solo ruido
    routeMgr.stepMultiplier = 0
    locations = routeMgr.applyEffects()
    exportXml(locations, "noise-test.kml")
    exportCsv(locations, "noise-test.csv")

if __name__ == "__main__":
    main()
