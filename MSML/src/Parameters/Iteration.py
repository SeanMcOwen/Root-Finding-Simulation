from ..Types import NumberOfIterationsType, ObjectiveValueType

iteration_parameter_set = {"name": "Dummy Parameter Set",
                       "notes": "",
                       "parameters": [{"variable_type": NumberOfIterationsType,
                                       "name": "max_iterations",
                                       "description": "The maximum number of iterations for the simulation",
                                       "symbol": None,
                                       "domain": None
                                       },
                                       {"variable_type": ObjectiveValueType,
                                       "name": "tolerance",
                                       "description": "The tolerance to determine if iteartions can stop",
                                       "symbol": None,
                                       "domain": None
                                       }]}