import numpy as np
import sympy as sp
def evaluate(expr:str,x:float)->float:
    symbol=sp.symbols('x')
    return float(sp.N(sp.sympify(expr).subs(symbol,x)))
def array_mean(values:list[float])->float:
    return float(np.mean(values))
