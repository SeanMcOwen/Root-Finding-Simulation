from .Dummy import dummy_mechanism
from .Iteration import (
    update_x_mechanism,
    increment_iteration_step_mechanism,
    set_simulation_time_mechanism,
    update_y_mechanism,
    update_y_prime_mechanism,
)
from .Metrics import log_computation_time_metric_mechanism

mechanism = {
    "Dummy Mechanism": dummy_mechanism,
    "Update X Mechanism": update_x_mechanism,
    "Log Computation Time Metric Mechanism": log_computation_time_metric_mechanism,
    "Increment Iteration Step Mechanism": increment_iteration_step_mechanism,
    "Set Simulation Time Mechanism": set_simulation_time_mechanism,
    "Update Y Mechanism": update_y_mechanism,
    "Update Y Prime Mechanism": update_y_prime_mechanism,
}
