# TURMU
Collaboration with Carlos Hidalgo @ Tecnalia

##Create osm map for carla simulator
1. Copy `osm_to_xodr.py` to the carla `PythonAPI/util` folder.
2. Copy the `map.osm` file to the same folder.
3. Replace the first parameter (filename) of the `open` function in line 25
4. Save and run the `osm_to_xodr.py`

Note: you probably need root privilages to complete the above steps.

The xodr file should be ready at this point.