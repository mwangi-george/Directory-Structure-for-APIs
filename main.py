from fastapi import FastAPI
from app.routes.user import create_user_router

# application factory pattern (using functions to create instances of applications)


def create_application() -> FastAPI:

    user_router = create_user_router()
    app = FastAPI(
        title="API UserManager",
        description="Made with ❤️ by George Mwangi"
    )
    app.include_router(user_router)
    return app


app = create_application()
