iteration_wiring = []
iteration_wiring.append(
    {
        "name": "Iteration Parallel Block",
        "components": [
            "Update X Mechanism",
            "Log Computation Time Metric Mechanism",
        ],
        "description": "Block which updates X and logs the computation time taken.",
        "constraints": [],
        "type": "Parallel",
        "mermaid_show_name": False,
    }
)
iteration_wiring.append(
    {
        "name": "Iteration Block",
        "components": ["Iteration Policy", "Iteration Parallel Block"],
        "description": "Block which calculates one iteration.",
        "constraints": [],
        "type": "Stack",
    }
)
