from typing import TypedDict
from ..Types import XType, ObjectiveValueType, ObjectiveDerivativeValueType


update_x_space = {
    "name": "Update X Space",
    "schema": {
        "x": XType,
    },
}


update_y_space = {
    "name": "Update Y Space",
    "schema": {
        "y": ObjectiveValueType,
    },
}

update_y_prime_space = {
    "name": "Update Y Prime Space",
    "schema": {
        "y_prime": ObjectiveDerivativeValueType,
    },
}

iteration_spaces = [update_x_space, update_y_space, update_y_prime_space]
