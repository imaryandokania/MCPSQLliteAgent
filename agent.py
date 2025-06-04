from smolagents import ToolCallingAgent, ToolCollection, LiteLLMModel
from mcp import StdioServerParameters

# Set up the model
model = LiteLLMModel(
    model_id="ollama_chat/mistral",
    num_ctx=8192,
)

# Configure server connection
server_parameters = StdioServerParameters(
    command="python3",
    args=["server.py"],
)

# Connect to the tool and run a query
with ToolCollection.from_mcp(server_parameters, trust_remote_code=True) as tool_collection:
    agent = ToolCallingAgent(tools=[*tool_collection.tools], model=model)
    agent.run("Can you tell me which company has the highest revenue?")