import glob
import os
import sys

try:
    sys.path.append(glob.glob('/opt/carla-simulator/PythonAPI/carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass


import carla

import argparse
import datetime
import re
import socket
import textwrap

if __name__ == "__main__":

    #read the map
    osm_map = open("map.osm", "r")
    osm_data = osm_map.read()
    osm_map.close()

    #convert to xodr
    settings = carla.Osm2OdrSettings()
    xodr_data = carla.Osm2Odr.convert(osm_data, settings)

    #write xodr file
    xodr_map = open("gardonyi_xodr.xodr", 'w')
    xodr_map.write(xodr_data)
    xodr_map.close()