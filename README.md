# Numerisches Lösen von Gleichungen

Projektarbeit für den Gegenstand SWP in der Klasse 3BHWI im Schuljahr 2025/26.

In diesem Projekt werden verschiedene numerische Verfahren zur Bestimmung von Nullstellen umgesetzt, getestet und angewendet. Der Schwerpunkt liegt auf dem Bisektionsverfahren sowie auf einem alternativen Lösungsverfahren nach Newton-Raphson.

## Projektinhalt

Das Projekt umfasst folgende Teile:

- Aufgabe 5: Implementierung eines Solvers mit dem Bisektionsverfahren
- Aufgabe 6: Alternative Nullstellensuche mit dem Newton-Verfahren
- Aufgabe 7: Grafische Darstellung der Nullstellenfindung mit Matplotlib
- Aufgabe 8: Genauigkeitstest mit dem Polynom P4(x) = 2x + x^2 + 3x^3 - x^4
- Aufgabe 9: Anwendung auf ein reales Problem mit einer Kettenlinie

## Dateien

- `solver_bisektion.py`  
  Solver für die Nullstellensuche mit dem Bisektionsverfahren

- `solver_newton.py`  
  Solver für die Nullstellensuche mit dem Newton-Verfahren

- `solver_visualisierung.py`  
  Grafische Darstellung der Iterationen

- `solver_test_polynom.py`  
  Test der Genauigkeit mit dem gegebenen Polynom

- `solver_kettenlinie.py`  
  Berechnung des Krümmungsradius und der Leitungslänge

## Ausführung im Terminal

Die Programme können einzeln im Terminal oder in PowerShell gestartet werden.

Beispiele:

```bash
python solver_bisektion.py
python solver_newton.py
python solver_visualisierung.py
python solver_test_polynom.py
python solver_kettenlinie.py
```

Falls `python` nicht funktioniert, kann stattdessen auch `python3` verwendet werden. Die Programme sind so aufgebaut, dass sie einzeln testbar sind.

## Voraussetzungen

Für die Programme werden folgende Python-Pakete benötigt:

- numpy
- matplotlib

Installation bei Bedarf:

```bash
pip install numpy matplotlib
```

## Ziel des Projekts

Ziel dieses Projekts ist es, numerische Verfahren praktisch umzusetzen, ihre Genauigkeit zu vergleichen und ihre Anwendung an mathematischen und realen Problemen zu demonstrieren. Das Projekt verbindet Planung, Programmierung, Testung und Dokumentation.

## Autorin

Hadžiaganović Laila  
3BHWI  
SWP  
Schuljahr 2025/26