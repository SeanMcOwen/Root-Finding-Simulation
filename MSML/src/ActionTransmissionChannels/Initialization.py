from ..Spaces import initialization_space

initialization_transmission_channels = []

initialization_transmission_channels.append({"origin": "Initialization Control Action",
                                        "target": "Iteration Controller Policy",
                                        "space": initialization_space,
                                        "optional": False})
