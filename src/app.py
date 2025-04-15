from fastapi import FastAPI
from fastapi_mcp import FastApiMCP


app = FastAPI(
    title="My FastAPI",
    description="This is a sample FastAPI application",
    version="0.0.1",
    redirect_slashes=False
)

@app.get("/", operation_id="get_root")
def get_root():
    return {"message": "FastAPI running in a Docker container"}


mcp = FastApiMCP(
    app,
    name="My API MCP",
    description="My API description",
    base_url="http://localhost:80",
    include_operations=["get_root"]
    # describe_all_responses=True,     # Include all possible response schemas in tool descriptions
    # describe_full_response_schema=True  # Include full JSON schema in tool descriptions
)
mcp.mount(app)

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app)