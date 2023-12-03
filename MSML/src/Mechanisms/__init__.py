from .Dummy import dummy_mechanism
from .Iteration import update_x_mechanism
from .Metrics import log_computation_time_metric_mechanism

mechanism = {"Dummy Mechanism": dummy_mechanism,
             "Update X Mechanism": update_x_mechanism,
             "Log Computation Time Metric Mechanism": log_computation_time_metric_mechanism}
