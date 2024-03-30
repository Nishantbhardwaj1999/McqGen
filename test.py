
# Once you add your API key below, make sure to not share it with anyone! The API key should remain private.
OPENAI_API_KEY="sk-KozUFdPlTpJXSJdV7mBsT3BlbkFJDcl3FYjWW9EvLpKQ9Y3K0"


import backoff 
import openai
from openai import OpenAI
client = OpenAI()

@backoff.on_exception(backoff.expo, openai.RateLimitError)
def completions_with_backoff(**kwargs):
    return client.completions.create(**kwargs)
 
completions_with_backoff(model="gpt-3.5-turbo-instruct", prompt="Once upon a time,")