import asyncio
import os
import sys

from mcp import Client, StdioServerParameters


async def main():

    server = StdioServerParameters(
        command=sys.executable,
        args=["-m", "repomind.mcp.server"],
        env={
            **os.environ,
            "PYTHONPATH": "src"
        }
    )

    async with Client(server) as client:

        result = await client.call_tool(
            "search_repository",
            {
                "question": "What authentication does this project use?"
            }
        )

        print()
        print("==============================")
        print("MCP Tool Result")
        print("==============================")

        for content in result.content:
            print(content.text)
if __name__ == "__main__":
    asyncio.run(main())
