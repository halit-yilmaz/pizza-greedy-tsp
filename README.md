# 🍕 Pizza-Greedy Method for the Traveling Salesman Problem (TSP)

**Pizza-Greedy** is a heuristic strategy to solve the classic **Traveling Salesman Problem (TSP)**. It divides the map around a central city into pizza-slice-like sectors and applies a greedy approach within each.

---

## 💡 Core Idea

1. **Choose a central city** (e.g., Berlin or any geographic center).
2. **Divide space into radial sectors** (e.g., 6 slices of 60° each).
3. **Visit cities sector by sector**, either clockwise or counterclockwise.
4. **Greedy within sector**: Choose the nearest unvisited city until the sector is complete.
5. **Return to start** after all sectors are processed.

---

## 🗺️ Why Pizza-Greedy?

* Visually intuitive – great for geographic TSP problems
* Easy to implement
* Can be adapted to different regions and use cases
* Good balance between route quality and simplicity

---

## ▶️ Example

Run the demo on the 20 largest cities in Germany:

```bash
python3 run_example.py
```

You’ll see a reasonable travel route and total distance estimation.

---

## 📦 Installation

No dependencies required:

```bash
git clone https://github.com/halit-yilmaz/pizza-greedy-tsp.git
cd pizza-greedy-tsp
python3 run_example.py
```

---

## 📜 License

MIT License
