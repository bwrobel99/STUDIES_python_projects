# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 18:35:28 2019

@author: bart
"""

import unittest
import graphs_2 as mr
import networkx as nx

class TestGraphs2(unittest.TestCase):
    
    def test_load_from_file(self):
        G = mr.load_multigraph_from_file('.\dijkstra_multi.dat')
        graph = nx.MultiDiGraph()
        graph.add_weighted_edges_from([(1,2,0.5), (2,3,0.3), (2,3,0.4), (1,3,1.0)])
        print(nx.info(graph))
        self.assertEqual(nx.info(G), nx.info(graph))
        
        
    def test_find_min_trail(self):
        graph = nx.MultiDiGraph()
        graph.add_weighted_edges_from([(1,2,0.5), (2,3,0.4), (2,3,0.3), (1,3,1.0)])
        buff = [mr.TrailSegmentEntry(start_node = 1, end_node = 2, edge_id = 0, edge_weight = 0.5),
                mr.TrailSegmentEntry(start_node = 2, end_node = 3, edge_id = 1, edge_weight = 0.3)]
        self.assertEqual(mr.find_min_trail(graph, 1, 3), buff)
        
    def test_trail_to_str(self):
        graph = nx.MultiDiGraph()
        graph.add_weighted_edges_from([(1,2,0.5), (2,3,0.4), (2,3,0.3), (1,3,1.0)])   
        tr = mr.find_min_trail(graph, 1,3)
        string = mr.trail_to_str(tr)
        self.assertEqual(string, '1 -[0: 0.5]-> 2 -[1: 0.3]-> 3  (total = 0.8)')
        
if __name__ == '__main__':
    unittest.main()