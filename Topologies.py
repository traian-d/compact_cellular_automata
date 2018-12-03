
def rectangular_four_neighbors(n_rows, n_cols):
    adj_dict = {}

    for i in range(n_rows):
        for j in range(n_cols):
            loc = i * n_cols + j
            if loc not in adj_dict:
                adj_dict[loc] = set()

            if i > 0:
                adj_dict[loc].add((i - 1) * n_cols + j)
            if i < n_rows - 1:
                adj_dict[loc].add((i + 1) * n_cols + j)

            if j > 0:
                adj_dict[loc].add(i * n_cols + j - 1)
            if j < n_cols - 1:
                adj_dict[loc].add(i * n_cols + j + 1)

    return False, adj_dict


def rectangular_four_diagonal_neighbors(n_rows, n_cols):
    adj_dict = {}

    for i in range(n_rows):
        for j in range(n_cols):
            loc = i * n_cols + j
            if loc not in adj_dict:
                adj_dict[loc] = set()

            if i > 0:
                if j > 0:
                    adj_dict[loc].add((i - 1) * n_cols + j - 1)
                if j < n_cols - 1:
                    adj_dict[loc].add((i - 1) * n_cols + j + 1)
            if i < n_rows - 1:
                if j > 0:
                    adj_dict[loc].add((i + 1) * n_cols + j - 1)
                if j < n_cols - 1:
                    adj_dict[loc].add((i + 1) * n_cols + j + 1)

    return False, adj_dict
