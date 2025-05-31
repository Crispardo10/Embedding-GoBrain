import os
import openai
import faiss
import numpy as np
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_embedding(text, model="text-embedding-3-small"):
    response = openai.embeddings.create(input=[text], model=model)
    return response.data[0].embedding

# Leer los textos base
with open("conocimiento.txt", "r", encoding="utf-8") as f:
    textos = [line.strip() for line in f.readlines() if line.strip()]

# Crear embeddings
embeddings = [get_embedding(texto) for texto in textos]
embeddings = np.array(embeddings).astype("float32")

# Guardar el índice
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)
faiss.write_index(index, "vector_index.faiss")

# Guardar los textos
with open("textos.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(textos))

print("✅ Embeddings creados y guardados.")
