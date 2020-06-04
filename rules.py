
def conway_game_of_life(adj_dict, cell_values):
    new_cell_values = []
    for i in range(len(cell_values)):
        new_val = cell_values[i]
        live_neighbors = 0
        for neighbor in adj_dict[i]:
            live_neighbors += cell_values[neighbor]
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


def sierpinski_triangle(adj_dict, cell_values):
    new_cell_values = []
    for i in range(len(cell_values)):
        new_val = 0
        if len(adj_dict[i]) < 2:
            new_cell_values.append(new_val)
            continue
        left_neigh = adj_dict[i][0]
        right_neigh = adj_dict[i][1]
        if cell_values[left_neigh] + cell_values[i] + cell_values[right_neigh] == 1:
            new_val = 1
        new_cell_values.append(new_val)
    return new_cell_values


def ibm_may2020(adj_dict, cell_state):
    new_cell_state = cell_state
    for cell in adj_dict:
        live_neighbors = 0
        nb = adj_dict[cell]
        if cell_state & nb[0] > 0:
            live_neighbors += 1
        if cell_state & nb[1] > 0:
            live_neighbors += 1
        if cell_state & nb[2] > 0:
            live_neighbors += 1
        if cell_state & nb[3] > 0:
            live_neighbors += 1

        if 0 < live_neighbors < 3 and cell_state & cell == 0:
            new_cell_state |= cell
        elif live_neighbors != 3:
            if new_cell_state & cell > 0:
                new_cell_state -= cell
    return new_cell_state


def rule_factory(birth_neighs, live_neighs):
    def dynamic_rule(adj_dict, cell_state):
        new_cell_state = cell_state
        for cell in adj_dict:
            live_neighbors = 0
            for neighbor in adj_dict[cell]:
                if cell_state & neighbor > 0:
                    live_neighbors += 1
            if live_neighbors in birth_neighs and cell_state & cell == 0:
                new_cell_state |= cell
            elif live_neighbors not in live_neighs:
                if new_cell_state & cell > 0:
                    new_cell_state -= cell
        return new_cell_state
    return dynamic_rule


