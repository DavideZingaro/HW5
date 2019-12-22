# HW5
this repository contain:

* `func_1.py`: suggested python file that contains functions for Functionality 1 
* `func_2.py`: suggested python file that contains functions for Functionality 2 
* `func_3.py`: suggested python file that contains functions for Functionality 3 
* `func_4.py`: suggested python file that contains functions for Functionality 4 and Visualization 3, 4.
* `main.py`: the main python file.

## func_1
In this file there are the functions to perform the functionality 1 task. Here we find all the nodes which distance is equal or lower than a starting node; these nodes can be adjacent or not to the initial one.
## func_2
## func_3
In this file there are the functionds to perform the functionality 3 task. Here we find the shortest ordered route from a starting node **H** and a succession of ordered nodes **p = [p_1, ..., p_n]**. To complete this exercise, we divided it into **n** sub-problems, performing the shortest route between two consecutive nodes and then linking them. We implemented the solution following the Dijkstra method.
## func_4
In this file there are the functions to read the .gz files and save them in the networkx.Graph () format and the function to save the coordinates in a dictionary.
In order to find the best route we used a variant of the Nearest Neighbor Algorithm performed on a completely connected graph in which the weights of the edges are the distances as the crow flies between the vertices.
Instead of starting from the initial node and looking for the one closest to it and then repeating the procedure, we decided to start from both the initial and the final nodes. We alternated the search for the nearest node first looking for the one closest to the initial node and then to the final one and repeating again until the end of the nodes.
In this way the maximum distance as the crow flies is much lower than the classic approach.
Once the correct order of the nodes has been found, the problem of func_3 returns.
This file also contains the display of points on the map. It was made with the folium library. The initial and final vertices are in green and red respectively, the vrtices desired by the user in blue and the intermediate vertices are always darker in color from the beginning to the end.
The map is saved in the folder and automatically opened in the browser.
