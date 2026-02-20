from pydantic import BaseModel
from typing import Dict, List, Optional


class McpServerConfig(BaseModel):
    """Configuration for a single MCP server."""

    command: str
    args: List[str] | str
    env: Optional[Dict[str, str]] = None
    alwaysAllow: Optional[List[str]] = None


class McpSettings(BaseModel):
    """MCP settings configuration loaded from mcp_settings.json."""

    mcpServers: Dict[str, McpServerConfig]
