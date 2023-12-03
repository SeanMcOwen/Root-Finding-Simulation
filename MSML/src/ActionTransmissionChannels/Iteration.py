from ..Spaces import none_space, update_x_space, computation_time_metric_space, dummy_space1

iteration_transmission_channels = []

iteration_transmission_channels.append({"origin": "Iteration Controller Policy",
                                        "target": "Iteration Policy",
                                        "space": none_space,
                                        "optional": True})

iteration_transmission_channels.append({"origin": "Iteration Policy",
                                        "target": "Update X Mechanism",
                                        "space": update_x_space,
                                        "optional": False})

iteration_transmission_channels.append({"origin": "Iteration Policy",
                                        "target": "Log Computation Time Metric Mechanism",
                                        "space": computation_time_metric_space,
                                        "optional": False})

iteration_transmission_channels.append({"origin": "Iteration Policy",
                                        "target": "Calculate Y Policy",
                                        "space": dummy_space1,
                                        "optional": False})

iteration_transmission_channels.append({"origin": "Calculate Y Policy",
                                        "target": "Calculate Y Prime Policy",
                                        "space": dummy_space1,
                                        "optional": False})

