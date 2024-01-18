from .Simulation import simulation_wiring
from .CalculateY import calculate_y_wiring
from .CalculateYPrime import calculate_y_prime_wiring
from .CalculateDependent import calculate_dependent_blocks
from .Iteration import iteration_wiring
from .RootFinding import root_finding_blocks

wiring = []
wiring.extend(calculate_y_wiring)
wiring.extend(calculate_y_prime_wiring)
wiring.extend(calculate_dependent_blocks)
wiring.extend(iteration_wiring)
wiring.extend(root_finding_blocks)


wiring.extend(simulation_wiring)
