from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.tracers.langchain import wait_for_all_tracers
import os

from dotenv import load_dotenv
load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from tavily import TavilyClient

tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
@tool
def search(query: str) -> str:
    """
    Tool that searches over internet
    Args:
        query: The query to search for
    Returns:
        The search result
    """
    print(f"Searching for: {query}")
    return tavily_client.search(query)

llm = ChatOpenAI(
    model="gpt-oss-20b",
    base_url="http://localhost:8080/v1",
    api_key="not-needed",
    temperature=1.0,
)
tools = [search]
agent = create_agent(model=llm, tools=tools)


def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages": [HumanMessage(content="top 2 job postings for lang chain in India?")]})
    print(result)



if __name__ == "__main__":
    main()
