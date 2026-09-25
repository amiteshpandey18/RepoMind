from src.repomind.agent.tools import search_repository, get_commits


result = search_repository.invoke(
    "What authentication does this project use?"
)

print()
print("==============================")
print("Search Repository Tool")
print("==============================")
print(result)


commits = get_commits.invoke({})

print()
print("==============================")
print("Commits Tool")
print("==============================")
print(commits)