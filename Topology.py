class Topology:

    def __init__(self, n_rows, n_cols, topology_function):
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.states = [[0] * (n_rows * n_cols)]
        self.topology_function = topology_function

        self.has_neighbor_order, self.adj_dict = topology_function(n_rows, n_cols)

    def __add__(self, other):
        if other.n_rows != self.n_rows or other.n_cols != self.n_cols:
            raise ValueError('Topologies have different row/column sizes.')
        if self.has_neighbor_order or other.has_neighbor_order:
            raise ValueError('Topologies with neighbor order cannot be added.')

        def combined_topology_function(n_rows, n_cols):
            self_adj_dict = self.topology_function(n_rows, n_cols)[1]
            other_adj_dict = other.topology_function(n_rows, n_cols)[1]
            return self.has_neighbor_order, {cell: self_adj_dict[cell].union(other_adj_dict[cell]) for cell in other_adj_dict}

        return Topology(self.n_rows, self.n_cols, combined_topology_function)

