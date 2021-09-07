"""
Run the following to install the Github module:

pip3 install PyGithub
"""
from github import Github

"""
create a credentials.py with the following content:

user = 'your username'
password = 'your personal access token'
"""
from credentials import user, password

print("| Repository | Description |")
print("--- | ---")

g = Github(user, password)
res = g.search_code("github.com/caddyserver/caddy/v2 filename:go.mod")
for result in res:
    repo = result.repository
    if repo.description is not None and repo.name != "Caddy":
        print(f"| [{repo.full_name}]({repo.html_url}) | {repo.description} |")
