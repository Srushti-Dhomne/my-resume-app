students = [
  {"Name": "Srushti", "Age": 19, "Skill": "Python"}
  {"Name": "Priya", "Age": 19, "Skill": "Python"}
  {"Name": "Anjali", "Age": 18, "Skill": "Python"}
]

for s in students:
  if s["Age"] == 19 and s["Skill"] == "Python":
    print(s["Name"])

print("\n--- Students with Python Skill ---")
for s in students:
    if s["Skill"] == "Python":
        print(f"{s['Name']} knows Python")
print("\n--- Students who are 18 years old ---")
for s in students:
    if s["Age"] == 18:
        print(f"{s['Name']} is 18 years old")
