from dotenv import load_dotenv
import os
from groq import Groq
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo

load_dotenv()

web_agent = Agent(
    name="Web Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)

if __name__ == "__main__":
    web_agent.print_response("Who are you?")
