#!/usr/bin/env python3
# Copyright (C) Ryax Technologies
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from enum import Enum


class Operation(Enum):
    equal: str = "equal"
    greater: str = "greater"
    lower: str = "lower"


def handle(module_input):
    operation: Operation = module_input["operation"]
    first_value: int = module_input["first"]
    second_value: int = module_input["second"]
    result: bool = False
    if operation == "equal":
        result = first_value == second_value
    elif operation == "greater":
        result = first_value > second_value
    elif operation == "lower":
        result = first_value < second_value
    else:
        pass

    if result is True:
        return []
    else:
        return {}
