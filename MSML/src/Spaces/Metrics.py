from ..Types import SecondsType, XType, ObjectiveValueType, ObjectiveDerivativeValueType
from datetime import datetime


computation_time_metric_space = {
    "name": "Computation Time Metric Space",
    "schema": {
        "simulation_time": datetime,
        "computation_time": SecondsType,
        "action_name": str,
    },
}


state_metric_space = {
    "name": "State Metric Space",
    "schema": {
        "simulation_time": datetime,
        "x": XType,
        "y": ObjectiveValueType,
        "y_prime": ObjectiveDerivativeValueType,
        "iteration_step": int,
    },
}

metric_spaces = [computation_time_metric_space, state_metric_space]
