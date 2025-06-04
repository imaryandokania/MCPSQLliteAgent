# Import standard modules
import sqlite3
from mcp.server.fastmcp import FastMCP

# Create the MCP server
mcp = FastMCP("sqlite_server")

# Add a tool to execute SQLite queries
@mcp.tool()
def query_sqlite(query: str) -> str:
    """Executes a SQL query on a local SQLite database.

    Args:
        query: A valid SQL query string (e.g., "SELECT * FROM financials")
        Example: SELECT company, ebitda FROM financials

    Returns:
        str: Results of the SQL query or an error message
    """
    try:
        conn = sqlite3.connect("finance_data.db")  # Make sure this DB file exists
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()
        return f"Query Results:\n{rows}"
    except Exception as e:
        return f"Error executing query: {e}"

# Run the MCP server
if __name__ == "__main__":
    mcp.run(transport="stdio")