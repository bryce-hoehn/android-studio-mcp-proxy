import uvicorn
from fastapi import FastAPI
from app.routes.mcp import router as mcp_router, register_mcp_routes
from app.config import settings

app = FastAPI()

app.include_router(mcp_router)

register_mcp_routes(app)

if __name__ == "__main__":
    uvicorn.run(app, host=settings.HOST, port=settings.PORT)
