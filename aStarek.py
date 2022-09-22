
def aStarAlgo(start_node,stop_node):
    open_set = set(start_node)
    close_set = set()

    g = {} #store distance from starting node
    parent = {} # parent contains an adjacent map of all nodes

    g[start_node] = 0
    #print(g) #{'A':0}
    parent[start_node] = start_node
    #print(parent) #{'A':'A'}
    while len(open_set) > 0 : 
       # print((open_set))  #-->len : 1,2,3,3,2,1
        n = None

        
        for v in open_set: 
            #print(heuristic(v)) --> heuristic value 14,12,11,6,4,0
           
            if n == None or g[v] + heuristic(v) < g[n] + heuristic(n): 
                n = v  
        if n == stop_node or Graph_node[n] == None: 
            pass
            
        else:
            for (m,weight) in get_neighbour(n): #get_neghbour(v) give A,B,G which is not path
                #m = B, C , E , D , E , G ,E , G
            #WEIGHT= 4, 3 , 10, 7 , 2 , 5 ,12, 16
                if m not in open_set and m not in close_set: 
                    #print(m)
                    open_set.add(m)
                    #print(m)  -->B,C,E,D,G
                    #print(n)   -->A,A,C,C,B
                    #print(parent)
                    # {'A': 'A', 'B': 'A', 'C': 'A', 'E': 'C', 'D': 'C'}
                    parent[m] = n
                    
                    # parent[m] value A,A,A,C,C,E
                    # n = A,A,A,C,C,E
        
                    #print(g) -->{'A': 0, 'B': 4, 'C': 3, 'E': 13, 'D': 10}
                   # print(g[n]) --> 0,0,3,3,4 means(A,A,C,C,B)
                   # print(weight)  --> B:4,C:3,E:10,D:7,G:5
                    g[m] = g[n] + weight
                else: 
                    if g[m] > g[n] + weight:
                        
                        g[m] = g[n] + weight
                        parent[m] = n

                        # if m in close_set:
                        #     close_set.remove(m)
                        #     open_set.add(n)

        if n == None:
            print('Path is not exist')
            return None
        
        if n == stop_node:
            path = []
            while parent[n] != n:
                path.append(n)
                n = parent[n]
               

            path.append(start_node)
            path.reverse()

            print('Path found: {}'.format(path))
            return path

        open_set.remove(n)
        close_set.add(n)
    
    print('path not exist')
    return None

def get_neighbour(v):
    if v in Graph_node: # v = A,B,C,D,E  --> String
        return Graph_node[v]  #Graph_node[v] is [('B,4),('C',3)],.....
    else:
        return None

def heuristic(n):
    H_dist = {
         'A' : 14 ,
         'B' : 12 ,
         'C' : 11 ,
         'D' : 6 ,
         'E' : 4 ,
         'G' : 0 ,    
    }
    return H_dist[n]

Graph_node = {
    'A' : [('B',4),('C',3)],
    'B' : [('E',12),('G',16)],
    'C' : [('E',10),('D',7)],
    'D' : [('E',2)],
    'E' : [('G',5)]
}

aStarAlgo('A', 'G')