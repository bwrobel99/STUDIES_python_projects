# Bartosz Wrobel, 302940
#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import Dict, Tuple, List

def adjmat_to_adjlist(adjmat: List[List[int]]) -> Dict[int, List[int]]:
    dct = {}
    for row, list in enumerate(adjmat,1):
        list_ = []
        for index, value in enumerate(list,1):
            if value != 0:
                list_.extend(value*[index])
            if len(list_)>0:
                dct[row] = list_[:]
    return dct

def dfs_recursive(G: Dict[int, List[int]], s: int) -> List[int]:
    visited=[]
    def rec_inner(G_: Dict[int, List[int]], s_: int, visited_: List[int]) -> List[int]:

        visited_.append(s_)
        for v in G_[s_]:
            if v not in visited_:
                rec_inner(G_, v, visited_)

        return visited_

    return rec_inner(G, s, visited)

def dfs_iterative(G: Dict[int, List[int]], s: int) -> List[int]:
    stack = [s]
    visited = []
    while stack:
        tmp = stack.pop()
        if tmp not in visited:
            visited.append(tmp)
            for elem in reversed(G[tmp]):
                stack.append(elem)
    return visited

def is_acyclic_support(G: Dict[int, List[int]], s:int) -> bool:
    stack = [s]
    visited = []
    while stack:
        tmp = stack.pop()
        if tmp not in visited:
            visited.append(tmp)
            for elem in reversed(G[tmp]):
                if elem not in visited:
                    stack.append(elem)
                elif G[elem]:
                    return False
    return True

def is_acyclic(G: Dict[int, List[int]]) -> bool:

    for i in G.keys():
        support = is_acyclic_support(G, i)
        if support is False:
            return support
    return True
def kacper():
    print("Kacper")
# Bartosz Wrobel, 302940