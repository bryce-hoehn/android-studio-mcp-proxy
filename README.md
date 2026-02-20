# Android Studio MCP Proxy

A FastAPI server for using local MCP servers in Android Studio

## Features

- Dynamic MCP server routing - Register MCP servers from configuration
- Docker support

## Installation

### Docker

1. Clone the repository
3. Configure MCP servers in `mcp_settings.json`
4. Start the container:
   ```bash
   docker-compose up -d
   ```
5. The server will run on `http://localhost:5555`

## Configuration

### MCP Servers

Configure MCP servers in `mcp_settings.json`. Ex:

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp"],
      "env": {
        "DEFAULT_MINIMUM_TOKENS": ""
      },
      "alwaysAllow": [
        "resolve-library-id",
        "get-library-docs",
        "query-docs"
      ]
    }
  }
}
```

```bash
docker-compose restart
```

## Using MCP Servers in Android Studio

1. **Open Android Studio Settings:**
   - Go to `File` -> `Settings` -> `Tools` -> `AI Assistant` -> `MCP Servers`

2. **Enable MCP Integration:**
   - Add a new MCP server with the URL: `http://localhost:5555/mcp/{server_name}`
   - Replace `{server_name}` with the name from your `mcp_settings.json` (e.g., `context7`)

3. **Example Configuration:**
  
   ```json
   {
     "mcpServers": {
       "context7": {
         "httpUrl": "http://localhost:5555/mcp/context7"
       }
     }
   }
    ```

## API Endpoints

### MCP Servers

Dynamic endpoints are created for each configured MCP server:

```
GET /mcp/{server_name}
```

For example, with the default configuration:
```
GET /mcp/context7
```
