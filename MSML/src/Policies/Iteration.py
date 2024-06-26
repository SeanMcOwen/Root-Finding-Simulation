constant_iters = {
    "name": "Constant Iterations Policy Option",
    "description": "A policy option which runs a constant number of iterations for any simulation.",
    "logic": """If state["iteration_step"] < params["max_iterations"], call the iteration policy, otherwise terminate""",
}

tolerance_stopping = {
    "name": "Tolerance Policy Option",
    "description": "A policy option which runs a constant number of iterations for any simulation unless abs(y) is less than a tolerance.",
    "logic": """If state["iteration_step"] < params["max_iterations"] and abs(state["y"]) > params["tolerance"], call the iteration policy, otherwise terminate""",
}

iteration_controller_policy = {
    "name": "Iteration Controller Policy",
    "description": "The policy which controls whether another iteration should take place in a simulation.",
    "constraints": [],
    "policy_options": [constant_iters, tolerance_stopping],
    "domain": [],
    "codomain": [],
    "parameters_used": ["max_iterations"],
    "metrics_used": [],
}


iteration_policy = {
    "name": "Iteration Policy",
    "description": "The policy which produces one iteration of the root finding algorithm.",
    "constraints": [],
    "policy_options": [],
    "domain": [],
    "codomain": ["Update X Space", "Computation Time Metric Space"],
    "parameters_used": ["root_finding_method"],
    "metrics_used": [],
}


calculate_y_policy_basic = {
    "name": "Calculate Y Policy Basic",
    "description": "Basic solving.",
    "logic": """y = params["f"](state["x"])""",
}


calculate_y_policy = {
    "name": "Calculate Y Policy",
    "description": "The policy which calculates the value for f.",
    "constraints": [],
    "policy_options": [calculate_y_policy_basic],
    "domain": [
        "Empty Space",
    ],
    "codomain": ["Update Y Space", "Computation Time Metric Space"],
    "parameters_used": ["f"],
    "metrics_used": [],
}

calculate_y_prime_policy_basic = {
    "name": "Calculate Y Prime Policy Basic",
    "description": "Basic solving.",
    "logic": """y_prime = params["f_prime"](state["X"])""",
}


calculate_y_prime_policy = {
    "name": "Calculate Y Prime Policy",
    "description": "The policy which calculates the value for the derivative of f.",
    "constraints": [],
    "policy_options": [calculate_y_prime_policy_basic],
    "domain": [],
    "codomain": ["Update Y Prime Space", "Computation Time Metric Space"],
    "parameters_used": ["f_prime"],
    "metrics_used": [],
}

iteration_policies = [
    iteration_controller_policy,
    iteration_policy,
    calculate_y_policy,
    calculate_y_prime_policy,
]
