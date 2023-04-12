

from threading import BrokenBarrierError
import openai
import os

api_key = os.environ["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"]
model_engine = 'text-davinci-002'
prompt = 'Discuss games'
max_tokens = 150
temperature = 0.5

async def generate_response(user_message):
    completions = await openai.Completion.create(
        engine=model_engine,
        prompt=prompt + "\nUser: " + user_message + "\nAI:",
        max_tokens=max_tokens,
        temperature=temperature,
    )
    message = completions.choices[0].text
    return message.strip()

print("Welcome to the game discussion chatbot!")

async def generate_response(user_message):
   completions = await openai.Completion.create(
       engine=model_engine,
       prompt=prompt + "\nUser: " + user_message + "\nAI:",
       max_tokens=max_tokens,
       temperature=temperature,
   )
   message = completions.choices[0].text
   return message.strip()
