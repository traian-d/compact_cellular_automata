class Game:

    def __init__(self, topology, starting_pattern, collects_states=True):

        self.collects_states = collects_states
        self.states = [starting_pattern]
        self.last_state = starting_pattern
        self.topology = topology

    def pad_states(self):
        padded_states = []
        n_rows = self.topology.n_rows
        if self.topology.n_rows == 1:
            n_rows = len(self.states)
        for i in range(len(self.states)):
            padded_state = self.state_to_bitlist(i)
            if self.topology.n_rows == 1:
                padded_state = [cell for state in self.states[:i] for cell in state]
                padded_state.extend(self.states[i])
                padded_state.extend([0] * (n_rows - i - 1) * self.topology.n_cols)
            padded_states.append(padded_state)
        return padded_states, n_rows

    def state_to_bitlist(self, state_index):
        n_cells = self.topology.n_rows * self.topology.n_cols
        bin_str = bin(self.states[state_index])[2:]
        left_pad = [0] * (n_cells - len(bin_str))
        return left_pad + [int(i) for i in bin_str]

    def states_to_string(self):
        output = []
        for i in range(len(self.states)):
            bitlist = self.state_to_bitlist(i)
            output.append(''.join([str(bit) for bit in bitlist]))

        return output

    def apply_rule(self, rule):
        self.last_state = rule(self.topology.adj_dict, self.last_state)
        if self.collects_states:
            self.states.append(self.last_state)
        return -1
