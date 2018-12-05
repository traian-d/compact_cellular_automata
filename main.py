import topologies as top
import rules as rules
import starting_patterns as sp
import os
import time


topology = top.make_eight_neighbor_torus(20, 20)
topology.apply_state(sp.conway_glider(20, 20, 1))

for i in range(500):
    topology.apply_rule(rules.conway_game_of_life)
    print(topology)
    time.sleep(0.08)
    os.system('clear')

