
from pizza_greedy import pizza_greedy, haversine

city_coords = {
    "Berlin": (52.5200, 13.4050),
    "Hamburg": (53.5511, 9.9937),
    "München": (48.1351, 11.5820),
    "Köln": (50.9375, 6.9603),
    "Frankfurt am Main": (50.1109, 8.6821),
    "Stuttgart": (48.7758, 9.1829),
    "Düsseldorf": (51.2277, 6.7735),
    "Leipzig": (51.3397, 12.3731),
    "Dortmund": (51.5136, 7.4653),
    "Essen": (51.4556, 7.0116),
    "Bremen": (53.0793, 8.8017),
    "Dresden": (51.0504, 13.7373),
    "Hannover": (52.3759, 9.7320),
    "Nürnberg": (49.4521, 11.0767),
    "Duisburg": (51.4344, 6.7623),
    "Bochum": (51.4818, 7.2162),
    "Wuppertal": (51.2562, 7.1508),
    "Bielefeld": (52.0302, 8.5325),
    "Bonn": (50.7374, 7.0982),
    "Münster": (51.9607, 7.6261)
}

route = pizza_greedy(city_coords, center_city="Berlin")
print("Pizza-Greedy-Route:")
print(" → ".join(route))

# Gesamtdistanz
dist = sum(haversine(city_coords[route[i]], city_coords[route[i+1]]) for i in range(len(route)-1))
print(f"Gesamtdistanz: {round(dist)} km")
