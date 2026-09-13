from langchain_groq import ChatGroq

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.4
)


def documentation_agent(state):

    prompt = f"""
    Create professional documentation for:

    Requirements:
    {state["requirements"]}

    Plan:
    {state["plan"]}

    Code:
    {state["code"]}

    Generate:

    1. README
    2. Installation Guide
    3. Usage Instructions
    4. API Documentation
    """

    response = llm.invoke(prompt)

    state["documentation"] = response.content

    return state
