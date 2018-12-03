class Topology:

    def __init__(self, rows, cols, topology_function):
        self.rows = rows
        self.cols = cols
        self.cell_values = [0] * (rows * cols)
        self.topology_function = topology_function

        self.has_neighbor_order, self.adj_dict = topology_function(rows, cols)

    def __str__(self):
        output = ''
        for i in range(self.rows):
            for j in range(self.cols):
                output += str(self.cell_values[i * self.cols + j])
                output += ' '
            output += '\n'
        return output

    def apply_rule(self, rule):
        self.cell_values = rule(self.adj_dict, self.cell_values)

    def apply_state(self, cell_values):
        self.cell_values = cell_values

