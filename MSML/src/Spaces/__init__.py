from .Initialization import initialization_spaces
from .Iteration import iteration_spaces
from .Metrics import metric_spaces

spaces = []
spaces.extend(initialization_spaces)
spaces.extend(iteration_spaces)
spaces.extend(metric_spaces)
