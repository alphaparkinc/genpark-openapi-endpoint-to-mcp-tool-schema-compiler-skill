"""MCP server for OpenAPI Endpoint to MCP Tool Schema Compiler."""
import sys
import json
from client import OpenAPIToMCPCompiler

def handle_request(req):
    method = req.get("method")
    if method == "tools/list":
        return {
            "tools": [{
                "name": "compile_openapi_to_mcp",
                "description": "Compiles OpenAPI path operations into MCP tool definitions",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "openapi_paths": {"type": "object"}
                    },
                    "required": ["openapi_paths"]
                }
            }]
        }
    elif method == "tools/call":
        params = req.get("params", {})
        if params.get("name") == "compile_openapi_to_mcp":
            paths = params.get("arguments", {}).get("openapi_paths", {})
            res = OpenAPIToMCPCompiler.compile_endpoints(paths)
            return {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}
    return {"error": "Method not found"}

if __name__ == "__main__":
    for line in sys.stdin:
        if line.strip():
            print(json.dumps(handle_request(json.loads(line))))
            sys.stdout.flush()
