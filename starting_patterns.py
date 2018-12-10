
def conway_glider(n_rows, n_cols, starting_pos):
    initial_state = [0] * n_rows * n_cols
    initial_state[starting_pos] = 1
    initial_state[starting_pos + n_rows + 1] = 1
    initial_state[starting_pos + 2 * n_rows - 1] = 1
    initial_state[starting_pos + 2 * n_rows] = 1
    initial_state[starting_pos + 2 * n_rows + 1] = 1
    return initial_state


def acorn(n_rows, n_cols, starting_pos):
    initial_state = [0] * n_rows * n_cols
    initial_state[starting_pos] = 1
    initial_state[starting_pos + n_rows + 2] = 1
    initial_state[starting_pos + 2 * n_rows - 1] = 1
    initial_state[starting_pos + 2 * n_rows] = 1
    initial_state[starting_pos + 2 * n_rows + 3] = 1
    initial_state[starting_pos + 2 * n_rows + 4] = 1
    initial_state[starting_pos + 2 * n_rows + 5] = 1
    return initial_state


def one_dot(n_rows, n_cols, starting_pos):
    initial_state = [0] * n_rows * n_cols
    initial_state[starting_pos] = 1
    return initial_state
