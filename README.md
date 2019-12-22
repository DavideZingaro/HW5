# Homework 5 - Explore California and Nevada with graphs

![alt text](https://camo.githubusercontent.com/ae26f5178a3c7d279181fcc5a36c00269462732a/68747470733a2f2f31696763306f6a6f73736134313268316533656b386431772d7770656e67696e652e6e6574646e612d73736c2e636f6d2f77702d636f6e74656e742f75706c6f6164732f323031382f30332f393738303932313333383339302e6a7067 "Logo Title Text 1" )


This repository contains:

* `func_1.py`: suggested python file that contains functions for Functionality 1 
* `func_2.py`: suggested python file that contains functions for Functionality 2 
* `func_3.py`: suggested python file that contains functions for Functionality 3 
* `func_4.py`: suggested python file that contains functions for Functionality 4 and Visualization 1, 3, 4.
* `main.py`: the main python file.

## func_1
In this file there are the functions to perform the functionality 1 task. Here we find all the nodes which distance is equal or lower than a starting node; these nodes can be adjacent or not to the initial one.
## func_2
## func_3
In this file there are the functionds to perform the functionality 3 task. Here we find the shortest ordered route from a starting node **H** and a succession of ordered nodes **p = [p_1, ..., p_n]**. To complete this exercise, we divided it into **n** sub-problems, performing the shortest route between two consecutive nodes and then linking them. We implemented the solution following the Dijkstra method.
## func_4
In this file there are the functions to read the .gz files and save them in the networkx.Graph() format and the function to save the coordinates in a dictionary.

In order to find the best route we used a variant of the Nearest Neighbor Algorithm performed on a completely connected graph in which the weights of the edges are the distances as the crow flies between the vertices.

Instead of starting from the initial node and looking for the one closest to it and then repeating the procedure, we decided to start from both the initial and the final nodes. We alternated the search for the nearest node first looking for the one closest to the initial node and then to the final one and repeating again until the end of the nodes.

In this way the maximum distance as the crow flies is much lower than the classic approach.
in addition we repeat the porcesso both for
\[initial, near initial, ..., near final, final\] and also for \[final, near final, ..., near initial, initial\]: and we take the one with the shortest distance (obviously in the case of the second we invert it) . 

Once the correct order of the nodes has been found, the problem of func_3 returns.
This file also contains the function for plot the points on a map. It was made with the folium library. 

The initial and final vertices are in green and red respectively, the vrtices desired by the user in blue and the intermediate vertices are always darker in color from the beginning to the end.

The map is saved in the folder and automatically opened in the browser.
