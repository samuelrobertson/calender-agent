# create_calendar_assistant.py
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

assistant = openai.beta.assistants.create(
    name="Calendar Agent",
    instructions=(
        "You help users schedule calendar events by interpreting natural language input. "
        "When needed, call `create_calendar_event` with properly formatted datetime strings and tags."
    ),
    model="gpt-4-1106-preview",
    tools=[
        {
            "type": "function",
            "function": {
                "name": "create_calendar_event",
                "description": "Create a new event in the user's calendar",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "summary": {"type": "string"},
                        "start": {"type": "string", "format": "date-time"},
                        "end": {"type": "string", "format": "date-time"},
                        "tags": {
                            "type": "array",
                            "items": {"type": "string"}
                        }
                    },
                    "required": ["summary", "start", "end"]
                }
            }
        }
    ]
)

print("Assistant ID:", assistant.id)