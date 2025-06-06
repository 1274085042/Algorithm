import numpy as np

class AdjacencyMatrixGraph:
    def __init__(self, num_vertices:int, is_directed:bool=True, is_weighted:bool=False):
        """
        Intialize a graph by a adjacency matrix.

        Arguments:
        num_vertices -- number of vertices in this graph
        is_directed -- boolean whether or not graph is directed
        is_weighted -- boolean whether or not edges are weighted

        """
        self._num_vertices = num_vertices
        self._is_directed = is_directed
        self._is_weighted = is_weighted
        self._num_edges = 0
        if is_weighted:
            self._adj_matrix = np.ndarray(shape=(num_vertices, num_vertices))
            self._no_edge = float("inf")
            self._adj_matrix.fill(self._no_edge)
        else:
            self._adj_matrix = np.zeros(shape=(num_vertices, num_vertices), dtype=int)
            self._no_edge = 0


    def is_weighted(self) -> bool:
        return self._is_weighted


    def is_directed(self) -> bool:
        return self._is_directed


    def num_vertices(self) -> int:
        return self._num_vertices


    def num_edges(self) -> int:
        return self._num_edges


    def adj_matrix(self):
        return self._adj_matrix


    def has_edge(self, u:int, v:int) -> bool:
        return self._adj_matrix[u, v] != self._no_edge
    

    def insert_edge(self, u:int, v:int, weight=None):
        """
        Insert an edge between vetices u and v.

        Arguments:
        u -- index of vertex
        v -- index of vertex

        """
        # verify the weight's validity
        if self._is_weighted:
            if weight is None:
                raise RuntimeError(f"Inserting unweighted edge({u}, {v}) in a weighted graph.")
        else:
            if weight is not None:
                raise RuntimeError(f"Inserting weighted edge({u}, {v}) in an unweighted graph.")
            
            weight = 1

        if self.has_edge(u, v):
                raise RuntimeError(f"An edge({u} ,{v}) already exists.")
        
        if self._is_directed:
            self._adj_matrix[u, v] = weight
            self._num_edges +=1
        else:
            if u == v:
                raise RuntimeError(f"Cannot insert self-loop({u}, {v}) into undirected graph.")
            else:
                self._num_edges +=1
                self._adj_matrix[u, v] = weight
                self._adj_matrix[v, u] = weight

    
    def delete_edge(self, u:int, v:int):
        if self.has_edge(u, v):
            self._num_edges -= 1
            if self._is_directed:
                self._adj_matrix[u, v] = self._no_edge
            else:
                self._adj_matrix[u, v] = self._no_edge
                self._adj_matrix[v, u] = self._no_edge


    def edges_list(self) -> list:
        edges_list = []
        for u in range(self._num_vertices):
            if self._is_directed:
                lowest_v = 0
            else:
                lowest_v = u + 1
            for v in range(lowest_v, self._num_vertices):
                if self.has_edge(u, v):
                    edges_list.append((u, v))
        return edges_list


    def copy(self) -> "AdjacencyMatrixGraph":
        copy_graph = AdjacencyMatrixGraph(self._num_vertices, self._is_directed, self._is_weighted)
        copy_graph._adj_matrix = self._adj_matrix.copy() # deep copy
        copy_graph._num_edges = self._num_edges
        return copy_graph
    

    def __str__(self):
        
        return str(self._adj_matrix)
    
    
if __name__ == "__main__":
    # Directed
    array1 = [8, 0, 9, 8, 8, 9, 8, 8, 2, 8, 8, 7, 5, 9, 6, 2, 6, 2, 8, 4]
    graph1 = AdjacencyMatrixGraph(10)
    for i in range(0, len(array1)-1, 2):
        try:
            graph1.insert_edge(array1[i], array1[i+1])
        except RuntimeError as e:
            print(e)
    print(graph1)
    print(graph1.num_edges())
    print(graph1.edges_list())

    # Undirected
    graph2 = AdjacencyMatrixGraph(10, is_directed=False)
    for i in range(0, len(array1)-1, 2):
        try:
            graph2.insert_edge(array1[i], array1[i+1])
        except RuntimeError as e:
            print(e)
    print(graph2)
    print(graph2.num_edges())
    print(graph2.edges_list())
    
    # Test has_edge
    for i in range(graph2.num_vertices()):
        for j in range(graph2.num_vertices()):
            if graph2.has_edge(i, j):
                print(f"({i}, {j})")
            else:
                if i != j:
                    missing_edge = (i,j)
    print(f"graph2 missing edge: {missing_edge}")

    # Test copy
    graph3 = graph2.copy()
    graph3.insert_edge(*missing_edge)
    print(graph2.num_edges())
    print(graph3.edges_list())
    print(graph3.num_edges())

    # Test delete_edge
    graph3.delete_edge(*missing_edge)
    print(graph3.edges_list())
    print(graph3.num_edges())

    # Test weighted
    graph4 = AdjacencyMatrixGraph(10, True, True)
    try:
        graph4.insert_edge(0, 1)
    except RuntimeError as e:
        print(e)
    
    for i in range(0, len(array1)-1, 2):
        try:
            graph4.insert_edge(array1[i], array1[i+1], array1[i])
        except RuntimeError as e:
            print(e)
    print(graph4)
    print(graph4.num_edges())
    print(graph4.edges_list())
