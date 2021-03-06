#/usr/bin/env python

import sys
import queue as queue


# Edge class
class Edge:
    def __init__(self, destination, weight=1):
        self.destination = destination
        self.weight = weight


# Vertex class
class Vertex:
    def __init__(self, value='vertex', color='white', parent=None):
        self.value = value
        self.edges = []
        # Color of this vertex
        # Used to mark vertices for the traversal algorithm (BFS or DFS)
        self.color = color
        # Parent reference to keep track of the previous node in the
        # graph when traversing through the graph
        self.parent = parent


# Graph class
class Graph:
    def __init__(self):
        self.vertices = []

    def find_vertex(self, value):
        """
        Looks through all the vertices in the graph instance and returns
        the first vertex it finds that matches the `value` parameter.

        Used in the `main` function to look up the vertices passed in
        from the command line.

        @param {*} value: The value of the Vertex to find

        @return None if no such Vertex exists in the Graph.
        @return {Vertex} the found Vertex
        """
        # DFS Traversal, Iterative
        stack = [self.vertices[0]]
        visited = []

        while len(stack) > 0:
            
            current = stack.pop()
            visited.append(current)
            # print(current.value)

            if current.value.upper() == value.upper():
                # print(current, 'Value found')
                return current

            for edge in current.edges:
                if edge.destination not in visited:
                    stack.append(edge.destination)

        # print('Value not found.')
        return None

        # !!!! IMPLEMENT ME

    def bfs(self, start):
        """
        Breadth-First search from an input starting Vertex
        Should maintain parent references back from neighbors to their parent.

        @param {Vertex} start: The starting vertex
        """

        if start not in self.vertices:
            raise IndexError('Starting value does not exist.')

        visited = []
        storage = queue.Queue()
        storage.put(start)

        while not storage.empty():
            current = storage.get()

            if current not in visited:
                visited.append(current)
            for edge in current.edges:
                if edge.destination not in visited:
                    storage.put(edge.destination)
                    edge.destination.parent = current
        # print(f'bfs: {visited}')
        return visited
        # !!!! IMPLEMENT ME
        

    def output_route(self, start):
        """
        Print out the route from the start vertex back along its parent
        references (these were set in the `bfs` method)

        @param {Vertex} start: The starting Vertex to follow and print
        """
        # !!!! IMPLEMENT ME
        # visited_routes = self.bfs(start)

        parents = [start.value]
        stack = [start]

        while len(stack) > 0:
            current = stack.pop()
            if current.parent:
                parents.append(current.parent.value)
                stack.append(current.parent)

        print('Shortest Route: \n')
        for p in parents:
            print(f'{p} => ', end='')
        print('\n')
        
        # print('Route path: \n')
        # for v in visited_routes:
        #     print(f'{v.value} => ', end='')
        # print('\n')
        # return visited_routes
        

    def route(self, start, end):
        # BFS to build the parent reference tree
        self.bfs(end)
        # print the route from the start Vertex
        self.output_route(start)


# Helper function to add bidirectional edges
def add_edge(start, end):
    start.edges.append(Edge(end))
    end.edges.append(Edge(start))


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: routing.py hostA hostB')
        sys.exit()

    graph = Graph()
    vertA = Vertex('HostA')
    vertB = Vertex('HostB')
    vertC = Vertex('HostC')
    vertD = Vertex('HostD')
    vertE = Vertex('HostE')
    vertF = Vertex('HostF')
    vertG = Vertex('HostG')
    vertH = Vertex('HostH')

    add_edge(vertA, vertB)
    add_edge(vertB, vertD)
    add_edge(vertA, vertC)
    add_edge(vertC, vertD)
    add_edge(vertC, vertF)
    add_edge(vertG, vertF)
    add_edge(vertE, vertF)
    add_edge(vertH, vertF)
    add_edge(vertH, vertE)

    graph.vertices.append(vertA)
    graph.vertices.append(vertB)
    graph.vertices.append(vertC)
    graph.vertices.append(vertD)
    graph.vertices.append(vertE)
    graph.vertices.append(vertF)
    graph.vertices.append(vertG)
    graph.vertices.append(vertH)

    # Look up the hosts passed in from the command line by
    # name to see if we can find them.
    hostAVert = graph.find_vertex(sys.argv[1])

    if hostAVert is None:
        print('routing.py: could not find host: ', sys.argv[1])
        sys.exit()

    hostBVert = graph.find_vertex(sys.argv[2])

    if hostBVert is None:
        print('routing.py: could not find host: ', sys.argv[2])
        sys.exit()

    # Show the route from one Vertex to the other
    graph.route(hostAVert, hostBVert)
