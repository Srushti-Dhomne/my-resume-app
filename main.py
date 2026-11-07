students = [
    {"Name": "Srushti", "Age": 19, "Skill": "Python"},
    {"Name": "Priya", "Age": 19, "Skill": "Python"},
    {"Name": "Anjali", "Age": 18, "Skill": "Python"},
    {"Name": "Rohan", "Age": 20, "Skill": "Java"},
    {"Name": "Meera", "Age": 19, "Skill": "Java"},
    {"Name": "Aarav", "Age": 21, "Skill": "Python"}
]

# Filter by Python Skill
for s in students:
    if s["Skill"] == "Python":
        print(f"{s['Name']} knows Python")

# Filter by Age 18
for s in students:
    if s["Age"] == 18:
        print(f"{s['Name']} is 18 years old")

# Filter by Java Skill
for s in students:
    if s["Skill"] == "Java":
        print(f"{s['Name']} knows Java")

# Filter by Age 19
for s in students:
    if s["Age"] == 19:
        print(f"{s['Name']} is 19 years old")

# Filter by Age 21
for s in students:
    if s["Age"] == 21:
        print(f"{s['Name']} is 21 years old")
