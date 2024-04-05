from .types import RootFindingMethodType, ObjectiveFunctionType, NumberIterationsType, ObjectiveValueType, ObjectiveFunctionDerivativeType
from typing import TypedDict

SystemParameters = TypedDict('SystemParameters', {'max_iterations': NumberIterationsType, 'tolerance': ObjectiveValueType})

BehavioralParameters = TypedDict('BehavioralParameters', {'f': ObjectiveFunctionType, 'f_prime': ObjectiveFunctionDerivativeType})

FunctionalParameters = TypedDict('FunctionalParameters', {'root_finding_method': RootFindingMethodType, 'FP Iteration Controller Policy': str})

Parameters = TypedDict("Parameters",{**BehavioralParameters.__annotations__,
 **FunctionalParameters.__annotations__,
**SystemParameters.__annotations__})

functional_parameters: FunctionalParameters = {"root_finding_method": None,
"FP Iteration Controller Policy": None,
}

behavioral_parameters: BehavioralParameters = {"f": None,
"f_prime": None,
}

system_parameters: SystemParameters = {"max_iterations": None,
"tolerance": None,
}

parameters: Parameters = {**behavioral_parameters, **functional_parameters, **system_parameters}