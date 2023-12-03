from typing import NewType, Union

NumberOfIterationsType = NewType("Number of Iterations Type", str)
ObjectiveValueType = NewType("Objective Value Type", float)
RootFindingMethodType = NewType("Root Finding Method Type", Union["Bisection", "Newton", "Secant", "Steffensen"])
ObjectiveFunctionType = NewType("Objective Function Type", callable)
ObjectiveFunctionDerivativeType = NewType("Objective Function Derivative Type", callable)



