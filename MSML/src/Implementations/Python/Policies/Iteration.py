def calculate_y_policy(state, params, spaces):
    return params["f"](state["X"])
