from typing import Union

mapping = {
    "NumberIterationsType": int,
    "ObjectiveValueType": float,
    "ObjectiveDerivativeValueType": float,
    "RootFindingMethodType": Union["Bisection", "Newton", "Secant", "Steffensen"],
    "ObjectiveFunctionType": callable,
    "ObjectiveFunctionDerivativeType": callable,
    "XType": float,
    "SecondsType": float,
    "ActionNameType": str,
}
