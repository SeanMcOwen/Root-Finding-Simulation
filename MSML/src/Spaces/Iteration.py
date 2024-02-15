from typing import TypedDict
from ..Types import XType, ObjectiveValueType, ObjectiveDerivativeValueType


update_x_space = {
    "name": "Update X Space",
    "schema": {
        "x": XType,
    },
}

none_space = {
    "name": "None Space",
    "schema": {},
}


update_y_space = {
    "name": "Update Y Space",
    "schema": {
        "y": "Objective Value Type",
    },
}

update_y_prime_space = {
    "name": "Update Y Prime Space",
    "schema": {
        "y_prime": "Objective Derivative Value Type",
    },
}

iteration_spaces = [update_x_space, update_y_space, update_y_prime_space, none_space]
