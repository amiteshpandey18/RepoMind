from src.repomind.agent.graph import app


result = app.invoke({
    "question": "What are the recent commits in this project?",
    "context": "",
    "answer": ""
})


print()
print("==============================")
print("LangGraph Result")
print("==============================")
print(result)