class Topology:

    def __init__(self, n_rows, n_cols, topology_function, power_up=True):
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.topology_function = topology_function

        self.has_neighbor_order, self.adj_dict = topology_function(n_rows, n_cols)
        if power_up:
            self.power_up()

    def __add__(self, other):
        if other.n_rows != self.n_rows or other.n_cols != self.n_cols:
            raise ValueError('Topologies have different row/column sizes.')
        if self.has_neighbor_order or other.has_neighbor_order:
            raise ValueError('Topologies with neighbor order cannot be added.')

        def combined_topology_function(n_rows, n_cols):
            self_adj_dict = self.topology_function(n_rows, n_cols)[1]
            other_adj_dict = other.topology_function(n_rows, n_cols)[1]
            for cell in other_adj_dict:
                self_adj_dict[cell].extend(other_adj_dict[cell])
            return self.has_neighbor_order, self_adj_dict

        return Topology(self.n_rows, self.n_cols, combined_topology_function)

    def power_up(self):
        output_dict = {}
        for cell in self.adj_dict:
            output_dict[pow(2, cell)] = [pow(2, neigh) for neigh in self.adj_dict[cell]]
        self.adj_dict = output_dict
