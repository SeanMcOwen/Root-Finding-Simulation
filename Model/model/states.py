from .types import SecondsType, ObjectiveDerivativeValueType, XType, NumberIterationsType, ObjectiveValueType
from typing import TypedDict

GlobalState = TypedDict('Global State', {'X': XType, 'Iteration Step': NumberIterationsType, 't': SecondsType, 'Y': ObjectiveValueType, 'Y Prime': ObjectiveDerivativeValueType})

state: GlobalState = {"X": None,
"Iteration Step": None,
"t": None,
"Y": None,
"Y Prime": None,
}