import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    # Write code here
    n=len(x)

    result=0

    for i in range(n):
        result=result+(x[i]*y[i])
    return result