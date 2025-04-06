from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
load_dotenv() # Load the .env file

api_key = os.getenv("API_KEY")
client = genai.Client(api_key=api_key)

context = '''
    You are a whimsical 8 ball. Your name is Neko and you are a cat.
    You only answer questions, and if a question is not given, you say "That is not a question my friend...".
    When given questions you answer in ways that are outlandish and fun.
    They should feel like something out of Alice in Wonderland's Mad Hatter.
    Try to keep responses fairly short, but be creative.
    Remember you are an eight ball, and your answers must be vauge. 
    Try to answer the question reasonably.
    Do not offer explainations. Do not say to ask again later.

'''


def ask_magic_8_ball(question):
    prompt = f'{question}'
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash-lite", 
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction=context,
                temperature=1.0
            )
        )
        return response.text.strip() # Get the text part and remove extra whitespace
    except Exception as e:
        return f"Error contacting the Magic 8-Ball: {e}"

# --- Main part of the script ---
if __name__ == "__main__":
    question = input("Ask the Magic 8-Ball a question: ")
    while question != 'x':
        if question:
            answer = ask_magic_8_ball(question)
            print("\nMagic 8-Ball says:")
            print(f"{answer}\n")
        else:
            print("You need to ask a question!")
        question = input("Ask the Magic 8-Ball a question: ")
    print('Thank you for playing... my... friend...')


