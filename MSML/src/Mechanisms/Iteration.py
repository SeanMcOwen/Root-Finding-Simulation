update_x_mechanism = {
    "name": "Update X Mechanism",
    "description": "Mechanism for update to the x value",
    "constraints": [],
    "logic": "",
    "domain": ("Update X Space",),
    "parameters_used": [],
}

update_y_mechanism = {
    "name": "Update Y Mechanism",
    "description": "Mechanism for an update to the y value",
    "constraints": [],
    "logic": "",
    "domain": ("Update Y Space",),
    "parameters_used": [],
}

update_y_prime_mechanism = {
    "name": "Update Y Prime Mechanism",
    "description": "Mechanism for an update to the y_prime value",
    "constraints": [],
    "logic": "",
    "domain": ("Update Y Prime Space",),
    "parameters_used": [],
}

increment_iteration_step_mechanism = {
    "name": "Increment Iteration Step Mechanism",
    "description": "Mechanism for incrementing the iteration step by 1",
    "constraints": [],
    "logic": "state['iteration_step'] += 1",
    "domain": ("Empty Space",),
    "parameters_used": [],
}

set_simulation_time_mechanism = {
    "name": "Set Simulation Time Mechanism",
    "description": "Mechanism for setting the current time of the simulation",
    "constraints": [],
    "logic": "state['simulation_time'] = now()",
    "domain": ("Empty Space",),
    "parameters_used": [],
}
