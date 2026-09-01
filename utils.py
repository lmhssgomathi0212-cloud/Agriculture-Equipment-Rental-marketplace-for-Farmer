# utils.py
def search_equipment(equipment, search_text):
    search_text = search_text.lower()
    return [
        item for item in equipment
        if search_text in item["name"].lower()
        or search_text in item["category"].lower()
        or search_text in item["location"].lower()
    ]
def get_categories(equipment):
    return sorted(set(item["category"] for item in equipment))
def get_locations(equipment):
    return sorted(set(item["location"] for item in equipment))
