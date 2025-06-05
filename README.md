# 🍕 Pizza-Greedy Method for the Traveling Salesman Problem (TSP)

**Pizza-Greedy Method** is a heuristic approach for solving the classic Traveling Salesman Problem (TSP), inspired by a circular “pizza slice” division of space. It offers a geographically intuitive and computationally efficient solution by combining a radial sector approach with a greedy algorithm inside each sector.

## 💡 Concept

The route is based on the following core principles::

1. Define a central city (e.g. Berlin or another geographic center).
2. Divide the space into radial sectors (like pizza slices), e.g. 6 slices of 60° each.
3. Process each sector one by one (clockwise or counterclockwise), visiting all cities within using a greedy strategy (nearest neighbor).
4. Avoid unnecessary backtracking by only moving forward to the next sector once the current one is completed.
5. Return to the starting city after visiting all reachable cities.

## 🗺️ Why Pizza-Greedy?

Visually intuitive – great for geographic TSP problems
Easy to implement
Can be adapted to different regions and use cases
Good balance between route quality and simplicity

## 📦 Installation

No external dependencies – pure Python.

## ▶️ Verwendung

```bash
python3 run_example.py
```

Die Beispielausgabe zeigt die berechnete Route und die gesamte zurückgelegte Entfernung in Kilometern.

## 📈 Example

The included example solves a route through the 20 largest German cities using the Pizza-Greedy approach.

## 📜 License

MIT License
