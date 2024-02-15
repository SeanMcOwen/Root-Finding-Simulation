from typing import NewType, Union

NumberOfIterationsType = {"name": "Number of Iterations Type", "type": int, "notes": ""}
ObjectiveValueType = {"name": "Objective Value Type", "type": float, "notes": ""}


ObjectiveDerivativeValueType = {
    "name": "Objective Derivative Value Type",
    "type": float,
    "notes": "",
}
RootFindingMethodType = {
    "name": "Root Finding Method Type",
    "type": Union["Bisection", "Newton", "Secant", "Steffensen"],
    "notes": "",
}
ObjectiveFunctionType = {
    "name": "Objective Function Type",
    "type": callable,
    "notes": "",
}
ObjectiveFunctionDerivativeType = {
    "name": "Objective Function Derivative Type",
    "type": callable,
    "notes": "",
}
XType = {"name": "X Type", "type": float, "notes": ""}
SecondsType = {"name": "Seconds Type", "type": float, "notes": ""}
ActionNameType = {"name": "Action Name Type", "type": str, "notes": ""}
