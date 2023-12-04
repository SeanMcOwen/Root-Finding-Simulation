from typing import TypedDict
from ..Types import XType, ObjectiveValueType, ObjectiveDerivativeValueType


update_x_space = TypedDict(
    "Update X Space",
    {
        "x": XType,
    },
)

update_y_space = TypedDict(
    "Update Y Space",
    {
        "y": ObjectiveValueType,
    },
)
update_y_prime_space = TypedDict(
    "Update Y Prime Space",
    {
        "y_prime": ObjectiveDerivativeValueType,
    },
)
