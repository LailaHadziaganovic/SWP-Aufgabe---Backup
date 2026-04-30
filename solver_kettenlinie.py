import numpy as np
from typing import Callable

# bisektions-solver (hier definiert, damit die datei alleine läuft)
def bisektion(funktion: Callable[[float], float], a: float, b: float, tol: float) -> float:
    """findet die nullstelle mit bisektion."""
    while abs(b - a) > tol:
        m: float = (a + b) / 2
        if funktion(a) * funktion(m) < 0:
            b = m
        else:
            a = m
    return (a + b) / 2

def f_kettenlinie(a: float) -> float:
    """nullstellen-funktion für den krümmungsradius a"""
    # formel: a * cosh(50/a) - a = 10
    return a * np.cosh(50 / a) - a - 10

# berechnung krümmungsradius
# nutzen des intervalls 50 bis 200
radius_a: float = bisektion(f_kettenlinie, 50, 200, 1e-8)

# berechnung leitungslänge mi gefundener lösung
leitung_l: float = 2 * radius_a * np.sinh(100 / (2 * radius_a))

# ausgabe protokoll
print(f"krümmungsradius a: {radius_a:.4f} m")
print(f"leitungslänge l: {leitung_l:.4f} m")