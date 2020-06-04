def rectangular_four_neighbors(n_rows, n_cols):
    adj_dict = {}

    for i in range(n_rows):
        for j in range(n_cols):
            loc = i * n_cols + j
            if loc not in adj_dict:
                adj_dict[loc] = []

            if i > 0:
                adj_dict[loc].append((i - 1) * n_cols + j)
            if i < n_rows - 1:
                adj_dict[loc].append((i + 1) * n_cols + j)

            if j > 0:
                adj_dict[loc].append(i * n_cols + j - 1)
            if j < n_cols - 1:
                adj_dict[loc].append(i * n_cols + j + 1)

    return False, adj_dict


def rectangular_four_diagonal_neighbors(n_rows, n_cols):
    adj_dict = {}

    for i in range(n_rows):
        for j in range(n_cols):
            loc = i * n_cols + j
            if loc not in adj_dict:
                adj_dict[loc] = []

            if i > 0:
                if j > 0:
                    adj_dict[loc].append((i - 1) * n_cols + j - 1)
                if j < n_cols - 1:
                    adj_dict[loc].append((i - 1) * n_cols + j + 1)
            if i < n_rows - 1:
                if j > 0:
                    adj_dict[loc].append((i + 1) * n_cols + j - 1)
                if j < n_cols - 1:
                    adj_dict[loc].append((i + 1) * n_cols + j + 1)

    return False, adj_dict


def top_bottom_cylinder(n_rows, n_cols):
    adj_dict = {i: [] for i in range(n_rows * n_cols)}
    for i in range(n_cols):
        adj_dict[i].append((n_rows - 1) * n_cols + i)
        adj_dict[(n_rows - 1) * n_cols + i].append(i)
    return False, adj_dict


def top_bottom_diag(n_rows, n_cols):
    adj_dict = {i: [] for i in range(n_rows * n_cols)}
    for i in range(n_cols):
        if i > 0:
            adj_dict[i].append((n_rows - 1) * n_cols + i - 1)
            adj_dict[(n_rows - 1) * n_cols + i - 1].append(i)
        if i < n_cols - 1:
            adj_dict[i].append((n_rows - 1) * n_cols + i + 1)
            adj_dict[(n_rows - 1) * n_cols + i + 1].append(i)

    return False, adj_dict


def left_right_cylinder(n_rows, n_cols):
    adj_dict = {i: [] for i in range(n_rows * n_cols)}
    for i in range(n_rows):
        adj_dict[i * n_cols].append((i + 1) * n_cols - 1)
        adj_dict[(i + 1) * n_cols - 1].append(i * n_cols)
    return False, adj_dict


def left_right_diag(n_rows, n_cols):
    adj_dict = {i: [] for i in range(n_rows * n_cols)}
    for i in range(n_rows):
        if i > 0:
            adj_dict[i * n_cols].append(i * n_cols - 1)
            adj_dict[i * n_cols - 1].append(i * n_cols)
        if i < n_rows - 1:
            adj_dict[i * n_cols].append((i + 2) * n_cols - 1)
            adj_dict[(i + 2) * n_cols - 1].append(i * n_cols)

    return False, adj_dict


def join_corners(n_rows, n_cols):
    adj_dict = {i: [] for i in range(n_rows * n_cols)}
    adj_dict[0] = [n_rows * n_cols - 1]
    adj_dict[n_rows * n_cols - 1] = [0]
    adj_dict[n_cols - 1] = [(n_rows - 1) * n_cols]
    adj_dict[(n_rows - 1) * n_cols] = [n_cols - 1]

    return False, adj_dict


def two_neighbors_ordered(n_rows, n_cols):
    adj_dict = {}
    for i in range(0, n_cols):
        if i not in adj_dict:
            adj_dict[i] = []
        if i > 0:
            adj_dict[i].append(i - 1)
        if i < n_cols - 1:
            adj_dict[i].append(i + 1)
    return True, adj_dict
