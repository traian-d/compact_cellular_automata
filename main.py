import topologies as top
import rules as rules
import starting_patterns as sp
from Topology import Topology
import os
import time


def run_game(topology, rule, starting_pattern, n_rows, n_cols, start_pos, iterations, clear=True, sleep=0.02):
    topology.apply_state(starting_pattern(n_rows, n_cols, start_pos))
    print(topology)
    for i in range(iterations):
        topology.apply_rule(rule)
        print(topology)
        time.sleep(sleep)
        if clear:
            os.system('clear')


# run_game(top.eight_neighbor_torus, rules.conway_game_of_life, sp.conway_glider, 50, 50, 1, 500)
# run_game(top.eight_neighbor_torus(50, 50), rules.conway_game_of_life, sp.acorn, 50, 50, 570, 500)

run_game(Topology(1, 101, top.two_neighbors_ordered), rules.rule_30, sp.one_dot, 1, 101, 51, 70, False)



