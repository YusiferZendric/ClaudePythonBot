import requests
import os
import threading
import time
def sc():
    os.system("node clewd.js")  # starts the endpoint

a = threading.Thread(target=sc)
a.start()

url = "http://127.0.0.1:8444/v1/chat/completions"
headers = {
    "Content-Type": "application/json"
}

time.sleep(3)
assistant_personality = input("Set the assistant's personality and identity: ")

messages = [
    {"role": "system", "content": f"Roleplay as {assistant_personality}"}
]

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break

    messages.append({"role": "user", "content": user_input})

    data = {
        "model": "claude-3-5-sonnet-20240620",
        "messages": messages,
        "max_tokens": 1024,
        "stream": False
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        ai_response = result['choices'][0]['message']['content']
        print("AI:", ai_response)
        messages.append({"role": "assistant", "content": ai_response})
    else:
        print(f"Error: {response.status_code} - {response.text}")

print("Chat ended.")
