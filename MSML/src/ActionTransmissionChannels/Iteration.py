from ..Spaces import none_space, update_x_space

iteration_transmission_channels = []

iteration_transmission_channels.append({"origin": "Iteration Controller Policy",
                                        "target": "Iteration Policy",
                                        "space": none_space,
                                        "optional": True})

iteration_transmission_channels.append({"origin": "Iteration Policy",
                                        "target": "Update X Mechanism",
                                        "space": update_x_space,
                                        "optional": False})
