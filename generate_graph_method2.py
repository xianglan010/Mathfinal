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
        if self.e > max_edges_number or self.e < self.v - 1:
            print('False edges number')
            return False
        
        # store the matrix index i,j in list
        edges = []
        for i in range(self.v):
            for j in range(i+1,self.v):
                edges.append((i,j))
                
        # first get a connected graph with n vertice, n-1 edges
        for i in range(0,self.v-1):
            j = random.randint(i+1,self.v-1)
            self.matrix[i][j] = 1
            self.matrix[j][i] = 1
            # remove the edges used
            edges.remove((i,j))
            
        # get the remain edges number
        remain_edge_num = self.e - self.v + 1
        print(remain_edge_num)
                        
        remain_edge_index = sorted(random.sample(range(0,len(edges)),remain_edge_num))
        
        for k in remain_edge_index:
            i = edges[k][0]
            j = edges[k][1]
            self.matrix[i][j] = self.matrix[j][i] = 1
            
        # the vertices should not be self connected
        for index in range(self.v):
                self.matrix[index][index] = 0
                
        print ("Initializing a graph with %d vertices and %d edges" % (self.v,self.e))
    
    def matrix_to_dict(self):
        for i,row in enumerate(self.matrix):
            self.graph_dict[i] = []
            for j, adjacent in enumerate(row):
                if adjacent:
                    self.graph_dict[i].append(j)
        
    # draw graph from the adjacent matrix
    def draw(self,color):
        G = nx.from_numpy_matrix(np.array(self.matrix))
        nx.draw(G, cmap=plt.get_cmap('viridis'), node_color=color,with_labels=True)
        
    def draw_no(self):
        G = nx.from_numpy_matrix(np.array(self.matrix))
        nx.draw(G, with_labels=True)
