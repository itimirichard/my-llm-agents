import os
from typing import Dict

import sendgrid
from sendgrid.helpers.mail import Mail, Email, Content, To
from agents import Agent, function_tool

@function_tool
def send_email(subject: str, html_body: str) -> Dict[str, str]:
    """Send an email to the user."""
    sg = sendgrid.SendGridAPIClient(api_key=os.getenv("SENDGRID_API_KEY"))
    from_email = Email("") # TODO: Add your email here
    to_email = To("") # TODO: Add the email of the recipient here
    content = Content("text/html", html_body)
    mail = Mail(from_email, to_email, subject, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print("Email response: ", response.status_code)
    return {"message": "Email sent successfully"}

INSTRUCTIONS = """You are able to send a nicely formatted HTML email based on a detailed report.
You will be provided with a detailed report. You should use your tool to send one email, providing the 
report converted into clean, well presented HTML with an appropriate subject line."""

email_agent = Agent(
    name="EmailAgent",
    instructions=INSTRUCTIONS,
    model="gpt-4o-mini",
    tools=[send_email],
)