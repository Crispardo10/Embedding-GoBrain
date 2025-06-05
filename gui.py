import tkinter as tk
from tkinter import scrolledtext
from chatbot import responder_con_contexto

# Crear ventana principal
root = tk.Tk()
root.title("Gobrain - Asistente Gopass")
root.geometry("600x500")
root.resizable(False, False)

# Título
title = tk.Label(root, text="🤖 Gobrain - Asistente de Gopass", font=("Helvetica", 16, "bold"))
title.pack(pady=10)

# Área de respuesta
output_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=20, font=("Helvetica", 11))
output_area.pack(padx=10, pady=10)
output_area.configure(state="disabled")

# Entrada de pregunta
input_frame = tk.Frame(root)
input_frame.pack(pady=5)

entry = tk.Entry(input_frame, width=50, font=("Helvetica", 12))
entry.grid(row=0, column=0, padx=5)

def enviar_pregunta():
    pregunta = entry.get().strip()
    if not pregunta:
        return
    output_area.configure(state="normal")
    output_area.insert(tk.END, f"🟡 Tú: {pregunta}\n")
    output_area.insert(tk.END, "🤖 Gobrain: Pensando...\n")
    output_area.see(tk.END)
    output_area.update_idletasks()
    respuesta = responder_con_contexto(pregunta)
    output_area.delete("end-2l", "end-1l")  # Eliminar "Pensando..."
    output_area.insert(tk.END, f"🤖 Gobrain: {respuesta}\n\n")
    output_area.configure(state="disabled")
    entry.delete(0, tk.END)

# Botón para enviar
send_button = tk.Button(input_frame, text="Enviar", command=enviar_pregunta, font=("Helvetica", 12))
send_button.grid(row=0, column=1)

# Vincular Enter
entry.bind("<Return>", lambda event: enviar_pregunta())

# Ejecutar interfaz
root.mainloop()
