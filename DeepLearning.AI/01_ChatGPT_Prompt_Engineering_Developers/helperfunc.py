from openai import OpenAI
import json

# Read OpenAI API key
with open('keys.json') as f:
    key = json.load(f)

# set API key in environment variable and read
client = OpenAI(api_key=key['OPENAI_API_KEY'])


# Helper functions
def get_completion(prompt, model='gpt-3.5-turbo'):
    messages = [{'role': 'user', 'content': prompt}]
    res = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return res.choices[0].message.content


def get_completion_from_messages(messages, model='gpt-3.5-turbo', temp=0):
    res = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temp,
    )
    return res.choices[0].message.content
