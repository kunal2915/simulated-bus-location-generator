import json
import random
import time

bus_ids = ["Bus_001", "Bus_002", "Bus_003", "Bus_004", "Bus_005"]

def generate_coordinates():
    # Example range for latitude and longitude (India region)
    latitude = round(random.uniform(23.00, 28.00), 5)
    longitude = round(random.uniform(72.00, 77.00), 5)
    return latitude, longitude

while True:
    bus_positions = {}
    for bus in bus_ids:
        latitude, longitude = generate_coordinates()
        bus_positions[bus] = {"latitude": latitude, "longitude": longitude}

    with open("bus_locations.json", "w") as file:
        json.dump(bus_positions, file, indent=4)

    print("Updated bus positions:", bus_positions)
    time.sleep(5)
