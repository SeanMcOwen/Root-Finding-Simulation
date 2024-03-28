def calculate_y_policy(state, params, spaces):
    return {"y": params["f"](state["X"])}
