import time


def update_x_mechanism(state, params, spaces):
    x = spaces[0]["x"]
    state["X"] = x


def set_simulation_time_mechanism(state, params, spaces):
    current_time = time.time()
    state["t"] = current_time


def update_y_mechanism(state, params, spaces):
    state["Y"] = spaces[0]["y"]


def update_y_prime_mechanism(state, params, spaces):
    state["Y Prime"] = spaces[0]["y_prime"]


def log_computation_time_mechanism(state, params, spaces):
    pass
