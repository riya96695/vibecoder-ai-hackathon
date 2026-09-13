from langchain_groq import ChatGroq

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0
)


def debug_agent(state):

    prompt = f"""
    You are a Senior Debugging Engineer.

    Review the following code:

    {state["code"]}

    Find:
    - Syntax Errors
    - Runtime Issues
    - Logic Bugs
    - Security Problems

    Suggest fixes and improvements.
    """

    response = llm.invoke(prompt)

    state["debug"] = response.content

    return state
