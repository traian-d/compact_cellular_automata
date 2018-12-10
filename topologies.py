from Topology import Topology
from topology_functions import rectangular_four_neighbors, rectangular_four_diagonal_neighbors, top_bottom_cylinder, \
    top_bottom_diag, left_right_cylinder, left_right_diag, join_corners, two_neighbors_ordered


def eight_neighbor_grid(n_rows, n_cols):
    return Topology(n_rows, n_cols, rectangular_four_neighbors)\
           + Topology(n_rows, n_cols, rectangular_four_diagonal_neighbors)


def eight_neighbor_torus(n_rows, n_cols):
    return Topology(n_rows, n_cols, rectangular_four_neighbors)\
        + Topology(n_rows, n_cols, rectangular_four_diagonal_neighbors)\
        + Topology(n_rows, n_cols, top_bottom_cylinder) + Topology(n_rows, n_cols, top_bottom_diag)\
        + Topology(n_rows, n_cols, left_right_cylinder) + Topology(n_rows, n_cols, left_right_diag)\
        + Topology(n_rows, n_cols, join_corners)


def single_row(n_cols):
    return Topology(1, n_cols, two_neighbors_ordered)