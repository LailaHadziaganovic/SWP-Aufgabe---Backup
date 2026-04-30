"""
aufgabe 6 - newton-raphson-verfahren

ich löse hier nullstellen mit dem newton-verfahren.
getestet wird wieder die wurzel-funktion:
x^2 - n = 0
"""

from typing import Callable


def mache_funktion(n: float) -> Callable[[float], float]:
    """
    gibt die funktion f(x) = x^2 - n zurück
    """

    def funktion(x: float) -> float:
        return x**2 - n

    return funktion


def mache_ableitung() -> Callable[[float], float]:
    """
    gibt die ableitung f'(x) = 2x zurück
    """

    def ableitung(x: float) -> float:
        return 2 * x

    return ableitung


def newton(
    funktion: Callable[[float], float],
    ableitung: Callable[[float], float],
    startwert: float,
    toleranz: float = 1e-8,
    max_iterationen: int = 1000,
) -> float:
    """
    berechnet nullstelle mit dem newton-verfahren
    """

    x = startwert

    for _ in range(max_iterationen):
        fx = funktion(x)
        f_ableitung = ableitung(x)

        if f_ableitung == 0:
            raise ZeroDivisionError("ableitung ist 0, newton nicht möglich")

        x_neu = x - (fx / f_ableitung)

        if abs(x_neu - x) < toleranz:
            return x_neu

        x = x_neu

    raise RuntimeError("zu viele iterationen, keine lösung gef")


def teste_wert(n: float) -> None:
    """
    testet newton-verfahren: für x^2 - n = 0
    """

    try:
        if n < 0:
            raise ValueError("n darf nicht negativ sein")

        funktion = mache_funktion(n)
        ableitung = mache_ableitung()
        näherung = newton(funktion, ableitung, startwert=n / 2)
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
    startet die tests für aufgabe 6
    """

    testwerte = [25, 81, 144]

    print("test vom newton-verfahren")
    print("-" * 40)

    for wert in testwerte:
        teste_wert(wert)


if __name__ == "__main__":
    main()