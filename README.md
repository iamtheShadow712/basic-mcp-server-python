# Basic MCP Server

A basic Model Context Protocol (MCP) server built with FastMCP that provides mathematical operations and process simulation tools.

## Features

This MCP server exposes three main tools:

- **add**: Adds two integers and returns their sum
- **divide**: Divides two integers with proper error handling for division by zero
- **long_process**: Simulates a long-running process with progress updates

## Installation

### Prerequisites

- Python 3.13 or higher
- pip (Python package installer)

### Setup

1. Clone or download this repository
2. Install dependencies using pip:

```bash
pip install -r requirements.txt
```

Or using uv (if you have it installed):

```bash
uv sync
```

## Usage

### Running the Server

To start the MCP server:

```bash
python main.py
```

The server runs on stdio transport and can be integrated with MCP-compatible clients.

### Available Tools

#### add(a: int, b: int) -> int

Adds two integers and returns their sum.

**Parameters:**
- `a` (int): First integer
- `b` (int): Second integer

**Returns:** The sum of a and b

**Example:**
```python
result = add(5, 3)  # Returns 8
```

#### divide(a: int, b: int) -> int

Divides two integers using integer division.

**Parameters:**
- `a` (int): Dividend
- `b` (int): Divisor (cannot be zero)

**Returns:** Integer result of a divided by b

**Throws:** MCPError with code 400 if division by zero is attempted

**Example:**
```python
result = divide(10, 3)  # Returns 3
```

#### long_process(steps: int)

Simulates a long-running process with progress updates.

**Parameters:**
- `steps` (int): Number of steps to simulate

**Returns:** "Process Completed" message

**Example:**
```python
result = long_process(10)  # Simulates 10 steps with 0.1s delay each
```

## Logging

The server logs all operations to `mcp_server.log` with the following format:
```
%(asctime)s - %(name)s - %(levelname)s - %(message)s
```

Log levels include INFO for operation details and ERROR for exceptions.

## Error Handling

The server includes custom error handling:
- Division by zero is prevented with a descriptive error message
- All errors are logged appropriately

## Development

### Project Structure

```
basic-mcp-server/
├── main.py              # Main server implementation
├── pyproject.toml       # Project configuration
├── requirements.txt     # Python dependencies
├── uv.lock             # Lock file for uv package manager
├── .python-version     # Python version specification
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

### Adding New Tools

To add new tools to the MCP server:

1. Define a new function decorated with `@mcp.tool()`
2. Add proper type hints and docstrings
3. Include appropriate logging and error handling

Example:
```python
@mcp.tool()
def new_tool(param: str) -> str:
    """
    Description of the new tool

    Args:
        param: Description of parameter

    Returns:
        Description of return value
    """
    logger.info(f"Executing new_tool with {param}")
    # Tool implementation
    return result
```

## Dependencies

Key dependencies include:
- `fastmcp`: FastMCP framework for building MCP servers
- `mcp`: Model Context Protocol core library
- Standard Python libraries for logging and time handling

