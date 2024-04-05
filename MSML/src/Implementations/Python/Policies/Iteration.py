from time import time


def calculate_y_policy(state, params, spaces):
    start = time()
    y = params["f"](state["X"])
    end = time()

    return ({"y": y}, {})
