iteration_transmission_channels = []

iteration_transmission_channels.append(
    {
        "origin": "Iteration Controller Policy",
        "target": "Iteration Policy",
        "space": ("None Space",),
        "optional": True,
    }
)

iteration_transmission_channels.append(
    {
        "origin": "Iteration Policy",
        "target": "Update X Mechanism",
        "space": ("Update X Space"),
        "optional": False,
    }
)

iteration_transmission_channels.append(
    {
        "origin": "Iteration Policy",
        "target": "Log Computation Time Metric Mechanism",
        "space": ("Computation Time Metric Space",),
        "optional": False,
    }
)

iteration_transmission_channels.append(
    {
        "origin": "Iteration Policy",
        "target": "Calculate Y Policy",
        "space": ("None Space",),
        "optional": False,
    }
)

iteration_transmission_channels.append(
    {
        "origin": "Calculate Y Policy",
        "target": "Log Computation Time Metric Mechanism",
        "space": ("Computation Time Metric Space",),
        "optional": False,
    }
)

iteration_transmission_channels.append(
    {
        "origin": "Calculate Y Policy",
        "target": "Calculate Y Prime Policy",
        "space": ("None Space",),
        "optional": False,
    }
)

iteration_transmission_channels.append(
    {
        "origin": "Calculate Y Prime Policy",
        "target": "Log Computation Time Metric Mechanism",
        "space": ("Computation Time Metric Space",),
        "optional": False,
    }
)


iteration_transmission_channels.append(
    {
        "origin": "Calculate Y Prime Policy",
        "target": "Increment Iteration Step Mechanism",
        "space": ("None Space",),
        "optional": False,
    }
)

iteration_transmission_channels.append(
    {
        "origin": "Calculate Y Prime Policy",
        "target": "Set Simulation Time Mechanism",
        "space": ("None Space",),
        "optional": False,
    }
)

iteration_transmission_channels.append(
    {
        "origin": "Calculate Y Policy",
        "target": "Update Y Mechanism",
        "space": ("None Space",),
        "optional": False,
    }
)

iteration_transmission_channels.append(
    {
        "origin": "Calculate Y Prime Policy",
        "target": "Update Y Prime Mechanism",
        "space": ("None Space",),
        "optional": False,
    }
)

iteration_transmission_channels.append(
    {
        "origin": "Calculate Y Prime Policy",
        "target": "Log State Metric Mechanism",
        "space": ("None Space",),
        "optional": False,
    }
)

iteration_transmission_channels.append(
    {
        "origin": "Calculate Y Prime Policy",
        "target": "Iteration Controller Policy",
        "space": ("None Space",),
        "optional": False,
    }
)
