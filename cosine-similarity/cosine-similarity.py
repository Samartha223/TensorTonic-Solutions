import numpy as np
import math

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    n=len(a)
    dot_product=0

    for i in range(n):
        dot_product=dot_product+(a[i]*b[i])

    squarred_x = 0
    squarred_y=0
    for i in range(n):
        squarred_x=squarred_x+a[i]**2
        squarred_y=squarred_y+b[i]**2

    rmse_x=math.sqrt(squarred_x)
    rmse_y=math.sqrt(squarred_y)

    if rmse_x ==0 or rmse_y==0:
        return 0
    result=dot_product/(rmse_x*rmse_y)
    return result
    