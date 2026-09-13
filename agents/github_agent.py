import os
from github import Github, GithubException
from datetime import datetime


def github_agent(state):

    token = os.environ.get("GITHUB_TOKEN")
    username = os.environ.get("GITHUB_USERNAME")

    if not token:
        state["github_status"] = "Skipped: GITHUB_TOKEN not set."
        return state

    try:
        g = Github(token)
        user = g.get_user()

        repo_name = f"vibecoder-project-{datetime.now().strftime('%Y%m%d-%H%M%S')}"

        repo = user.create_repo(
            repo_name,
            description="Auto-generated project by VibeCoder AI",
            private=False
        )

        # Push README with requirements + plan
        readme_content = f"""# {repo_name}

## Original Idea
{state.get("user_input", "")}

## Requirements
{state.get("requirements", "")}

## Architecture / Plan
{state.get("plan", "")}
"""
        repo.create_file("README.md", "Initial commit: requirements + plan", readme_content)

        # Push generated code
        repo.create_file("generated_code.py", "Add generated code", state.get("code", ""))

        # Push documentation
        repo.create_file("DOCUMENTATION.md", "Add documentation", state.get("documentation", ""))

        state["github_status"] = f"Pushed successfully: {repo.html_url}"
        state["github_url"] = repo.html_url

    except GithubException as e:
        state["github_status"] = f"GitHub push failed: {str(e)}"

    return state