initialization_control_action_option1 = {
    "name": "Set X = 0",
    "description": "Simply sets the starting value of X to be equal to 0.",
    "logic": "STATE[0].X = 0",
}

initialization_control_action = {
    "name": "Initialization Control Action",
    "description": "Control action to begin the simulation",
    "constraints": [],
    "control_action_options": [initialization_control_action_option1],
    "codomain": [
        "Update X Space",
    ],
    "parameters_used": [],
}
