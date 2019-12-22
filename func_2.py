# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 22:52:37 2019

@author: Nathan
"""

#We import the needed libraries and modules

import pandas as pd
import csv
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.shortest_paths.weighted import single_source_dijkstra
import collections
import heapq
from collections import defaultdict
from itertools import groupby
from ipywidgets import HTML
from ipyleaflet import Map, basemaps, basemap_to_tiles, Polyline, Marker, Icon, Popup
from itertools import permutations

#we import data

distance_df = pd.read_csv(r'C:\Users\Nathan\Sapienza\AMDM\HW5\USA-road-d.CAL.gr',sep = " ", header = None)
time_df = pd.read_csv(r'C:\Users\Nathan\Sapienza\AMDM\HW5\USA-road-t.CAL.gr',sep = " ", header = None)
node_df = pd.read_csv(r'C:\Users\Nathan\Sapienza\AMDM\HW5\USA-road-d.CAL.co.gr',sep = " ", header = None)


#we create lists with nodes_data 

nodes = []
lat = []
long = []
for key, value in node_df.iterrows():
    nodes.append(value[1])
    lat.append(value[2] / 1000000)
    long.append(value[3] / 1000000)
    
    
G = nx.Graph()

for key,value in distance_df.iterrows():
    G.add_edge(value[1], value[2], distance = value[3])
    

def get_shortest_path(graph, starting_node, ending_node):
    G = graph
    nodes_to_visit = [starting_node] 
    path = []
    n = 0
    visited_nodes = [] #we store visited nodes 
    
    while ending_node not in nodes_to_visit: #the stopping criteria is when the final node is in the visit list
        if nodes_to_visit[n] not in visited_nodes: #we visit each node just one time

            for neighbor in list(G.neighbors(nodes_to_visit[n])): 
                nodes_to_visit.append(neighbor) #we add the node we are visiting's neighbors to nodes_to_visit
                
            path.append(list(G.neighbors(nodes_to_visit[n]))) #we save the path to know where each node comes from
            visited_nodes.append(nodes_to_visit[n]) #we finally add the node to the visited_nodes
        n += 1
        
    element = visited_nodes[-1] # We save the element that has added the 'start' point in the 'to_visit' list
    n = 1
    result = [ending_node, element]
    
    while n < 100000 and element != starting_node: #as we are getting the path in the opposite direction, we iterate until we find the starting node
        p = []
        for k in range(len(path)):
            for i in range(len(path[k])):
                if path[k][i] == element: #we look for the last element we visited
                    p.append(k)
        element = visited_nodes[p[0]] # here we get which element is its parent
        i += 1
        result.append(element) # we add each parent to the result because it's part of the path
        
    result.reverse()
    
    return(result)
    

def get_distance_between_connected_nodes(function, starting_node, ending_node):
    a = function.loc[(function[1] == starting_node) & (function[2] == ending_node)] #use the dataframe to get the distance
    if len(a)>0 : 
        return int(a[3]) #get the distance
    else: 
        return 0
    
def get_distance_between_not_connected_nodes(function, starting_node, ending_node):
    path = get_shortest_path(G, starting_node,ending_node) #using the get_shortest function
    i = 0
    sum = 0
    while i < len(path)-1:
        sum += get_distance_between_connected_nodes(function, path[i], path[i+1]) #getting the distance between all connected node in the path
        i += 1
        
    return(sum)
    
def func2(nodes_list, function):
    l = []
    for s in permutations(nodes_list): #we try all the possibilities of the initial list of nodes
        case = list(s)
        sum_tot = 0
        n = 0
        while n < len(case)-1:
            sum_tot += get_distance_between_not_connected_nodes(function, case[n], case[n+1]) #we calculate the distance for each possibility
            n += 1
        element = (case, sum_tot)
        l.append(element) # we save the for each possibility, the distance
        
    l = sorted(l, key=lambda tup: (tup[1]),reverse = False) # we sort the list
    best_net = l[0][0] # we get the best possibilities
    
    

    i = 0
    list_edge = []
    while i < len(best_net)-1:
            list_edge = list_edge + get_shortest_path(G, best_net[i],best_net[i+1])
            i += 1
    return(best_net, list_edge) # we return the best path
    

def viz2(G, nodes_list, function):
    net, result = func2(nodes_list, function) # use the previous function
    edges = []
    for k in result:
        for i in list(G.neighbors(k)):
            edges.append((k,i)) #we fill the list with the neighbors of the nodes in the result
    red = []
    i = 0
    while i < len(result) -1:
        edges.append((result[i],result[i+1])) #we full the list with the nodes in the result
        red.append((result[i],result[i+1])) # we fill another list to print it with a different color
        i = i+1
    fig = plt.gcf()
    fig.set_size_inches(20, 20)


    G1 = nx.DiGraph()
    G1.add_edges_from(edges)

    val_map = {1: 2.0,
               }

    values = [val_map.get(node, 0.2) for node in G1.nodes()]

    # Specify the edges you want here

    red_edges = red
    edge_colours = ['black' if not edge in red_edges else 'red' for edge in G1.edges()]
    black_edges = [edge for edge in G1.edges() if edge not in red_edges]


    pos = nx.spring_layout(G1)
    
    for key,value in pos.items() :
        index = nodes.index(key)
        value[0] = lat[index]
        value[1] = long[index] # we get the real coordinates of each node

    
    nx.draw_networkx_nodes(G1, pos, cmap=plt.get_cmap('jet'), node_color = values, node_size = 1)
    nx.draw_networkx_labels(G1, pos)
    nx.draw_networkx_edges(G1, pos, edgelist=red_edges, edge_color='red', arrows=True)
    nx.draw_networkx_edges(G1, pos, edgelist=black_edges, edge_color='black',arrows=False)
    
    

a = viz2(G, [3,1,2], distance_data)
plt.show()






