"""OpenAPI Endpoint to MCP Tool Schema Compiler.
100% Python Standard Library.
"""

import re

class OpenAPIToMCPCompiler:
    """Compiles OpenAPI 3.x path operations into standardized MCP tool inputSchema definitions."""

    @staticmethod
    def compile_endpoints(openapi_paths: dict) -> dict:
        mcp_tools = []
        for path, methods in openapi_paths.items():
            for method, spec in methods.items():
                op_id = spec.get("operationId") or f"{method.lower()}_{re.sub(r'[^a-zA-Z0-9]+', '_', path).strip('_')}"
                summary = spec.get("summary", f"Executes {method.upper()} {path}")
                params = spec.get("parameters", [])
                props = {}
                required = []
                for p in params:
                    p_name = p.get("name", "param")
                    p_type = p.get("schema", {}).get("type", "string")
                    props[p_name] = {"type": p_type, "description": p.get("description", "")}
                    if p.get("required"):
                        required.append(p_name)

                mcp_tools.append({
                    "name": op_id,
                    "description": f"[{method.upper()} {path}] {summary}",
                    "inputSchema": {
                        "type": "object",
                        "properties": props,
                        "required": required
                    }
                })

        return {
            "compiled_tools_count": len(mcp_tools),
            "tools": mcp_tools
        }
