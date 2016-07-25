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

import argparse
from routeparser import RouteParser
from routemanager import RouteManager
from utils import *

def check_negative(value):
    iValue = int(value)
    if iValue < 0:
         raise argparse.ArgumentTypeError("%s is an invalid positive int value" % value)
    return iValue

def get_args():
	parser = argparse.ArgumentParser(
		description="Simulates a real gps route from waypoints file (CSV/KML) and exports it into outfile (CSV/KML)")

	parser.add_argument(
		"input", type=argparse.FileType('r'), help="the input filename")
	parser.add_argument(
		"-o","--output", type=str ,help="the output filename")
	parser.add_argument(
		"-t","--type", type=str, choices=["kml","csv"], default="kml", help="the output file format")
	parser.add_argument(
		"-n","--noise", type=check_negative, default=0, help="the noise of route")
	parser.add_argument(
		"-s","--step", type=check_negative, default=0, help="the step multiplier of route")

	return parser.parse_args()

def main(args):
	routeParser = RouteParser(args.input)
	route =routeParser.parse()

	routeManager = RouteManager(route, args.noise, args.step)
	locations = routeManager.applyEffects()
	# routeManager.routePrint()

	if(args.type == "kml"):
		exportXml(locations, args.output)
	else:
		exportCsv(locations, args.output)


if __name__ == "__main__":
	args = get_args()
	main(args)