from fastapi import FastAPI
from app.routes.user import user_router

app = FastAPI(
    title="API UserManager",
    description="Made with ❤️ by George Mwangi"
)
app.include_router(user_router)

# add user_router to our app
