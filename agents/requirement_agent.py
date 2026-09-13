from langchain_groq import ChatGroq

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.3
)


def requirement_agent(state):

    prompt = f"""
    You are a Software Requirement Analyst.

    Analyze the following project idea and generate:

    1. Functional Requirements
    2. Non-Functional Requirements
    3. Recommended Technology Stack

    Project:
    {state["user_input"]}
    """

    response = llm.invoke(prompt)

    state["requirements"] = response.content

    return state
