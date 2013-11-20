#!/usr/bin/env python

class EdgeNode:
    def __init__(self, y = 0, w = 0, n = None):
        self._y = y
        self._weight = w
        self._next = n

class Graph:
    def __init__(self, directed = False):
        self._edges = []
        self._degree = []
        self._nvertices = 0
        self._nedges = 0
        self._directed = directed

    def insert(self, x, y):
        #n = EdgeNode(y, w, n)
        self._nedges += 1
        print x, y

    def __str__(self):
        return "graph"

graph = Graph()
graph.insert(0, 1)
print graph
