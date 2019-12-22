import copy


def f1(b,dist):
    # Set s to upload the list of nodes whose distance is less than d
    s = set()
    for i in b:
        d = dict(copy.deepcopy(C[i]))
        for k in d:
            d[k]['weight'] += b[i]['weight']
        
            # Checking if the distance from b in less than d
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
            return f1(v, dist)
                