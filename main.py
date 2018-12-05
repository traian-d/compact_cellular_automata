import topologies as top
import rules as rules
import starting_patterns as sp
import os
import time


def run_game(topology_function, rule, starting_pattern, n_rows, n_cols, start_pos, iterations):
    topology = topology_function(n_rows, n_cols)
    topology.apply_state(starting_pattern(n_rows, n_cols, start_pos))
    for i in range(iterations):
        topology.apply_rule(rule)
        print(topology)
        time.sleep(0.02)
        os.system('clear')


# run_game(top.eight_neighbor_torus, rules.conway_game_of_life, sp.conway_glider, 50, 50, 1, 500)
run_game(top.eight_neighbor_torus, rules.conway_game_of_life, sp.acorn, 50, 50, 570, 500)



