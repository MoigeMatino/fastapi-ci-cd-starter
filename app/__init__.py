from contextlib import asynccontextmanager
from fastapi import FastAPI
from .database import init_db
from app.routes.item import router as item_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield
    
def create_app() -> FastAPI:
    app = FastAPI(lifespan=lifespan)

    
    # Include routers for the application
    app.include_router(item_router, tags=["items"])

    return app


# Create the app instance
app = create_app()