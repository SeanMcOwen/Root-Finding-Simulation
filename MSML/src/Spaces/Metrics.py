from datetime import datetime


computation_time_metric_space = {
    "name": "Computation Time Metric Space",
    "schema": {
        "simulation_time": "Seconds Type",
        "computation_time": "Seconds Type",
        "action_name": "Action Name Type",
    },
}


state_metric_space = {
    "name": "State Metric Space",
    "schema": {
        "simulation_time": "Seconds Type",
        "x": "X Type",
        "y": "Objective Value Type",
        "y_prime": "Objective Derivative Value Type",
        "iteration_step": "Number of Iterations Type",
    },
}

metric_spaces = [computation_time_metric_space, state_metric_space]
