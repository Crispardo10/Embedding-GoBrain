from search import buscar_contexto
import openai

def responder_con_contexto(pregunta):
    contexto = buscar_contexto(pregunta)
    
    if not contexto or all(len(c.strip()) == 0 for c in contexto):
        return "No tengo suficiente información para responder esa pregunta."

    prompt = f"""Actúa como un asistente experto en Gopass que se llama Gobrain. Responde con base en la información que te se te doy, se amable y tecnica.

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

if __name__ == "__main__":
    print("🟡 Tu pregunta (o 'salir'):", end=" ")
    while True:
        pregunta = input()
        if pregunta.lower() in ["salir", "exit", "quit"]:
            break
        respuesta = responder_con_contexto(pregunta)
        print("\n🤖 Respuesta:\n", respuesta)
        print("\n🟡 Tu pregunta (o 'salir'):", end=" ")
