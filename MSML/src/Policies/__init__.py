from .Iteration import (
    iteration_controller_policy,
    iteration_policy,
    calculate_y_policy,
    calculate_y_prime_policy,
)

policies = {
    "Iteration Controller Policy": iteration_controller_policy,
    "Iteration Policy": iteration_policy,
    "Calculate Y Policy": calculate_y_policy,
    "Calculate Y Prime Policy": calculate_y_prime_policy,
}
