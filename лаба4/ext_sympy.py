import sympy as sp

def test_sympy():
    x = sp.Symbol('x')
    eq = sp.Eq(x**2 - 4, 0)
    sol = sp.solve(eq, x)
    print(f"sympy: Розв'язок рівняння x^2 - 4 = 0 -> {sol}")