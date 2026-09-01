# database.py
equipment_data = [
    {
        "name": "Tractor",
        "category": "Tractor",
        "owner": "Ramesh",
        "location": "Chennai",
        "price": "₹1,500/day"
    },
    {
        "name": "Rotavator",
        "category": "Tillage Equipment",
        "owner": "Kumar",
        "location": "Coimbatore",
        "price": "₹1,000/day"
    },
    {
        "name": "Seed Drill",
        "category": "Sowing Equipment",
        "owner": "Suresh",
        "location": "Madurai",
        "price": "₹800/day"
    }
]
def get_equipment():
    return equipment_data
def get_equipment_count():
    return len(equipment_data)
