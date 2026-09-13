from typing import TypedDict


class AgentState(TypedDict):
    user_input: str

    requirements: str
    plan: str

    code: str
    debug: str

    documentation: str
    review: str

    github_status: str
    github_url: str
