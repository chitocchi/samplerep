import numpy as np

from samplerep.utils import square

def test_square():
    """Unit test for the square() function.
    """
    assert square(2.) == 4.
    assert square(-2.) == 4.
    assert square(0.) == 0.
    assert square(2) == 4
    assert square(-2) == 4
    assert square(0) == 0
    assert np.allclose(square(np.ones(100)), np.ones(100))