root_finding_blocks = []
root_finding_blocks.append(
    {
        "name": "Root Finding Block",
        "components": [
            "Iteration Controller Policy",
            "Iteration Block",
            "Calculate Dependent Variables Block",
            "Set Simulation Time Mechanism",
        ],
        "description": "Block which handles all aspects of using the root finding algorithm.",
        "constraints": [],
        "type": "Stack",
    }
)
