# ai_helper.py
import os
import openai
from typing import Optional


openai.api_key = os.getenv('OPENAI_API_KEY')


SYSTEM_PROMPT = (
'You are an assistant for a Multi-Domain Intelligence Platform. Respond concisely, and when asked provide step-by-step actionable recommendations.'
)


def ask_assistant(user_prompt: str, model: str = 'gpt-4o-mini') -> Optional[str]:
if not openai.api_key:
return 'OPENAI_API_KEY not configured.'
try:
resp = openai.ChatCompletion.create(
model=model,
messages=[{'role':'system','content':SYSTEM_PROMPT}, {'role':'user','content':user_prompt}],
temperature=0.2,
max_tokens=400
)
return resp['choices'][0]['message']['content'].strip()
except Exception as e:
return f'Error calling OpenAI: {e}'