# My MCP Server

A basic Model Context Protocol (MCP) server implementation using FastMCP.

## Overview

This MCP server provides several useful tools that can be integrated with AI assistants and other applications that support the Model Context Protocol.

## Available Tools

### 1. Calculator
Performs basic arithmetic operations (add, subtract, multiply, divide).
- **operation**: The operation to perform
- **a**: First number
- **b**: Second number

### 2. Get Time Info
Retrieves current time and date information.
- **format**: Time format (full, date, time, timestamp)

### 3. Text Processor
Processes text with various operations (upper, lower, reverse, word_count).

### 4. File Info
Retrieves information about files and directories.
- **file_path**: Path to the file or directory

### 5. List Operations
Performs operations on lists of numbers (sum, average, min, max, product).

## Installation

1. **Install using pip:**
```bash
pip install fastmcp
```

2. **Or install from the main requirements.txt:**
```bash
cd "Gen AI"
pip install -r requirements.txt
```

The `fastmcp` package is already included in the main project requirements.

## Running the Server

### Basic Run
```bash
python mcp_server.py
```

The server will start and listen for MCP client connections using the STDIO transport.

## Usage with Claude Desktop

To use this MCP server with Claude Desktop:

### Windows
1. Open or create the configuration file at:
   ```
   %APPDATA%\Claude\claude_desktop_config.json
   ```

2. Add the following configuration (adjust the path as needed):
```json
{
  "mcpServers": {
    "my-mcp-server": {
      "command": "python",
      "args": [
        "C:\\Users\\manan\\OneDrive\\Desktop\\Gen AI\\12_MyMCP\\mcp_server.py"
      ]
    }
  }
}
```

### Mac
1. Open or create the configuration file at:
   ```
   ~/Library/Application Support/Claude/claude_desktop_config.json
   ```

2. Add the configuration with your actual path:
```json
{
  "mcpServers": {
    "my-mcp-server": {
      "command": "python",
      "args": [
        "/full/path/to/Gen AI/12_MyMCP/mcp_server.py"
      ]
    }
  }
}
```

3. Restart Claude Desktop to load the new MCP server

### With Virtual Environment
If you're using a virtual environment, update the command to use the venv's Python:

```json
{
  "mcpServers": {
    "my-mcp-server": {
      "command": "C:\\Users\\manan\\OneDrive\\Desktop\\Gen AI\\venv\\Scripts\\python.exe",
      "args": [
        "C:\\Users\\manan\\OneDrive\\Desktop\\Gen AI\\12_MyMCP\\mcp_server.py"
      ]
    }
  }
}
```

## Testing the Server

You can test the server using the MCP Inspector or by creating a simple client:

```python
# test_client.py
import json
import subprocess

process = subprocess.Popen(
    ["python", "mcp_server.py"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    text=True
)

# Test the calculator tool
request = {
    "jsonrpc": "2.0",
    "method": "call_tool",
    "params": {
        "name": "calculator",
        "arguments": {"operation": "add", "a": 5, "b": 3}
    },
    "id": 1
}

process.stdin.write(json.dumps(request) + "\n")
response = process.stdout.readline()
print("Response:", response)
```

## Extending the Server

To add more tools to the server:

1. Import any required libraries
2. Define your function
3. Decorate it with `@mcp.tool()`
4. Add a docstring that describes the function and its parameters

Example:
```python
@mcp.tool()
def my_tool(param1: str, param2: int) -> str:
    """
    Description of what the tool does.
    
    Args:
        param1: Description of param1
        param2: Description of param2
    
    Returns:
        What the function returns
    """
    # Your implementation here
    return result
```

## Learn More

- [FastMCP Documentation](https://fastmcp.wiki/)
- [Model Context Protocol](https://modelcontextprotocol.io/)
- [MCP Specification](https://spec.modelcontextprotocol.io/)

