
import math

def haversine(coord1, coord2):
    R = 6371
    lat1, lon1 = map(math.radians, coord1)
    lat2, lon2 = map(math.radians, coord2)
    dlat, dlon = lat2 - lat1, lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1)*math.cos(lat2)*math.sin(dlon/2)**2
    return R * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

def calculate_angles(cities, center_city):
    center = cities[center_city]
    angles = {}
    for city, coord in cities.items():
        if city == center_city:
            continue
        dx = coord[1] - center[1]
        dy = coord[0] - center[0]
        angle = (math.degrees(math.atan2(dy, dx)) + 360) % 360
        angles[city] = angle
    return angles

def assign_sectors(angles, num_sectors=6):
    sectors = {i: [] for i in range(num_sectors)}
    for city, angle in angles.items():
        sector = int(angle // (360 / num_sectors))
        sectors[sector].append(city)
    return sectors

def greedy_tour(start, cities, coords):
    route = []
    current = start
    while cities:
        next_city = min(cities, key=lambda c: haversine(coords[current], coords[c]))
        route.append(next_city)
        cities.remove(next_city)
        current = next_city
    return route

def pizza_greedy(cities, center_city="Berlin", num_sectors=6):
    route = [center_city]
    angles = calculate_angles(cities, center_city)
    sectors = assign_sectors(angles, num_sectors)
    visited = set([center_city])
    current = center_city

    for i in range(num_sectors):
        sector = sectors[i][:]
        if not sector:
            continue
        first = min(sector, key=lambda c: haversine(cities[current], cities[c]))
        route.append(first)
        sector.remove(first)
        current = first
        sector_route = greedy_tour(current, sector, cities)
        route += sector_route
        if sector_route:
            current = sector_route[-1]

    route.append(center_city)
    return route
