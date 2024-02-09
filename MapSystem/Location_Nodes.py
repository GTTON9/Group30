import math
class Location_Nodes():
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return f"LocationNode: {self.name} ({self.latitude}, {self.longitude})"

    def calculate_distance(self, other_node):
        """
        Calculate the distance (in kilometers) between two location nodes
        using Haversine formula.
        """
        radius_of_earth = 6371  # Earth's radius in kilometers
        lat1, lon1 = math.radians(self.latitude), math.radians(self.longitude)
        lat2, lon2 = math.radians(other_node.latitude), math.radians(other_node.longitude)
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = radius_of_earth * c
        return distance


