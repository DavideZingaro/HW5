import copy


def func_1(b,dist):
    # Set of all adjacent nodes
    c = set()
    a = list(b.keys())[0]
    # C is the graph, b is the current node and dist is the maximum distance
    # from it
    ric(C,b,dist)
    # Removing initial node
    c.remove(a)
    
    return c

def ric(C,b,dist): #C is the graph
    # Set s to upload the list of nodes whose distance is less than d
    s = set()
    for i in b:
        d = dict(copy.deepcopy(C[i]))
        for k in d:
            # Uploading distance
            d[k]['weight'] += b[i]['weight']
        
            # Checking if the distance from b in less than dist
            if d[k]['weight'] <= dist:
                c.add(k)
                s.add(k)
                
        v = copy.deepcopy(d)        
        for i in d:
            if i not in s:
                del v[i]                
                        
    if len(s) == 0: # If no node is left to check          
        return
    
    else:            
        return ric(C,v, dist)