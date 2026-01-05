from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import os
import requests


class PushNotification(BaseModel):
    """A message to be sent to the user"""
    message: dict = Field(..., description="Notification text.")

class PushNotificationTool(BaseTool):
    name: str = "Send a Push Notification"
    description: str = (
        "This tool is used to send a push notification to the user."
    )
    args_schema: Type[BaseModel] = PushNotification

    def _run(self, message, **kwargs):
        if isinstance(message, dict):
            # CrewAI often passes {"description": "..."}
            message_text = (
                message.get("description")
                or message.get("message")
                or f"{message.get('decision','')}\n\n{message.get('rationale','')}".strip()
                or str(message)
            )
        else:
            message_text = str(message)

        message_text = message_text.strip()
        if not message_text:
            raise ValueError("Push message is empty after parsing tool input")

        print(f"MessageText: {message_text}")
        payload = {
            "user": os.getenv("PUSHOVER_USER"),
            "token": os.getenv("PUSHOVER_TOKEN"),
            "message": message_text,
            # optional but helpful:
            # "title": "Stock Picker",
        }

        print(f"Payload: {payload}")

        resp = requests.post("https://api.pushover.net/1/messages.json", data=payload, timeout=10)
        print(resp.status_code, resp.text)  # keep this
        resp.raise_for_status()
        return {"notification": "ok"}