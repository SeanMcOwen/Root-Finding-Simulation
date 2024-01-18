calculate_y_wiring = []


calculate_y_wiring.append(
    {
        "name": "Calculate Y Parallel Block",
        "components": ["Update Y Mechanism", "Log Computation Time Metric Mechanism"],
        "description": "Block which updates the Y value and logs the computation time it took from calculate Y policy.",
        "constraints": [],
        "type": "Parallel",
    }
)

calculate_y_wiring.append(
    {
        "name": "Calculate Y Block",
        "components": ["Calculate Y Policy", "Calculate Y Parallel Block"],
        "description": "Block which calculates and updates the Y value.",
        "constraints": [],
        "type": "Stack",
    }
)
