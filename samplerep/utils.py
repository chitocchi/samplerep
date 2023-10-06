"""General utilities.
"""

from typing import Union

import numpy as np


def square(value : Union[int, float, np.ndarray]) -> Union[float, np.ndarray]:
    """Return the square of a given number.

    This will accept any imput that support the ** operators, including
    integers, floating point numbers and numpy array.

    The function will raise a TypeError for incompatible types (e.g.,
    string).

    Arguments
    ---------
    value : number
        The input value to square.

    Return
    ------
        The square of the input value. : float
    """
    return value**2.