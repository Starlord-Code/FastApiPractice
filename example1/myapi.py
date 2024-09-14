from fastapi import FastAPI, Path

app = FastAPI()

#amazon.com/create-user

#GET - Get an information
#POST - Create something in data
#PUT - Update something
#DELETE - Delete Something

students = {
    1: {
        "name": "john",
        "age": 17,
        "class": "year 12"
    }
}

@app.get("/")
def index():
    return {"name": "First Data"}

#google.com/get-student/1
#path paramter with example
@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(description="The ID of the student you want to view ",gt=0, lt=4)):
    return students[student_id]

#query parameter with example
#google.com/