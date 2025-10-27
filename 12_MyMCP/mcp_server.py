from fastmcp import FastMCP
from datetime import datetime
import os

# Initialize the MCP server
mcp = FastMCP("Basic MCP Server")

# Tool 1: Calculator - Basic arithmetic operations
@mcp.tool()
def calculator(operation: str, a: float, b: float) -> float:
    """
    Perform basic arithmetic operations.
    
    Args:
        operation: The operation to perform (add, subtract, multiply, divide)
        a: First number
        b: Second number
    
    Returns:
        The result of the operation
    """
    operations = {
        "add": lambda x, y: x + y,
        "subtract": lambda x, y: x - y,
        "multiply": lambda x, y: x * y,
        "divide": lambda x, y: x / y if y != 0 else None
    }
    
    result = operations.get(operation.lower())
    if result:
        return result(a, b)
    else:
        return f"Invalid operation. Choose from: {', '.join(operations.keys())}"

# Tool 2: Get current time and date
@mcp.tool()
def get_time_info(format: str = "full") -> str:
    """
    Get current time and date information.
    
    Args:
        format: Time format to return (full, date, time, timestamp)
    
    Returns:
        Current time/date information
    """
    now = datetime.now()
    
    formats = {
        "full": now.strftime("%Y-%m-%d %H:%M:%S"),
        "date": now.strftime("%Y-%m-%d"),
        "time": now.strftime("%H:%M:%S"),
        "timestamp": str(now.timestamp())
    }
    
    return formats.get(format, formats["full"])

# Tool 3: Text manipulation
@mcp.tool()
def text_processor(text: str, operation: str) -> str:
    """
    Process text with various operations.
    
    Args:
        text: The text to process
        operation: The operation to perform (upper, lower, reverse, word_count)
    
    Returns:
        Processed text
    """
    operations = {
        "upper": str.upper,
        "lower": str.lower,
        "reverse": lambda x: x[::-1],
        "word_count": lambda x: f"Word count: {len(x.split())}"
    }
    
    result = operations.get(operation.lower())
    if result:
        return result(text)
    else:
        return f"Invalid operation. Choose from: {', '.join(operations.keys())}"

# Tool 4: File operations
@mcp.tool()
def file_info(file_path: str) -> dict:
    """
    Get information about a file.
    
    Args:
        file_path: Path to the file
    
    Returns:
        Dictionary with file information
    """
    info = {
        "exists": os.path.exists(file_path),
        "is_file": os.path.isfile(file_path),
        "is_directory": os.path.isdir(file_path)
    }
    
    if info["exists"] and info["is_file"]:
        stat = os.stat(file_path)
        info["size"] = stat.st_size
        info["modified"] = datetime.fromtimestamp(stat.st_mtime).isoformat()
        info["created"] = datetime.fromtimestamp(stat.st_ctime).isoformat()
    
    return info

# Tool 5: Simple list operations
@mcp.tool()
def list_operations(items: list, operation: str = "sum") -> float:
    """
    Perform operations on a list of numbers.
    
    Args:
        items: List of numbers
        operation: Operation to perform (sum, average, min, max, product)
    
    Returns:
        Result of the operation
    """
    operations = {
        "sum": sum,
        "average": lambda x: sum(x) / len(x) if x else 0,
        "min": min,
        "max": max,
        "product": lambda x: eval('*'.join(map(str, x)))
    }
    
    result = operations.get(operation.lower())
    if result:
        return float(result(items))
    else:
        return f"Invalid operation. Choose from: {', '.join(operations.keys())}"

# Run the server
if __name__ == "__main__":
    mcp.run()

