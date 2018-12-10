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


def np_plot(game, sleep=0.02):
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    states, n_rows = game.pad_states()
    for i in range(len(states)):
        ax.cla()
        ax.imshow(np.reshape(states[i], (n_rows, game.topology.n_cols)))
        ax.set_title("frame {}".format(i))
        plt.pause(sleep)


def save_gif(game, file_path, dpi=80, sleep=50):
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    states, n_rows = game.pad_states()

    def update(i):
        return ax.imshow(np.reshape(states[i], (n_rows, game.topology.n_cols)))

    from matplotlib.animation import FuncAnimation
    anim = FuncAnimation(fig, update, frames=np.arange(0, len(states)), interval=sleep)
    anim.save(file_path, dpi=dpi, writer='imagemagick')


# acorn_game = run_game(top.eight_neighbor_torus(50, 50), rules.conway_game_of_life, sp.acorn, 1261, iterations=100)
# save_gif(acorn_game, 'acorn_game.gif', 100)

# glider_torus = run_game(top.eight_neighbor_torus(25, 25), rules.conway_game_of_life, sp.conway_glider, 2, iterations=100)
# save_gif(glider_torus, 'glider_torus.gif', 100)

# glider_simple = run_game(top.eight_neighbor_grid(25, 25), rules.conway_game_of_life, sp.conway_glider, 2, iterations=100)
# save_gif(glider_simple, 'glider_simple.gif', 100)

rule30 = run_game(top.single_row(200), rules.rule_30, sp.one_dot, 101, iterations=100)
save_gif(rule30, 'rule30.gif', dpi=80, sleep=30)
