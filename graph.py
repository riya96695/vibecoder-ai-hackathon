from langgraph.graph import StateGraph, END

from state import AgentState

from agents.requirement_agent import requirement_agent
from agents.planning_agent import planning_agent
from agents.code_agent import code_agent
from agents.debug_agent import debug_agent
from agents.documentation_agent import documentation_agent
from agents.review_agent import review_agent
from agents.github_agent import github_agent


def build_graph():

    workflow = StateGraph(AgentState)

    # Nodes
    workflow.add_node("requirement_agent", requirement_agent)
    workflow.add_node("planning_agent", planning_agent)
    workflow.add_node("code_agent", code_agent)
    workflow.add_node("debug_agent", debug_agent)
    workflow.add_node("documentation_agent", documentation_agent)
    workflow.add_node("review_agent", review_agent)
    workflow.add_node("github_agent", github_agent)

    # Flow
    workflow.set_entry_point("requirement_agent")

    workflow.add_edge(
        "requirement_agent",
        "planning_agent"
    )

    workflow.add_edge(
        "planning_agent",
        "code_agent"
    )

    workflow.add_edge(
        "code_agent",
        "debug_agent"
    )

    workflow.add_edge(
        "debug_agent",
        "documentation_agent"
    )

    workflow.add_edge(
        "documentation_agent",
        "review_agent"
    )

    workflow.add_edge(
        "review_agent",
        "github_agent"
    )

    workflow.add_edge(
        "github_agent",
        END
    )

    return workflow.compile()
