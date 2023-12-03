constant_iters = {"name": "Constant Iterations Policy Option",
                                 "description": "A policy option which runs a constant number of iterations for any simulation.",
                                 "logic": """If state["iteration_step"] < params["max_iterations"], call the iteration policy, otherwise terminate"""
                                 }

tolerance_stopping = {"name": "Tolerance Policy Option",
                                 "description": "A policy option which runs a constant number of iterations for any simulation unless abs(y) is less than a tolerance.",
                                 "logic": """If state["iteration_step"] < params["max_iterations"] and abs(state["y"]) > params["tolerance"], call the iteration policy, otherwise terminate"""
                                 }

iteration_controller_policy = {"name": "Iteration Controller Policy",
                        "description": "The policy which controls whether another iteration should take place in a simulation.",
                        "constraints": [],
                        "policy_options": [constant_iters, tolerance_stopping],
                        "domain": [],
                        "codomain": [],
                        "parameters_used": ["max_iterations"]}
