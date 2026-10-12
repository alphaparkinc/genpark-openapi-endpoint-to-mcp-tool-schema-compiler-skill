"""Example usage for OpenAPI Endpoint to MCP Tool Schema Compiler."""
from client import OpenAPIToMCPCompiler

if __name__ == "__main__":
    paths = {
        "/v1/customers": {
            "get": {
                "operationId": "list_customers",
                "summary": "List active customers",
                "parameters": [{"name": "limit", "required": True, "schema": {"type": "integer"}}]
            }
        }
    }
    res = OpenAPIToMCPCompiler.compile_endpoints(paths)
    print("Compiled Tools:", res["tools"])
