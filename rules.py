
def conway_game_of_life(adj_dict, cell_values):
    new_cell_values = []
    for i in range(len(cell_values)):
        new_val = cell_values[i]
        live_neighbors = sum([cell_values[neighbor] for neighbor in adj_dict[i]])
        if live_neighbors < 2:
            new_val = 0
        elif live_neighbors > 3:
            new_val = 0
        elif live_neighbors == 3:
            new_val = 1
        new_cell_values.append(new_val)
    return new_cell_values


def rule_30(adj_dict, cell_values):
    new_cell_values = []
    for i in range(len(cell_values)):
        new_val = 0
        if len(adj_dict[i]) < 2:
            new_cell_values.append(new_val)
            continue
        left_neigh = adj_dict[i][0]
        right_neigh = adj_dict[i][1]
        if cell_values[left_neigh] != (cell_values[i] or cell_values[right_neigh]):
            new_val = 1
        new_cell_values.append(new_val)
    return new_cell_values

