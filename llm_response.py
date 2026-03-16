from groq import Groq
import os
import json
from dotenv import load_dotenv

load_dotenv()


client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def find_patterns(alerts):

    alerts_text = json.dumps(alerts, indent=2)

    prompt = f"""
    You are a cybersecurity analyst. 
    Analyze these SSH brute force alerts and identify 
    any patterns, connections, or coordinated attacks.
    
    Alerts:
    {alerts_text}
    
    Look for:
    - IPs from the same country attacking close together
    - Similar timing patterns suggesting automation
    - Any other suspicious correlations
    """

    # Step 3 — call the API
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )


    # Step 4 — extract and return the text response
    return response.choices[0].message.content