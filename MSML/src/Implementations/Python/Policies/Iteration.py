from time import time


def calculate_y_policy(state, params, spaces):
    start = time()
    y = params["f"](state["X"])
    end = time()

    return ({"y": y}, {})


def calculate_y_prime_policy(state, params, spaces):
    start = time()
    y_prime = params["f_prime"](state["X"])
    end = time()

    return ({"y_prime": y_prime}, {})
