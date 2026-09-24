from ollama import chat

while True:
    question = input("You:")
    if question.lower().strip() == "exit":
       print(f"Nova: Goodbye user. Please come back soon!")
       break
    response = chat(
            model="llama3.2",
            messages = [
                {
                    "role" : "user",
                    "content" : question
                }  
            ]
    )

    print(f"Nova:{response.message.content}")
