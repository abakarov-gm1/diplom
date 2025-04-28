from fastapi import FastAPI
from routes.users_route import router as users_router

app = FastAPI()
app.include_router(users_router, prefix="/auth")


@app.get("/")
def main():
    return "Backend is working !!!"



