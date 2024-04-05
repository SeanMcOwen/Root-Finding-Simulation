from .types import SecondsType, XType, NumberIterationsType, ObjectiveValueType, ActionNameType, ObjectiveDerivativeValueType
from typing import TypedDict

TerminatingSpace = TypedDict('Terminating Space', {})
EmptySpace = TypedDict('Empty Space', {})
InitializationSpace = TypedDict('Initialization Space', {})
UpdateXSpace = TypedDict('Update X Space', {'x': XType})
UpdateYSpace = TypedDict('Update Y Space', {'y': ObjectiveValueType})
UpdateYPrimeSpace = TypedDict('Update Y Prime Space', {'y_prime': ObjectiveDerivativeValueType})
NoneSpace = TypedDict('None Space', {})
ComputationTimeMetricSpace = TypedDict('Computation Time Metric Space', {'simulation_time': SecondsType, 'computation_time': SecondsType, 'action_name': ActionNameType})
StateMetricSpace = TypedDict('State Metric Space', {'simulation_time': SecondsType, 'x': XType, 'y': ObjectiveValueType, 'y_prime': ObjectiveDerivativeValueType, 'iteration_step': NumberIterationsType})
