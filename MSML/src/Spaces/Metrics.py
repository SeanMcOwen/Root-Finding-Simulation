from typing import TypedDict
from ..Types import SecondsType, XType, ObjectiveValueType, ObjectiveDerivativeValueType
from datetime import datetime


computation_time_metric_space = TypedDict(
    "Computation Time Metric Space",
    {"simulation_time": datetime, "computation_time": SecondsType, "action_name": str},
)


state_metric_space = TypedDict(
    "State Metric Space",
    {
        "simulation_time": datetime,
        "x": XType,
        "y": ObjectiveValueType,
        "y_prime": ObjectiveDerivativeValueType,
        "iteration_step": int,
    },
)
