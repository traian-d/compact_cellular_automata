class Game:

    def __init__(self, topology):
        self.states = [[0] * (topology.n_rows * topology.n_cols)]

        self.topology = topology

    def pad_states(self):
        padded_states = []
        n_rows = self.topology.n_rows
        if self.topology.n_rows == 1:
            n_rows = len(self.states)
        for i in range(len(self.states)):
            padded_state = self.states[i]
            if self.topology.n_rows == 1:
                padded_state = [cell for state in self.states[:i] for cell in state]
                padded_state.extend(self.states[i])
                padded_state.extend([0] * (n_rows - i - 1) * self.topology.n_cols)
            padded_states.append(padded_state)
        return padded_states, n_rows

    def states_to_string(self):
        output = []
        local_states = self.states
        n_rows = self.topology.n_rows
        n_cols = self.topology.n_cols
        if self.topology.n_rows == 1:
            local_states, n_rows = self.pad_states()
        for state in local_states:
            output.append(self.state_to_string(state, n_rows, n_cols))
        return output

    def state_to_string(self, state, n_rows, n_cols):
        output = ''
        for i in range(n_rows):
            for j in range(n_cols):
                value = state[i * n_cols + j]
                if value == 0:
                    output += '\x1b[0;37;47m' + str(value) + ' \x1b[0m'
                else:
                    output += '\x1b[0;34;44m' + str(value) + ' \x1b[0m'
            if n_rows > 1:
                output += '\n'
        return output

    def apply_rule(self, rule):
        self.states.append(rule(self.topology.adj_dict, self.states[-1]))

    def append_state(self, state):
        self.states.append(state)
