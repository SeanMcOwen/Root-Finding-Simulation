update_x_mechanism = {
    "name": "Update X Mechanism",
    "description": "Mechanism for update to the x value",
    "constraints": [],
    "logic": "Change the global state variable of X to be equal to DOMAIN[0].X",
    "domain": ("Update X Space",),
    "parameters_used": [],
    "updates": [("Global", "X", False)],
}

update_y_mechanism = {
    "name": "Update Y Mechanism",
    "description": "Mechanism for an update to the y value",
    "constraints": [],
    "logic": "Update the global state variable of Y to be equal to DOMAIN[0].Y",
    "domain": ("Update Y Space",),
    "parameters_used": [],
    "updates": [("Global", "Y", False)],
}

update_y_prime_mechanism = {
    "name": "Update Y Prime Mechanism",
    "description": "Mechanism for an update to the y_prime value",
    "constraints": [],
    "logic": "Update the global state variable of Y Prime to be equal to DOMAIN[0].Y Prime",
    "domain": ("Update Y Prime Space",),
    "parameters_used": [],
    "updates": [("Global", "Y Prime", False)],
}

increment_iteration_step_mechanism = {
    "name": "Increment Iteration Step Mechanism",
    "description": "Mechanism for incrementing the iteration step by 1",
    "constraints": [],
    "logic": "state['iteration_step'] += 1",
    "domain": (),
    "parameters_used": [],
    "updates": [("Global", "Iteration Step", False)],
}

set_simulation_time_mechanism = {
    "name": "Set Simulation Time Mechanism",
    "description": "Mechanism for setting the current time of the simulation",
    "constraints": [],
    "logic": "state['simulation_time'] = now()",
    "domain": (),
    "parameters_used": [],
    "updates": [("Global", "t", False)],
}
