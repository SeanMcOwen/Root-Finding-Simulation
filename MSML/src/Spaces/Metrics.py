from typing import TypedDict
from ..Types import SecondsType
from datetime import datetime


computation_time_metric_space = TypedDict("Computation Time Metric Space", {"simulation_time": datetime,
                                              "computation_time": SecondsType,
                                              "action_name": str})


