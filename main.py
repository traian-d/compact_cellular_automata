import topologies as top
import rules as rules
import starting_patterns as sp
from Game import Game
import os
import time
import numpy as np


def run_game(topology, rule, starting_pattern, start_pos, iterations):
    game = Game(topology)
    game.append_state(starting_pattern(topology.n_rows, topology.n_cols, start_pos))
    for i in range(iterations):
        game.apply_rule(rule)
    return game


def print_states(game, sleep=0.02, clear=True):
    states = game.states_to_string()
    for state in states:
        print(state)
        time.sleep(sleep)
        if clear:
            os.system('clear')


def np_plot(game):
    import matplotlib.pyplot as plt
    from matplotlib.animation import FuncAnimation

    fig, ax = plt.subplots()

    for i in range(len(game.states)):
        ax.cla()
        ax.imshow(np.reshape(game.states[i], (game.topology.n_rows, game.topology.n_cols)))
        ax.set_title("frame {}".format(i))
        plt.pause(0.1)

    # anim = FuncAnimation(fig, update, frames=np.arange(0, len(states)), interval=200)
    # anim.save('line.gif', dpi=80, writer='imagemagick')


# run_game(top.eight_neighbor_torus, rules.conway_game_of_life, sp.conway_glider, 50, 50, 1, 500)
acorn_game = run_game(top.eight_neighbor_torus(50, 50), rules.conway_game_of_life, sp.acorn, 501, iterations=200)
# print_states(acorn_game)
np_plot(acorn_game)
# run_game(Topology(1, 241, top.two_neighbors_ordered), rules.rule_30, sp.one_dot, 1, 241, 121, 120, False)

