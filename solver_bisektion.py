"""
aufgabe 5 - bisektionsverfahren

ich löse hier nullstellen mit dem bisektionsverfahren.
für den test nehme ich die wurzel-funktion aus aufgabe 1.
"""

from typing import Callable


def mache_funktion(n: float) -> Callable[[float], float]:
    """
    gibt die funktion f(x) = x^2 - n zurück
    """

    def funktion(x: float) -> float:
        return x**2 - n

    return funktion


def bisektion(
    funktion: Callable[[float], float],
    a: float,
    b: float,
    toleranz: float = 1e-8,
    max_iterationen: int = 1000,
) -> float:
    """
    berechnet mit dem bisektionsverfahren eine nullstelle
    """

    fa = funktion(a)
    fb = funktion(b)

    if fa == 0:
        return a
    if fb == 0:
        return b

    if fa * fb > 0:
        raise ValueError("kein vorzeichenwechsel im intervall gefunden")

    for _ in range(max_iterationen):
        m = (a + b) / 2
        fm = funktion(m)

        if abs(fm) < toleranz or abs(b - a) < toleranz:
            return m

        if fa * fm < 0:
            b = m
            fb = fm
        else:
            a = m
            fa = fm

    raise RuntimeError("zu viele iterationen, keine lösung gefunden")


def teste_wert(n: float) -> None:
    """
    testet die bisektion für x^2 - n = 0
    """

    try:
        if n < 0:
            raise ValueError("n darf nicht negativ sein")

        funktion = mache_funktion(n)
        näherung = bisektion(funktion, 0, n)
        analytisch = n**0.5
        fehler = abs(näherung - analytisch)

        print(f"\nwert n = {n}")
        print(f"numerische lösung : {näherung}")
        print(f"analytische lösung: {analytisch}")
        print(f"abweichung        : {fehler}")

    except Exception as fehlertext:
        print(f"fehler bei n = {n}: {fehlertext}")


def main() -> None:
    """
    startet die tests für aufgabe 5
    """

    testwerte = [25, 81, 144]

    print("test vom bisektionsverfahren")
    print("-" * 40)

    for wert in testwerte:
        teste_wert(wert)


if __name__ == "__main__":
    main()