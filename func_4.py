# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 11:23:01 2019

@author: franc
"""

# importing libraries
import numpy as np
import networkx as nx
import gzip
from itertools import islice
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from itertools import combinations 
from scipy.spatial import distance
from func import f3


# path for read files
path = 'C:/Users/franc/Desktop/Data_science/Algorithmic_Methods_of_Data_Mining/ADM_hw5/'


# the three func to built the graphs take as argument a nx.Graph()
# we are going to create the graph with the distance in meters
def d(graph):
    with gzip.open(path + "distance.gz", "r") as f:
        for line in islice(f, 7, None):
            r, s, t  = map(int, line[2:].split())
            graph.add_edge(r, s, weight = t)
    return graph

# we are going to create the graph with the time distance
def t(g):
    with gzip.open(path + "time_travel.gz", "r") as f:
        for line in islice(f, 7, None):
            r, s, t  = map(int, line[2:].split())
            g.add_edge(r, s, weight = t)
    return g

# we are going to create the graph with the dnetwork distance
def n(g):
    with gzip.open(path + "distance.gz", "r") as f:
        for line in islice(f, 7, None):
            r, s, t  = map(int, line[2:].split())
            g.add_edge(r, s, weight = 1)
    return g

# we are going to save all the coordinates into a dictionary in this form
'''
coord = {node_1 : (long, lat),
         node_2 : (long, lat),
         .
         .
         .}
'''
def coordinates(coord):
    with gzip.open(path + "coordinates.gz", "r") as f:
        for line in islice(f, 7, None):
            x = line[2:].split()
            r, s, t  = int(x[0]), float(x[1])/10**6, float(x[2])/10**6
            coord[r] = (s, t)
    return coord


# this is the function to find the heuristic solution for this problem
# take as argument a fully connecteg graph where the weights are the eucledian distances
# between the nodes
# to find the best path we use the a kind of Nearest Neighbour Algorithm    
def shortest_path_l_r(dcf_graph, start, end):    
    visited = [start, end]
    tot_dist = 0
    while len(visited) < len(dcf_graph):
        min_dist = np.inf
        near = 0
        for k,v in dcf_graph[visited[len(visited)//2 - 1]].items():
            if k not in visited:
                if v < min_dist:
                    min_dist = v
                    near = k
        visited.insert(len(visited)//2, near)
        tot_dist += min_dist
        min_dist = np.inf
        near = 0
        for k,v in dcf_graph[visited[len(visited)//2 + 1]].items():
            if k not in visited:
                if v < min_dist:
                    min_dist = v
                    near = k
        if near != 0:
            visited.insert(len(visited)//2 + 1, near)
            tot_dist += min_dist
    return visited, tot_dist

# we built the fully connected graph
def fully_connected_graph(dcf_graph, comb, coord):
    for vert in comb:
        r, s = vert
        t = distance.euclidean(coord[r], coord[s])
        if r not in dcf_graph:
            dcf_graph[r] = {s: t}
        else:
            dcf_graph[r][s] = t
        if s not in dcf_graph:
            dcf_graph[s] = {r: t}
        else:
            dcf_graph[s][r] = t
    return dcf_graph

def street(graph,dcf_graph, rand_po):    
    visited_1, dist_1 = shortest_path_l_r(dcf_graph, rand_po[2], rand_po[4])
    visited_2, dist_2 = shortest_path_l_r(dcf_graph, rand_po[4], rand_po[2])
    if dist_1 < dist_2:
        visited = visited_1
    else:
        visited = visited_2[::-1]
        
    # building list of nodes to visit
    Nodes = []
    for i in range(len(visited)-1):
        Nodes += f3(graph, visited[i], visited[i+1]) 
    return Nodes, visited

def visualization_4(visited, Nodes, coord):
    import folium
    starting = coord[visited[0]]
    mapit = folium.Map( location=[starting[1], starting[0]], zoom_start = 10 )
    Way = []
    for i in range(len(Nodes)):
        v = coord[Nodes[i]]
        Way.append((v[1], v[0]))
    folium.PolyLine(Way, color="gray", weight=2.5).add_to(mapit)
    
    for i in range(len(Way)):
        folium.CircleMarker(Way[i], radius = 3, opacity=0.1 + 0.9*((i+1)/len(Nodes))).add_to(mapit)
    for i in range(1,len(visited)-1):
        v = coord[visited[i]]
        folium.Marker((v[1], v[0]), icon=folium.Icon(color='blue', icon='cloud') , radius=8 ).add_to(mapit)
    folium.Marker( Way[0], icon=folium.Icon(color='green', icon='cloud') , radius=8 ).add_to(mapit)
    folium.Marker( Way[-1], icon=folium.Icon(color='red', icon='cloud') , radius=8 ).add_to(mapit)
    
    mapit.save(path + 'map.html')
    
    # We need to removit because otherwise the bulitin map() function doesn't work well
    del folium
 



# this is just for now, this part goes in main.py

graph = d(nx.Graph())
coord = coordinates({})
number = 6
n_max = 100 #1890816
rand_po = np.random.randint(60000, 60000+n_max,number)


comb = list(combinations(rand_po, 2))


dcf_graph = fully_connected_graph({}, comb, coord)

try:
    Nodes, visited = street(graph,dcf_graph, rand_po)
    visualization_4(visited, Nodes, coord)
except:
     print("Cannot reach the end from this starting node")


