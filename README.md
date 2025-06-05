# 🍕 Pizza-Greedy-Methode für das Traveling Salesman Problem (TSP)

Die **Pizza-Greedy-Methode** ist ein heuristischer Ansatz zur Lösung des TSP (Travelling Salesman Problem), bei dem der geografische Raum rund um eine zentrale Stadt (z. B. Berlin oder Kassel) in mehrere „Pizzastücke“ (Sektoren) unterteilt wird. Innerhalb jedes dieser Sektoren wird eine Greedy-Strategie angewendet, um eine sinnvolle Besuchsreihenfolge der Städte zu erzeugen.

## 💡 Idee der Methode

Die Route basiert auf folgenden Grundprinzipien:

1. **Zentrum definieren**: Eine zentrale Stadt wird als Start- und Endpunkt gewählt.
2. **Sektoraufteilung**: Der geografische Raum um das Zentrum wird in z. B. 6 Sektoren à 60° aufgeteilt – ähnlich wie Pizzastücke.
3. **Greedy-Strategie pro Sektor**: In jedem Sektor wird die nächstgelegene unbesuchte Stadt besucht, bis alle im Sektor abgearbeitet sind.
4. **Uhrzeigersinn / gegen Uhrzeiger**: Die Sektoren werden nacheinander im Kreis abgearbeitet, um unnötiges Hin- und Herfahren zu vermeiden.
5. **Rückkehr zum Startpunkt**: Nach dem letzten Sektor erfolgt die Rückkehr zur Startstadt.

Diese Methode ist besonders intuitiv, visuell nachvollziehbar und geografisch sinnvoll. Sie stellt eine gute Balance zwischen Effizienz und einfacher Implementierung dar.

## 📦 Installation

Keine externen Bibliotheken erforderlich. Das Projekt basiert vollständig auf der Python-Standardbibliothek.

## ▶️ Verwendung

```bash
python examples/run_example.py
```

Die Beispielausgabe zeigt die berechnete Route und die gesamte zurückgelegte Entfernung in Kilometern.

## 📈 Anwendungsbeispiel

Das mitgelieferte Beispiel demonstriert die Anwendung auf die 20 größten Städte Deutschlands. Die Methode kann jedoch leicht auf beliebige Städtemengen oder andere Länder angepasst werden.

## 📜 Lizenz

Dieses Projekt steht unter der MIT-Lizenz. Frei verwendbar – mit Pizza, aber ohne Garantie 😉.
