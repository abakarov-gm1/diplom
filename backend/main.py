from fastapi import FastAPI
from routes.users_route import router as users_router
from repositories.student_repository import StudentRepository

app = FastAPI()
app.include_router(users_router, prefix="/auth")


@app.get("/")
def main():
    return "Backend is working !!!"


@app.get("/students")
def get_students():
    obj = StudentRepository()
    return obj.get_students()





