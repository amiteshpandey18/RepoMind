from repomind.mcp.mcp_client import run_mcp_tool


result = run_mcp_tool(
    "search_repository",
    {
        "question": "What authentication does this project use?"
    }
)

print()
print("==============================")
print("MCP Client Result")
print("==============================")
print(result)
