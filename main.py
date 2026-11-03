students = [
  {"Name": "Srushti", "Age": 19, "Skill": "Python"}
  {"Name": "Priya", "Age": 19, "Skill": "Python"}
  {"Name": "Anjali", "Age": 18, "Skill": "Python"}
]

for s in students:
  if s["Age"] == 19 and s["Skill"] == "Python":
    print(s["Name"])
