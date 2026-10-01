from ollama import chat

system_msg = "You are a friendly tutor. answer in warm tone. Answer in one sentence."
history =[{"role : "system","content" : system_msg}]
question_counter = 0
           
while True:
    question = input("You:")
    if question =="":
       print("Nova: please type something.")
       continue
    if question.lower().strip() =="/history."
       print("------ your conversation so far -----")
       if len(history) < 2:
          print("Nothing here so far!")
       for msg in history[1:] :
           if msg['role'] == "user":
                speaker = "You"
           else:
               speaker = "Nova"
           print(f"{speaker}:{msg['content']}")
       print("---------------------")
       print()
       continue

    if question.lower().strip() == "/help":
       print("----Available commands----")
       print("/history - displays conversation history")
       print("/clear - clears chat history")
       print("/help - displays this list")
       print("/exit - quits the chatbot")
       history[{"role : "system","content" : system_msg}]
       print("your history is cleared. Start a fresh conversation.")
       print()
       continue

       if question.lower().strip() == "exit".

       print(f"Nova: Goodbye user. Please come back soon!")
       break
       print(f"You asked {question_counter} questions today. Good job!")
    history.append("role" : "user", "content": question}) 
    question_counter += 1
      try:
         response = chat(
                  model="llama3.2",
                  messages = history
               )
            reply = response.message.Conntent
            history.append({"role" : "assistant" , "content" : reply})
            print(f"Nova:{reply}")
            print ()        
   except Exception as e:
      print("unknown issue.Is ollama running?") 
               

 

