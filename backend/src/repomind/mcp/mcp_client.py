import asyncio
import os
import sys

from mcp import Client, StdioServerParameters


async def call_mcp_tool(
    tool_name: str,
    arguments: dict
):

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
            tool_name,
            arguments
        )

        return result.content[0].text


def run_mcp_tool(
    tool_name: str,
    arguments: dict
):

    return asyncio.run(
        call_mcp_tool(
            tool_name,
            arguments
        )
    )
