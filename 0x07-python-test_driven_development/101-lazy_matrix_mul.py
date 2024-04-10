#!/usr/bin/pyton3
import numpy as np # type: ignore

def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.

    Raises:
        ValueError: If m_a or m_b is empty, or if m_a and m_b can't be multiplied.

    Returns:
        numpy.ndarray: The resulting matrix after multiplication.
    """

    # Convert input matrices to NumPy arrays
    a = np.array(m_a)
    b = np.array(m_b)

    # Perform matrix multiplication using NumPy's dot function
    result = np.dot(a, b)

    return result
