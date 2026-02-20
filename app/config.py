import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    HOST: str = "0.0.0.0"
    PORT: int = 5555
    TIMEOUT: int = 60
    MCP_SETTINGS_PATH: str = os.getenv(
        "MCP_SETTINGS_PATH", "/app/config/mcp_settings.json"
    )


settings = Settings()
