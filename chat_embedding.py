import os
import openai
import faiss
import numpy as np
from dotenv import load_dotenv

# Cargar API Key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Cargar índice FAISS y textos
index = faiss.read_index("vector_index.faiss")
with open("textos.txt", "r", encoding="utf-8") as f:
    textos = [line.strip() for line in f.readlines() if line.strip()]

def get_embedding(text, model="text-embedding-3-small"):
    response = openai.embeddings.create(input=[text], model=model)
    return response.data[0].embedding

def buscar_contexto(pregunta, k=3):
    embedding_pregunta = np.array(get_embedding(pregunta)).astype("float32")
    D, I = index.search(np.array([embedding_pregunta]), k)
    resultados = [textos[i] for i in I[0] if i < len(textos)]
    return resultados

def responder_con_contexto(pregunta):
    contexto = buscar_contexto(pregunta)
    
    if not contexto or all(len(c.strip()) == 0 for c in contexto):
        return "No tengo suficiente información en mi base de conocimiento para responder esa pregunta."

    prompt = f"""Actúa como un asistente experto en Gopass. Responde únicamente con base en la siguiente información."

Contexto:
{chr(10).join(contexto)}

Pregunta: {pregunta}
Respuesta:"""

    respuesta = openai.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )
    
    return respuesta.choices[0].message.content.strip()

# Loop de chat
if __name__ == "__main__":
    print("🟡 Tu pregunta (o 'salir'):", end=" ")
    while True:
        pregunta = input()
        if pregunta.lower() in ["salir", "exit", "quit"]:
            break
        respuesta = responder_con_contexto(pregunta)
        print("\n🤖 Respuesta:\n", respuesta)
        print("\n🟡 Tu pregunta (o 'salir'):", end=" ")
