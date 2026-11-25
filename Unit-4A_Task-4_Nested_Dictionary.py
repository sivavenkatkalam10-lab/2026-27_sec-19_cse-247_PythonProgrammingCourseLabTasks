students = {
    1: {"name": "Siva", "marks": 90},
    2: {"name": "Naidu", "marks": 85},
    3: {"name": "Kalam", "marks": 95}
}

for roll_no, details in students.items():
    print("Name:", details["name"])
    print("Marks:", details["marks"])
    print()