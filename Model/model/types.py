import typing

NumberIterationsType = int
ObjectiveValueType = float
ObjectiveDerivativeValueType = float
RootFindingMethodType = typing.Union[typing.Literal['Bisection'], typing.Literal['Newton'], typing.Literal['Secant'], typing.Literal['Steffensen']]
ObjectiveFunctionType = callable
ObjectiveFunctionDerivativeType = callable
XType = float
SecondsType = float
ActionNameType = str
