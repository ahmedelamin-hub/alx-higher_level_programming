#!/usr/bin/python3
"""
This module retrieves the last 10 commits

Usage: ./100-github_commits.py <repository name> <owner name>
"""

import requests
import sys


def fetch_commits(repo_name, owner_name):
    """
    last10 commits of the given repoy the specified user
    from the GitHub API
    """
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    response = requests.get(url)
    commits = response.json()

    for commit in commits[:10]:
        sha = commit.get('sha')
        author_name = commit.get('commit').get('author').get('name')
        print(f"{sha}: {author_name}")


if __name__ == "__main__":
    if len(sys.argv) == 3:
        repo_name = sys.argv[1]
        owner_name = sys.argv[2]
        fetch_commits(repo_name, owner_name)
