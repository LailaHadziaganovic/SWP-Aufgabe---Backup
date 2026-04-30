from typing import Callable

def p4(x: float) -> float:
    """polynomfunktion"""
    return 2*x + x**2 + 3*x**3 - x**4


def bisektion_mit_zaehler(funktion: Callable[[float], float], a: float, b: float, toleranz: float) -> int:
    """Führt die bisektion aus und zähltdchritte"""
    schritte: int = 0
    while abs(b - a) > toleranz:
        m: float = (a + b) / 2
        # prüft, in welcher intervallhälfte die nullstelle liegt
        if funktion(a) * funktion(m) < 0:
            b = m
        else:
            a = m
        schritte += 1
    return schritte


# TESt
for eps in [1e-2, 1e-8]:
    anzahl: int = bisektion_mit_zaehler(p4, 3, 4, eps)
    print(f"genauigkeit {eps}: {anzahl} iterationen")