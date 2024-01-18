from .Simulation import simulation_wiring
from .CalculateY import calculate_y_wiring

wiring = []
wiring.extend(calculate_y_wiring)
wiring.extend(simulation_wiring)
