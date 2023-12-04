from ..Spaces import update_x_space, dummy_space1

update_x_mechanism = {
    "name": "Update X",
    "description": "Mechanism for update to the x value",
    "constraints": [],
    "logic": "",
    "domain": [update_x_space],
    "parameters_used": [],
}

increment_iteration_step_mechanism = {
    "name": "Increment Iteration Step Mechanism",
    "description": "Mechanism for incrementing the iteration step by 1",
    "constraints": [],
    "logic": "state['iteration_step'] += 1",
    "domain": [dummy_space1],
    "parameters_used": [],
}

set_simulation_time_mechanism = {
    "name": "Set Simulation Time Mechanism",
    "description": "Mechanism for setting the current time of the simulation",
    "constraints": [],
    "logic": "state['simulation_time'] = now()",
    "domain": [dummy_space1],
    "parameters_used": [],
}
