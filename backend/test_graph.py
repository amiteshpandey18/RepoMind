from repomind.agent.graph import app


config = {
    "configurable": {
        "thread_id": "repo-1"
    }
}


result1 = app.invoke(
    {
        "question": "What authentication does this project use?",
        "context": "",
        "answer": "",
        "tool": "",
        "messages": [
            {
                "role": "user",
                "content": "What authentication does this project use?"
            }
        ]
    },
    config=config
)


print()
print("==============================")
print("Question 1")
print("==============================")
print(result1["answer"])


result2 = app.invoke(
    {
        "question": "What library is used for password hashing?",
        "context": "",
        "answer": "",
        "tool": "",
        "messages": [
            {
                "role": "user",
                "content": "What library is used for password hashing?"
            }
        ]
    },
    config=config
)


print()
print("==============================")
print("Question 2")
print("==============================")
print(result2["answer"])


result3 = app.invoke(
    {
        "question": "Why is it used?",
        "context": "",
        "answer": "",
        "tool": "",
        "messages": [
            {
                "role": "user",
                "content": "Why is it used?"
            }
        ]
    },
    config=config
)


print()
print("==============================")
print("Question 3")
print("==============================")
print(result3["answer"])
