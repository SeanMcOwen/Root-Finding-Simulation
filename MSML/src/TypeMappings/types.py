from typing import Union, Literal

mapping = {
    "NumberIterationsType": int,
    "ObjectiveValueType": float,
    "ObjectiveDerivativeValueType": float,
    "RootFindingMethodType": Union[
        Literal["Bisection"],
        Literal["Newton"],
        Literal["Secant"],
        Literal["Steffensen"],
    ],
    "ObjectiveFunctionType": callable,
    "ObjectiveFunctionDerivativeType": callable,
    "XType": float,
    "SecondsType": float,
    "ActionNameType": str,
}
