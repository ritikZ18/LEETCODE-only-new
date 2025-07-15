import math

class SquirrelResearch:
    def __init__(self, locations: dict[str, int]) -> None:
        self.locations = locations
        self.location_data = {}  # location_id -> list of levels
        self.nut_to_location = {}  # nut_id -> (location_id, level)
        self.nut_expiry = {}  # nut_id -> expiry time

        for loc_id, levels in locations.items():
            self.location_data[loc_id] = [[] for _ in range(levels)]

    def hide_nut(self, timestamp: float, location_id: str, nut_id: str,
                 nut_weight: float, time_to_expire: float) -> bool:
        # Check if the nut already exists
        if nut_id in self.nut_to_location:
            return False
        if location_id not in self.location_data:
            return False

        levels = self.location_data[location_id]
        for i in range(len(levels)):
            # Fill level i if the level below it is filled
            if i == 0 or len(levels[i - 1]) > 0:
                if len(levels[i]) == 0:
                    expiry_time = timestamp + time_to_expire
                    levels[i].append((nut_weight, nut_id, expiry_time))
                    self.nut_to_location[nut_id] = (location_id, i)
                    self.nut_expiry[nut_id] = expiry_time
                    return True
        return False

    def retrieve_nut(self, timestamp: float, location_id: str,
                     max_squirrel_capacity_in_nuts: int) -> list[str]:
        if location_id not in self.location_data:
            return []

        retrieved = []
        levels = self.location_data[location_id]
        total_levels = len(levels)

        for i in reversed(range(total_levels)):  # start from top level
            level = levels[i]

            # Remove expired nuts
            level[:] = [entry for entry in level if entry[2] > timestamp]

            # Skip this level if it's not topmost and has < 50% capacity
            if i < total_levels - 1 and len(level) < 1:
                continue

            # Sort nuts by weight then by nut_id
            level.sort(key=lambda x: (x[0], x[1]))

            while level and len(retrieved) < max_squirrel_capacity_in_nuts:
                nut_weight, nut_id, expiry_time = level.pop(0)
                retrieved.append(nut_id)
                self.nut_to_location.pop(nut_id, None)
                self.nut_expiry.pop(nut_id, None)

        return retrieved



def test_assignment_case():
    sr = SquirrelResearch({"OakHollow": 3, "PineNook": 1})
    print("HideNut=" + str(sr.hide_nut(100, "OakHollow", "nut1", 0.31, 600))) # Level 0, OakHollow
    print("HideNut=" + str(sr.hide_nut(105, "OakHollow", "nut2", 0.40, 600))) # Level 1, OakHollow (nut1 is in level 0)
    print("HideNut=" + str(sr.hide_nut(110, "PineNook",  "nut3", 0.31, 600))) # Level 0, PineNook
    print("HideNut=" + str(sr.hide_nut(115, "OakHollow", "nut4", 0.53, 600))) # False (OakHollow levels are full)
    print("HideNut=" + str(sr.hide_nut(120, "PineNook",  "nut5", 0.35, 600))) # False (PineNook levels are full)
    print("HideNut=" + str(sr.hide_nut(121, "OakHollow", "nut6", 0.35, 600))) # False (OakHollow levels are full)Q

    # State before first retrieve:
    # OakHollow:
    #   Level 0: [(0.31, 'nut1', 700)]
    #   Level 1: [(0.40, 'nut2', 705)]
    # PineNook:
    #   Level 0: [(0.21, 'nut3', 710)]

    print("RetrieveNut=" + str(sr.retrieve_nut(140, "PineNook", 3))) # Retrieve from PineNook, should get nut3
    # PineNook after retrieve:
    #   Level 0: []

    print("RetrieveNut=" + str(sr.retrieve_nut(145, "OakHollow", 5))) # Retrieve from OakHollow
    # Expected: Retrieve from Level 1 first (nut2), then Level 0 (nut1)
    # nut2 (0.40) is heavier than nut1 (0.31)
    # Should get ['nut2', 'nut1']

test_assignment_case()
