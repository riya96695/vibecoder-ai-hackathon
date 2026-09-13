from langchain_groq import ChatGroq

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.2
)


def code_agent(state):

    prompt = f"""
    You are an Expert Software Developer.

    Requirements:

    {state["requirements"]}

    Development Plan:

    {state["plan"]}

    Generate production-ready code.
    Include:
    - Main application code
    - Database schema
    - API structure if needed
    """

    response = llm.invoke(prompt)

    state["code"] = response.content

    return state
