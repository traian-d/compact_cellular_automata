
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
    return pow(2, starting_pos)


def four_dots(n_rows, n_cols, starting_pos):
    initial_state = [0] * n_rows * n_cols
    initial_state[starting_pos] = 1
    initial_state[starting_pos + 1] = 1
    initial_state[starting_pos + n_cols] = 1
    initial_state[starting_pos + n_cols + 1] = 1
    return initial_state


def tessalation_factory(pattern_string, length):
    def repeated_pattern(n_rows, n_cols, starting_pos):
        reps = length // len(pattern_string) + 1
        rep_str = (pattern_string * reps)[:length]
        int_pattern = 0
        for i in range(length):
            int_pattern += pow(2, length - i - 1) * int(rep_str[i])
        return int_pattern
    return repeated_pattern