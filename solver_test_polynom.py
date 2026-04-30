def p4(x):
    return 2*x + x**2 + 3*x**3 - x**4

def bisektion_mit_zaehler(funktion, a, b, toleranz):
    schritte = 0
    while abs(b - a) > toleranz:
        m = (a + b) / 2
        if funktion(a) * funktion(m) < 0:
            b = m
        else:
            a = m
        schritte += 1
    return schritte

# Testen
for eps in [1e-2, 1e-8]:
    anzahl = bisektion_mit_zaehler(p4, 3, 4, eps)
    print(f"genauigkeit {eps}: {anzahl} iterationen")