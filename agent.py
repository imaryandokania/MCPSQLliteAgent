#!/usr/bin/env python3
import sys
from smolagents import ToolCallingAgent, ToolCollection, LiteLLMModel
from mcp import StdioServerParameters

def main():
    if len(sys.argv) < 2:
        print("Usage: agent.py \"your question here\"")
        sys.exit(1)

    prompt = " ".join(sys.argv[1:])  

    model = LiteLLMModel(
        model_id="ollama_chat/mistral",
        num_ctx=8192,
    )

    server_parameters = StdioServerParameters(
        command="python3",
        args=["server.py"],
    )

    with ToolCollection.from_mcp(server_parameters, trust_remote_code=True) as tool_collection:
        agent = ToolCallingAgent(tools=[*tool_collection.tools], model=model)
        response = agent.run(prompt)
        print(response)

if __name__ == "__main__":
    main()