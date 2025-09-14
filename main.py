from mcp.server.fastmcp import FastMCP
import time
import logging

mcp = FastMCP("add_integers")

logging.basicConfig(
    level= logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filemode='a',
    filename="./mcp_server.log"
)
logger = logging.getLogger(__name__)

class MCPError(Exception):
    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message
        super().__init__(f"[{code}] {message}")

@mcp.tool()
def add(a: int, b: int) -> int:
    '''
    Add two integers and return the SUM
    
    Args:
        a: First Integer
        b: Second Integer
        
    Returns:
        The Sum of a and b.
    '''
    logger.info(f"Adding {a} and {b}")
    result = a + b
    logger.info(f"Result = {result}")
    return result


@mcp.tool()
def divide(a: int, b: int) -> int:
    '''
    Divide two integers a and b
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        The division of a/b
    '''
    if b == 0:
        raise MCPError(code=400, message="Division by zero is not allowed")
    return a//b

@mcp.tool()
def long_process(steps: int):
    '''
    Simulates a long-running process
    '''
    for i in range(steps):
        print(f"Processing step: {i + 1} of {steps}")
        time.sleep(0.1)
    return "Process Compeleted"
    
if __name__ == "__main__":
    mcp.run(transport="stdio")