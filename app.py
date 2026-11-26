from fastapi import FastAPI

app = FastAPI()

students = [
    {"Name": "Srushti", "Age": 19, "Skill": "Python"},
    {"Name": "Priya", "Age": 19, "Skill": "Python"},
    {"Name": "Anjali", "Age": 18, "Skill": "Python"},
    {"Name": "Rohan", "Age": 20, "Skill": "Java"},
    {"Name": "Meera", "Age": 19, "Skill": "Java"},
    {"Name": "Aarav", "Age": 21, "Skill": "Python"},
    {"Name": "Riya", "Age": 21, "Skill": "HTML"},
    {"Name": "Sneha", "Age": 22, "Skill": "CSS"},
    {"Name": "Kabir", "Age": 23, "Skill": "SQL"},
    {"Name": "Arjun", "Age": 24, "Skill": "JavaScript"},
    {"Name": "Ishita", "Age": 25, "Skill": "React"},
    {"Name": "Vihaan", "Age": 26, "Skill": "Node.js"},
    {"Name": "Ananya", "Age": 27, "Skill": "C++"},
    {"Name": "Diya", "Age": 28, "Skill": "TypeScript"},
    {"Name": "Kavya", "Age": 29, "Skill": "Tailwind CSS"},
]

@app.get("/")
def home():
    return {"message": "Hello Srushti, your Resume API is running!"}

@app.get("/students")
def get_students():
    return students

@app.get("/students/{name}")
def get_one_student(name: str):
    for s in students:
        if s["Name"] == name:
            return s
    return {"message": "Student not found"}

@app.get("/students/skill/{skill}")
def get_by_skill(skill: str):
    result = []
    for s in students:
        if s["Skill"] == skill:
            result.append(s)
    return result

@app.post("/students")
def add_student(student: dict):
    students.append(student)
    return student

@app.delete("/students/{name}")
def delete_student(name: str):
    for s in students:
        if s["Name"] == name:
            students.remove(s)
            return {"message": f"{name} deleted"}
    return {"message": "Student not found"}

@app.put("/students/{name}")
def update_student(name: str, new_data: dict):
    for s in students:
        if s["Name"] == name:
            s.update(new_data)
            return s
    return {"message": "Student not found"}

@app.get("/students/count")
def count_students():
    return {"total_students": len(students)} 

@app.get("/skills")
def get_all_skills():
    skills = []
    for s in students:
        if s["skill"] not in skills:
            skills.append(s["skill"])
    return {"skills": skills}
