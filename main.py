from blender_mcp.server import main as server_main
import sys

def main():
    """Entry point for the blender-mcp package.
    
    Runs the MCP server that bridges Blender and Claude AI.
    
    Make sure Blender is running with the blender-mcp addon enabled
    before starting this server, otherwise connections will fail.
    
    Default port is 9876. The Blender addon and this server must use
    the same port to communicate successfully.
    """
    # Print a startup message so it's clear the server is launching
    print("Starting Blender MCP server...", file=sys.stderr)
    print("Tip: Ensure the Blender addon is active before connecting.", file=sys.stderr)
    print("Tip: Check that the port in the addon matches the server port (default: 9876).", file=sys.stderr)
    server_main()

if __name__ == "__main__":
    main()
