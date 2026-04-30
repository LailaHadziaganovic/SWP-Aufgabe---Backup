"""
aufgabe 7 - grafische aufbereitung mit matplotlib

hier wird das bisektionsverfahren grafisch dargestellt.
es werden zwei diagramme gezeigt:

1. aktuelle genauigkeit je iterationsschritt
2. aktuelle lösung x je iterationsschritt

getestet wird mit der wurzel-funktion:
x^2 - n = 0
"""


import matplotlib.pyplot as plt
from typing import Callable



def mache_funktion(n: float) -> Callable[[float], float]:
    """
    gibt die funktion f(x) = x^2 - n zurück
    """


    def funktion(x: float) -> float:
        return x**2 - n


    return funktion



def bisektion_mit_verlauf(
    funktion: Callable[[float], float],
    a: float,
    b: float,
    toleranz: float = 1e-8,
    max_iterationen: int = 1000,
) -> tuple[list[float], list[float]]:
    """
    führt die bisektion aus und speichert
    genauigkeit und lösung pro schritt
    """


    if a >= b:
        raise ValueError("a muss kleiner als b sein")


    fa = funktion(a)
    fb = funktion(b)


    if fa * fb > 0:
        raise ValueError("intervall enthält keine sichere nullstelle")


    genauigkeit_verlauf = []
    loesung_verlauf = []


    for _ in range(max_iterationen):
        m = (a + b) / 2
        fm = funktion(m)


        genauigkeit_verlauf.append(abs(fm))
        loesung_verlauf.append(m)


        if abs(fm) < toleranz or abs(b - a) < toleranz:
            return genauigkeit_verlauf, loesung_verlauf


        if fa * fm < 0:
            b = m
            fb = fm
        else:
            a = m
            fa = fm


    raise RuntimeError("zu viele iterationen, keine lösung gefunden")



def visualisiere_bisektion(n: float) -> None:
    """
    erstellt die diagramme für aufgabe 7
    """


    funktion = mache_funktion(n)
    genauigkeit, loesung = bisektion_mit_verlauf(funktion, 0, n)


    analytische_loesung = n**0.5
    schritte = list(range(1, len(genauigkeit) + 1))


    fig, achsen = plt.subplots(2, 1, figsize=(10, 8))


    achsen[0].plot(schritte, genauigkeit, marker="o", color="blue")
    achsen[0].set_title("aktuelle genauigkeit je iterationsschritt")
    achsen[0].set_xlabel("iterationsschritt")
    achsen[0].set_ylabel("|f(x)|")
    achsen[0].grid(True)


    achsen[1].plot(schritte, loesung, marker="o", color="green", label="numerische lösung")
    achsen[1].axhline(
        y=analytische_loesung,
        color="red",
        linestyle="--",
        label="analytische lösung",
    )
    achsen[1].set_title("aktuelle lösung x je iterationsschritt")
    achsen[1].set_xlabel("iterationsschritt")
    achsen[1].set_ylabel("x")
    achsen[1].grid(True)
    achsen[1].legend()


    plt.tight_layout()
    plt.show()



def main() -> None:
    """
    startet die visualisierung
    """


    try:
        visualisiere_bisektion(25)
    except Exception as fehler:
        print(f"fehler: {fehler}")



if __name__ == "__main__":
    main()