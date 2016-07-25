# Route Simulator
Simulates a real gps route from waypoints file (CSV/KML) and exports it into outfile (CSV/KML)

# How to use
First we need to create a kml file with google maps (MyMaps), google earth or some kml editor and add *Placemarks* 
with the desired speed in their description.

After we can use this file as input and execute the next command:
`routesimulator.py [-h] [-o OUTPUT] [-t {kml,csv}] [-n NOISE] [-s STEP] input`

* `input` This is the input file. Must be a valid kml file with *placemarks*. 
          The description of this *placemarks* must be the *speed* between points.
          
* `-o OUTPUT, --output OUTPUT` This is the output filename.

* `-t {kml,csv}, --type {kml,csv}` This is the type of the output file.

* `-n NOISE, --noise NOISE` This is the noise to add in the output *placemarks*.
                            Increment this to disturb the route.
                            Must be a positive integer.

*  `-s STEP, --step STEP` This is the step multiplier of route. 
                          Increment this to do faster route.
                          Must be a positive integer.
