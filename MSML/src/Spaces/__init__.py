from .Dummy import dummy_space1, dummy_space2, none_space
from .Initialization import initialization_space
from .Iteration import update_x_space, update_y_space, update_y_prime_space
from .Metrics import computation_time_metric_space, state_metric_space

spaces = {
    "Dummy Space 1": dummy_space1,
    "Dummy Space 2": dummy_space2,
    "Initialization Space": initialization_space,
    "None Space": none_space,
    "Update X Space": update_x_space,
    "Computation Time Metric Space": computation_time_metric_space,
    "Update Y Space": update_y_space,
    "Update Y Prime Space": update_y_prime_space,
    "State Metric Space": state_metric_space,
}
