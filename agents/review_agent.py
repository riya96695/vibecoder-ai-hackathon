from langchain_groq import ChatGroq

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.2
)


def review_agent(state):

    prompt = f"""
    You are a Principal Software Reviewer.

    Review:

    Requirements:
    {state["requirements"]}

    Plan:
    {state["plan"]}

    Code:
    {state["code"]}

    Debug Report:
    {state["debug"]}

    Provide:

    1. Code Quality Score (/10)
    2. Scalability Review
    3. Security Review
    4. Maintainability Review
    5. Final Recommendations
    """

    response = llm.invoke(prompt)

    state["review"] = response.content

    return state
