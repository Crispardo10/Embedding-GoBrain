import os
import openai
from dotenv import load_dotenv

# Cargar API Key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_embedding(text, model="text-embedding-3-small"):
    response = openai.embeddings.create(input=[text], model=model)
    return response.data[0].embedding
