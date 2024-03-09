from openai import OpenAI
from dotenv import dotenv_values

config = dotenv_values('.env')
client = OpenAI(api_key=config['API_KEY'])

def generate_blog(paragraph_topic):
  response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a very competent language model."},
        {"role": "system", "content": "Answer concisely and informatively."},
        {"role": "user", "content": f"Write a paragraph on the following topic : {paragraph_topic}"}
    ]
  )

  retrieve_blog = response.choices[0].message.content

  return retrieve_blog

print(generate_blog('Why NYC is better than your city.'))

keep_writing = True

while keep_writing:
  answer = input('Write a new paragraph? Y for yes, anything else for no. ')
  if (answer == 'Y'):
    paragraph_topic = input('What should this paragraph talk about? ')
    print(generate_blog(paragraph_topic))
  else:
    keep_writing = False
