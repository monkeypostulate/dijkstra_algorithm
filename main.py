class Graph:
    '''
    Class creates an undirected weighted graph. 
    It also assumes that graphs are connected, and thus, a new node can be added by adding using the method add_edge.
    '''
    def __init__(self,edges=[],edges_weight=[]):
        self.adjacency_list = {}
        self.edges_weight=edges_weight
           
    def get_nodes(self):
        '''
        get_nodes: gets all nodes.
        '''
        return list(self.adjacency_list.keys())
            
    def add_edge(self,v1,v2, weight :int):
        '''
        add_edge: adds a new edges to the graph. 
        Parameters:
        v1: a node in the graph
        v2: a node in the graph
        if node v1 does not exists, then it is added to the graph.
        The same applies if node v2 does not exists
        '''
        if v1 not in self.adjacency_list:
            self.adjacency_list[v1] = {}
        self.adjacency_list[v1][v2] = weight
        # Since, we are assuming that the network is 
        # undirected, we have to create an edge in the other
        # direction.
        if v2 not in self.adjacency_list:
            self.adjacency_list[v2] = {}
        self.adjacency_list[v2][v1] = weight
        
    def get_neighbours(self,v1):
        '''
        get_neighbours: gets all the neighbors for node a node.
        Parameters:
        v1: a node in the graph        
        '''
        if v1 not in self.adjacency_list:
            return None
        else:
            return list(self.adjacency_list[v1].keys())
    
   
   

   
def dijkstra_algorithm(g,start_node):
    '''
    Finds the shortest path for a given node to all other nodes.
    It returns the length of the shortest distance as a list.
    The shortest path distance as a dictionary, with the key being the end node, and the value being a list with the shortest path.
    
    Parameters: start_node is the node for which we are calculating the shortest paths.
    '''
    import sys
    shortest_path_dist = {}
    shortest_path={}

    previous_nodes = {}
    unvisited_nodes = list(g.get_nodes())
    unvisited_nodes.remove(start_node)
    
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path_dist[node] = max_value
    # However, we initialize the starting node's value with 0   
    shortest_path_dist[start_node] = 0 
    current_min_node=   start_node    
    shortest_path[start_node]=[start_node]

    while(unvisited_nodes):
        # Get all neigbours to the current node
        neighbors = g.get_neighbours(current_min_node)
        # for all the nodes compute the distance
        for neighbor in neighbors:
            tentative_value = shortest_path_dist[current_min_node] + g.adjacency_list[current_min_node][ neighbor]
            if neighbor not in shortest_path.keys():
                shortest_path[neighbor]=[current_min_node,neighbor]
            if tentative_value < shortest_path_dist[neighbor]:
                shortest_path_dist[neighbor] = tentative_value
                previous_nodes[neighbor] = current_min_node
                shortest_path[neighbor]=shortest_path[current_min_node]+[neighbor]
                
        # Get the unvisited node with min distance 
        for i in range(len(unvisited_nodes)): # Iterate over the nodes
            temp_dist=shortest_path_dist[unvisited_nodes[i]]
            if i == 0:
                temp_shortest_dist = temp_dist
                current_min_node = unvisited_nodes[i]
            else:
                if temp_dist<temp_shortest_dist:
                    temp_shortest_dist = temp_dist
                    current_min_node = unvisited_nodes[i]
        unvisited_nodes.remove(current_min_node)        
                
    return shortest_path_dist,shortest_path
   
   
   

   
   
def shortest_path(g,v1,v2):
    '''
    Calculates the shortest path between two nodes.
    Parameters: 
    v1, v2 are the two nodes for which we want to calculate the shortest path.
    '''
    nodes_distance, shortest_paths=dijkstra_algorithm(g,v1)
    return  {'distance': nodes_distance[v2],
             'path': shortest_paths[v2]}
