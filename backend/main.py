from fastapi import FastAPI
from routes.users_route import router as users_router
from repositories.student_repository import StudentRepository
from routes.superservice_route import router as super_router

app = FastAPI()
app.include_router(users_router, prefix="/auth")
app.include_router(super_router, prefix="/super-service")


@app.get("/")
def main():
    return "Backend is working !!!"


@app.get("/students")
def get_students():
    obj = StudentRepository()
    return obj.get_students()





