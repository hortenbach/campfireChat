from decouple import config
import openai
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = config('API_KEY')

openai.api_key = SECRET_KEY

openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)

response = openai.Completion.create(
    engine='text-davinci-003',
    prompt='Hello, how are you?',
    max_tokens=50,
    n=1,
    stop=None,
)

reply = response.choices[0].text.strip()
print(reply)
