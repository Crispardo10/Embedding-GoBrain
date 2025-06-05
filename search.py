import faiss
import numpy as np
from utils import get_embedding

INDEX_FILE = "vector_index.faiss"
TEXT_FILE = "textos.txt"

# Cargar índice y textos
index = faiss.read_index(INDEX_FILE)
with open(TEXT_FILE, "r", encoding="utf-8") as f:
    textos = [line.strip() for line in f.readlines() if line.strip()]

def buscar_contexto(pregunta, k=3):
    embedding = np.array(get_embedding(pregunta)).astype("float32")
    D, I = index.search(np.array([embedding]), k)
    return [textos[i] for i in I[0] if i < len(textos)]
