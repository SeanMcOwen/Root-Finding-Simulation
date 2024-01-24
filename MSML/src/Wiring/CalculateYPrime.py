calculate_y_prime_wiring = []


calculate_y_prime_wiring.append(
    {
        "name": "Calculate Y Prime Parallel Block",
        "components": [
            "Update Y Prime Mechanism",
            "Log Computation Time Metric Mechanism",
        ],
        "description": "Block which updates the Y prime value and logs the computation time it took from calculate Y prime policy.",
        "constraints": [],
        "type": "Parallel",
        "mermaid_show_name": False,
    }
)

calculate_y_prime_wiring.append(
    {
        "name": "Calculate Y Prime Block",
        "components": ["Calculate Y Prime Policy", "Calculate Y Prime Parallel Block"],
        "description": "Block which calculates and updates the Y prime value.",
        "constraints": [],
        "type": "Stack",
    }
)
