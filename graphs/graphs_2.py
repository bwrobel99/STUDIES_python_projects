#Bartosz Wrobel, 302940

from typing import List, Set, Dict, NamedTuple
from enum import Enum, auto
import networkx as nx
# Pomocnicza definicja podpowiedzi typu reprezentującego etykietę
# wierzchołka (liczba 1..n)

VertexID = int
AdjMatrix = List[List[int]]
AdjList = Dict[VertexID, List[VertexID]]
VertexID = int
EdgeID = int
Distance = int

class Colors(Enum):
    WHITE = auto()
    GREY = auto()
    BLACK = auto()

class Node(NamedTuple):
    id: int
    distance: int

class TrailSegmentEntry(NamedTuple):
    start_node: VertexID
    end_node: VertexID
    edge_id: VertexID
    edge_weight: float

Trail = List[TrailSegmentEntry]
    
def neighbors(adjlist: AdjList, start_vertex_id: VertexID,
              max_distance: Distance) -> Set[VertexID]:
    col_dict = {}
    result = set()
    for i in adjlist:
        col_dict[i] = Colors.WHITE
    col_dict[start_vertex_id] = Colors.GREY
    Q = [Node(start_vertex_id, 0)]
    while Q:
        u = Q.pop()
        if u.distance <= max_distance and u.id != start_vertex_id:
            result.add(u.id)
        if u.id in adjlist:
            for v in adjlist[u.id]:
                if v not in col_dict:
                    Q.append(Node(v, u.distance+1))
                    continue
                elif col_dict[v] == Colors.WHITE:
                    col_dict[v] = Colors.GREY
                    Q.append(Node(v, u.distance+1))
        col_dict[u.id] = Colors.BLACK
    return result 
  
 
def load_multigraph_from_file(filename: str) -> nx.MultiDiGraph:
    
    data = []
    with open(filename, 'r') as file:
        for line in file:
            if line.split():
                lil_tuple = int(line.split()[0]), int(line.split()[1]), float(line.split()[2])
                data.append(lil_tuple)
    Graph = nx.MultiDiGraph()
    Graph.add_weighted_edges_from(data)
    return Graph

def min_trail_support(g, start_node_, end_node_):
    weight_dict = {}
    for i in g[start_node_][end_node_]:
        weight_dict[i] = g[start_node_][end_node_][i]['weight']
        id_ = min(weight_dict, key=weight_dict.get)
        weight_ = weight_dict[id_]
        result = TrailSegmentEntry(start_node = start_node_, end_node = end_node_, 
                                   edge_id = id_, edge_weight = weight_)
        
    return result
    
    
def find_min_trail(g: nx.MultiDiGraph, v_start: VertexID, v_end: VertexID) -> Trail:

        path = nx.dijkstra_path(g, v_start, v_end)
        trail_lst = []
        i = 0
        while i+1<len(path):
            trail_lst.append(min_trail_support(g, path[i], path[i+1]))
            i+=1
        return trail_lst
            
def trail_to_str(trail: Trail) -> str:
    sum_of_weights = 0
    final_string = ''
    for elem in trail:
        sum_of_weights+=elem.edge_weight
        if elem is trail[0]:
            final_string += '{} -[{}: {}]-> {}'.format(elem.start_node, elem.edge_id, elem.edge_weight, elem.end_node)
        else:
            final_string += ' -[{}: {}]-> {}'.format(elem.edge_id, elem.edge_weight, elem.end_node)
    final_string+= '  (total = {})'.format(sum_of_weights)
    return final_string

#Bartosz Wrobel, 302940