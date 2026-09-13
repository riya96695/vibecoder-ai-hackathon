from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from graph import build_graph

# Page Config
st.set_page_config(
    page_title="VibeCoder AI",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 VibeCoder AI")
st.subheader("Multi-Agent System for Automated Code Generation and Development Support")

st.markdown("""
Transform your project ideas into software solutions using collaborative AI agents.
""")

# User Input
user_prompt = st.text_area(
    "Describe your project idea:",
    height=200,
    placeholder="Example: Create an e-commerce website with user authentication, payment gateway, and admin dashboard."
)

# Run Button
if st.button("🚀 Generate Project"):

    if not user_prompt.strip():
        st.warning("Please enter a project description.")
    else:

        with st.spinner("Running AI Agents..."):

            graph = build_graph()

            result = graph.invoke(
                {
                    "user_input": user_prompt,
                    "requirements": "",
                    "plan": "",
                    "code": "",
                    "debug": "",
                    "documentation": "",
                    "review": ""
                }
            )

        st.success("Project Generated Successfully!")

        # Requirements
        st.header("📋 Requirements Analysis")
        st.write(result["requirements"])

        # Plan
        st.header("📝 Development Plan")
        st.write(result["plan"])

        # Code
        st.header("💻 Generated Code")
        st.code(result["code"], language="python")

        # Debugging
        st.header("🐞 Debug Report")
        st.write(result["debug"])

        # Documentation
        st.header("📚 Documentation")
        st.write(result["documentation"])

        # Review
        st.header("✅ Code Review")
        st.write(result["review"])

# Sidebar
with st.sidebar:
    st.title("⚙️ Agents")

    st.markdown("""
    ### Active Agents

    ✅ Requirement Analysis Agent

    ✅ Planning Agent

    ✅ Code Generation Agent

    ✅ Debugging Agent

    ✅ Documentation Agent

    ✅ Review Agent
    """)

    st.markdown("---")

    st.info(
        "VibeCoder AI uses LangGraph-based multi-agent workflows "
        "to automate software development."
    )
