import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("OPENAI_KEY")

client = OpenAI(
    api_key=key,
)

messages = []

def completion(message):
    global messages
    messages.append(
        {
            "role":"user",
            "content": message
        }
    )

    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages = messages
        )

    message = {
        "role":"assistant",
        "content": chat_completion.choices[0].message.content
    }
    messages.append(message)
    print(f"Jarvis: {message["content"]}")


if __name__ == "__main__":
    print(f"Jarvis: Hi, I am Jarvis, how may I help you?\n")
    while(True):
        user_question = input()
        print(f"User: {user_question}")
        completion(user_question)