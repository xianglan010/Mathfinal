import heapq

def test_valid(vertice,graph_map,color_map):
    for i in graph_map[vertice]:
        if color_map[i] == color_map[vertice]:
            return False
    return True


def welsh_powell(graph_map):
    
    # get the degree for every vertice
    degree = {}
    for k,v in graph_map.items():
        degree[k] = len(v)

    # build prioity queue using the dict value
    degree_pq = []
    for k,v in degree.items():
        heapq.heappush(degree_pq,(v,k))

    # store the vertices in ascending order of degree
    v_degree_list = []
    for i in range(len(degree)):
        v_degree_list.append(heapq.heappop(degree_pq)[1])
    # get the vertice in discending order of degree
    v_degree_list.reverse()
    
    # set color for the graph
    color_map = []
    for i in range(len(graph_map)):
        color_map.append(0)
    color_index = 1
    used = []
    
    print(v_degree_list)
    print(color_map)
    
    for vertice in v_degree_list:
        if vertice not in used:
            # vertices set color
            if color_map[vertice] == 0:
                color_map[vertice] = color_index
            used.append(vertice)
            # not connect set same color
            for other_vertice in v_degree_list:
                if (other_vertice not in graph_map[vertice]) and (color_map[other_vertice] == 0):
                    color_map[other_vertice] = color_index
                    
                    if test_valid(other_vertice,graph_map,color_map) == False:
                        color_map[other_vertice] = 0
                    else:
                        used.append(other_vertice)
            color_index += 1
    color_num = color_index -1
    return color_map,color_num
