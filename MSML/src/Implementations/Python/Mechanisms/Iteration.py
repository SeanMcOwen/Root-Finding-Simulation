import time


def update_x_mechanism(state, params, spaces):
    x = spaces[0]["x"]
    state["X"] = 0


def set_simulation_time_mechanism(state, params, spaces):
    current_time = time.time()
    state["t"] = current_time
