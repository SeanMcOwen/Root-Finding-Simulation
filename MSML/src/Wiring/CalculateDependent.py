calculate_dependent_blocks = []

calculate_dependent_blocks.append(
    {
        "name": "Calculate Dependent Variables Block",
        "components": [
            "Calculate Y Block",
            "Calculate Y Prime Block",
            "Increment Iteration Step Mechanism",
        ],
        "description": "Block which updates the Y, Y Prime, and the iteration step.",
        "constraints": [],
        "type": "Parallel",
    }
)
