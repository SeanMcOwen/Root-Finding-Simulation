from .Dummy import dummy_mechanism
from .Iteration import (
    update_x_mechanism,
    increment_iteration_step_mechanism,
    set_simulation_time_mechanism,
)
from .Metrics import log_computation_time_metric_mechanism

mechanism = {
    "Dummy Mechanism": dummy_mechanism,
    "Update X Mechanism": update_x_mechanism,
    "Log Computation Time Metric Mechanism": log_computation_time_metric_mechanism,
    "Increment Iteration Step Mechanism": increment_iteration_step_mechanism,
    "Set Simulation Time Mechanism": set_simulation_time_mechanism,
}
