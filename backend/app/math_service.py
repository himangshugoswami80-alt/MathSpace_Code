import sympy as sp
def solve(expression:str):
    x=sp.symbols('x')
    return [str(v) for v in sp.solve(sp.sympify(expression),x)]
def differentiate(expression:str):
    x=sp.symbols('x'); return str(sp.diff(sp.sympify(expression),x))
def integrate(expression:str):
    x=sp.symbols('x'); return str(sp.integrate(sp.sympify(expression),x))
