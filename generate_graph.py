import random
import numpy as np
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

class random_generate_graph(object):
    
    def __init__(self,vertices_number,edges_number):
        self.v = vertices_number
        self.e = edges_number
        self.graph_dict = {}
        self.matrix = [[0 for i in range(self.v)] for j in range(self.v)]
            
    def adjacent_matrix(self):
        # for a connected without self loop graph, the maximum edges number
        max_edges_number = int(self.v*(self.v-1)/2)
        # if bigger than the max numbers of edges, return False
        if self.e > max_edges_number:
            print('False edges number')
            return False
        
        while self.is_connected() == False:
            
            # random choose specific number of edges to connect
            edges_index = sorted(random.sample(range(0,max_edges_number),self.e))
            
            # get the connect edges index
            edges_dict = {}
            m = 0
            for i in range(self.v):
                for j in range(i+1,self.v):
                    edges_dict[m] = [i,j]
                    m += 1

            # undirected graph adjacent matrix setting
            for index in edges_index:
                if index in edges_dict:
                    i = edges_dict[index][0]
                    j = edges_dict[index][1]
                    self.matrix[i][j] = self.matrix[j][i] = 1

            # the vertices should not be self connected
            for index in range(self.v):
                self.matrix[index][index] = 0
        else:
            print ("Initializing a graph with %d vertices and %d edges" % (self.v,self.e))
    
    
    def matrix_to_dict(self):
        for i,row in enumerate(self.matrix):
            self.graph_dict[i] = []
            for j, adjacent in enumerate(row):
                if adjacent:
                    self.graph_dict[i].append(j)
        
    ## Using BFS to test if the generated adjacent martrix is a connected graph
    def is_connected(self):
        see = set()
        Q = deque()
        Q.append(0)
        
        self.matrix_to_dict()
        while len(Q) > 0:
            p = Q.popleft()
            if p not in see:
                see.add(p)
                connect_vertices = self.graph_dict[p]
                for item in connect_vertices:
                    Q.append(item)
        if len(see) == len(self.graph_dict):
            return True
        else:
            return False
        
    # draw graph from the adjacent matrix
    def draw(self):
        G = nx.from_numpy_matrix(np.array(self.matrix))
        nx.draw(G, with_labels=True)
