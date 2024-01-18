root_finding_blocks = []
root_finding_blocks.append(
    {
        "name": "Calculate Y Prime Block",
        "components": ["Calculate Y Prime Policy", "Calculate Y Prime Parallel Block"],
        "description": "Block which calculates and updates the Y prime value.",
        "constraints": [],
        "type": "Stack",
    }
)
