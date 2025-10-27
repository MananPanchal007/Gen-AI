"""
Test client for the MCP server.
This script demonstrates how to interact with the MCP server.
"""

import json
import subprocess
import sys
import time

def send_request(process, method, params, request_id=1):
    """Send a request to the MCP server."""
    request = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params,
        "id": request_id
    }
    
    print(f"\n📤 Sending request: {method}")
    print(f"   Parameters: {params}")
    
    process.stdin.write(json.dumps(request) + "\n")
    process.stdin.flush()
    
    # Read response
    response = process.stdout.readline()
    print(f"📥 Response: {response.strip()}")
    
    try:
        parsed = json.loads(response)
        return parsed
    except:
        return None

def test_initialization(process):
    """Test server initialization."""
    print("\n" + "="*50)
    print("Testing Server Initialization")
    print("="*50)
    
    # Initialize the server
    init_request = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "initialize",
        "params": {
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "clientInfo": {
                "name": "test-client",
                "version": "1.0.0"
            }
        }
    }
    
    process.stdin.write(json.dumps(init_request) + "\n")
    process.stdin.flush()
    response = process.stdout.readline()
    print(f"✅ Server initialized")
    print(f"   Response: {response.strip()[:100]}...")

def test_tools_listing(process):
    """Test listing available tools."""
    print("\n" + "="*50)
    print("Listing Available Tools")
    print("="*50)
    
    request = {
        "jsonrpc": "2.0",
        "method": "tools/list",
        "params": {},
        "id": 2
    }
    
    process.stdin.write(json.dumps(request) + "\n")
    process.stdin.flush()
    response = process.stdout.readline()
    print(f"📋 Available tools:")
    print(response.strip())

def test_tool_call(process, tool_name, arguments, test_id):
    """Test calling a specific tool."""
    request = {
        "jsonrpc": "2.0",
        "method": "tools/call",
        "params": {
            "name": tool_name,
            "arguments": arguments
        },
        "id": test_id
    }
    
    process.stdin.write(json.dumps(request) + "\n")
    process.stdin.flush()
    
    # Wait a bit for response
    time.sleep(0.1)
    response = process.stdout.readline()
    
    print(f"\n🔧 Testing tool: {tool_name}")
    print(f"   Arguments: {arguments}")
    if response:
        print(f"   Result: {response.strip()}")
    
    return response

def main():
    """Run tests for the MCP server."""
    print("🚀 Starting MCP Server Test Client")
    print("="*50)
    
    # Start the MCP server
    server_path = "mcp_server.py"
    print(f"\n📂 Server path: {server_path}")
    
    try:
        process = subprocess.Popen(
            ["python", server_path],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=1
        )
        
        # Give server time to start
        time.sleep(0.5)
        
        # Test 1: Calculator
        print("\n" + "="*50)
        print("Test 1: Calculator Tool")
        print("="*50)
        test_tool_call(process, "calculator", {"operation": "add", "a": 10, "b": 5}, 3)
        test_tool_call(process, "calculator", {"operation": "multiply", "a": 7, "b": 8}, 4)
        
        # Test 2: Time Info
        print("\n" + "="*50)
        print("Test 2: Time Information Tool")
        print("="*50)
        test_tool_call(process, "get_time_info", {"format": "full"}, 5)
        test_tool_call(process, "get_time_info", {"format": "date"}, 6)
        
        # Test 3: Text Processor
        print("\n" + "="*50)
        print("Test 3: Text Processor Tool")
        print("="*50)
        test_tool_call(process, "text_processor", {"text": "Hello World", "operation": "upper"}, 7)
        test_tool_call(process, "text_processor", {"text": "Hello World", "operation": "word_count"}, 8)
        
        # Test 4: List Operations
        print("\n" + "="*50)
        print("Test 4: List Operations Tool")
        print("="*50)
        test_tool_call(process, "list_operations", {"items": [1, 2, 3, 4, 5], "operation": "sum"}, 9)
        test_tool_call(process, "list_operations", {"items": [10, 20, 30], "operation": "average"}, 10)
        
        print("\n" + "="*50)
        print("✅ All tests completed!")
        print("="*50)
        
        # Close the server
        process.terminate()
        
    except FileNotFoundError:
        print(f"❌ Error: Could not find mcp_server.py")
        print(f"   Make sure you're running this from the 12_MyMCP directory")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()

