import os
from dotenv import load_dotenv
from groq import Groq
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from modules.vertica import create_connection
from custom_tools.query_profile_tools import check_long_running_queries

load_dotenv()

web_agent = Agent(
    name="Web Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[create_connection, check_long_running_queries],
    instructions=["Give the result in a tabular format"],
    show_tool_calls=True,
    markdown=True,
)

if __name__ == "__main__":
    web_agent.print_response("Give me first 20 characters of logn running queris for campaign_report user")
