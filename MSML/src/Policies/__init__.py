from .Dummy import dummy_policy
from .Iteration import iteration_controller_policy, iteration_policy
policies = {
    "Dummy Policy": dummy_policy,
    "Iteration Controller Policy": iteration_controller_policy,
    "Iteration Policy": iteration_policy
}
