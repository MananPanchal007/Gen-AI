"""
Simple example of how to use the MCP server programmatically.
This demonstrates the basic usage pattern.
"""

from fastmcp import FastMCP

# Example: Creating a simple custom tool
# This would be added to mcp_server.py to extend functionality

mcp = FastMCP("Example Server")

@mcp.tool()
def greet(name: str) -> str:
    """Greet a person by name."""
    return f"Hello, {name}! Welcome to the MCP server."

@mcp.tool()
def current_working_directory() -> str:
    """Get the current working directory."""
    import os
    return os.getcwd()

@mcp.tool()
def repeat_text(text: str, times: int = 1) -> str:
    """Repeat text a specified number of times.
    
    Args:
        text: The text to repeat
        times: Number of times to repeat (default: 1)
    
    Returns:
        Repeated text
    """
    return (text + " ") * times

if __name__ == "__main__":
    mcp.run()

