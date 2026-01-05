from pydantic import BaseModel
from agents import Agent

NUMBER_OF_SEARCHES = 3

INSTRUCTIONS = f"You are a helpful research assistant. Given a query, come up with a set of web searches \
to perform to best answer the query. Output {NUMBER_OF_SEARCHES} terms to query for."

class WebSearchItem(BaseModel):
    reason: str
    """Your justifications for why this search is important."""
    query: str
    """The search query to perform."""

class WebSearchPlan(BaseModel):
    searches: list[WebSearchItem]
    """The set of search queries to perform."""

planner_agent = Agent(
    name="WebSearchPlanner",
    instructions=INSTRUCTIONS,
    model="gpt-4o-mini",
    output_type=WebSearchPlan,
)