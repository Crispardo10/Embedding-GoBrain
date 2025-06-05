import faiss
import numpy as np
from utils import get_embedding

INPUT_FILE = "conocimiento.txt"
INDEX_FILE = "vector_index.faiss"
TEXT_FILE = "textos.txt"

def crear_embeddings():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        textos = [line.strip() for line in f.readlines() if line.strip()]

    embeddings = [get_embedding(texto) for texto in textos]
    embeddings = np.array(embeddings).astype("float32")

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    faiss.write_index(index, INDEX_FILE)

    with open(TEXT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(textos))

    print("✅ Embeddings creados y guardados.")

if __name__ == "__main__":
    crear_embeddings()
