from ollama import chat

with open("meeting.txt", "r") as file:
    meeting_notes = file.read()

prompt = f"""
You are an experienced Program Manager.

Analyze the meeting notes and provide:

1. Executive Summary
2. Action Items
3. Risks
4. Next Steps

Meeting Notes:
{meeting_notes}
"""

response = chat(
    model='llama3.2',
    messages=[
        {
            'role': 'user',
            'content': prompt
        }
    ]
)

print(response['message']['content'])

output = response['message']['content']

with open("meeting_minutes.txt", "w") as file:
    file.write(output)

print("Meeting minutes generated successfully!")