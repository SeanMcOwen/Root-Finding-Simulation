from ..Types import (
    NumberOfIterationsType,
    ObjectiveValueType,
    RootFindingMethodType,
    ObjectiveFunctionType,
    ObjectiveFunctionDerivativeType,
)

iteration_parameter_set = {
    "name": "Dummy Parameter Set",
    "notes": "",
    "parameters": [
        {
            "variable_type": NumberOfIterationsType,
            "name": "max_iterations",
            "description": "The maximum number of iterations for the simulation",
            "symbol": None,
            "domain": None,
            "parameter_class": "system",
        },
        {
            "variable_type": ObjectiveValueType,
            "name": "tolerance",
            "description": "The tolerance to determine if iteartions can stop",
            "symbol": None,
            "domain": None,
            "parameter_class": "system",
        },
        {
            "variable_type": ObjectiveFunctionType,
            "name": "f",
            "description": "The objective function",
            "symbol": None,
            "domain": None,
            "parameter_class": "behavioral",
        },
        {
            "variable_type": ObjectiveFunctionDerivativeType,
            "name": "f_prime",
            "description": "The objective function derivative",
            "symbol": None,
            "domain": None,
            "parameter_class": "behavioral",
        },
        {
            "variable_type": RootFindingMethodType,
            "name": "root_finding_method",
            "description": "The functional parameterization for the root finding method to use",
            "symbol": None,
            "domain": None,
            "parameter_class": "functional",
        },
    ],
}
