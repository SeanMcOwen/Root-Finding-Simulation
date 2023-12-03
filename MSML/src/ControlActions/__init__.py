from .Dummy import dummy_control_action
from .Iteration import initialization_control_action

control_actions = {
    "Dummy Control Action": dummy_control_action,
    "Initialization Control Action": initialization_control_action
}
