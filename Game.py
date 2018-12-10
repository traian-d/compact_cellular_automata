class Game:

    def __init__(self, topology):
        self.states = [[0] * (topology.n_rows * topology.n_cols)]

        self.topology = topology

    def states_to_string(self):
        output = []
        for state in self.states:
            output.append(self.state_to_string(state))
        return output

    def state_to_string(self, state):
        output = ''
        for i in range(self.topology.n_rows):
            for j in range(self.topology.n_cols):
                value = state[i * self.topology.n_cols + j]
                if value == 0:
                    output += '\x1b[0;37;47m' + str(value) + ' \x1b[0m'
                else:
                    output += '\x1b[0;34;44m' + str(value) + ' \x1b[0m'
            if self.topology.n_rows > 1:
                output += '\n'
        return output

    def apply_rule(self, rule):
        self.states.append(rule(self.topology.adj_dict, self.states[-1]))

    def append_state(self, state):
        self.states.append(state)
