import customtkinter as ctk
from tkinter import filedialog, messagebox
import os
import markdown

# Configuração do tema
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# Janela principal
janela = ctk.CTk()
janela.title("Editor Markdown com Pré-Visualização")
janela.geometry("1000x600")

# Frame principal
frame_principal = ctk.CTkFrame(janela)
frame_principal.pack(padx=10, pady=(10, 0), fill="both", expand=True)

# Editor Markdown
texto_md = ctk.CTkTextbox(frame_principal, width=480, font=("Ubuntu Mono", 13))
texto_md.pack(side="left", fill="both", expand=True, padx=(0, 5))

# Pré-visualização HTML
preview_html = ctk.CTkTextbox(frame_principal, width=480, font=("Sans", 12), state="disabled")
preview_html.pack(side="right", fill="both", expand=True, padx=(5, 0))

# Variável de caminho
ficheiro_atual = None

# Funções principais
def novo_ficheiro():
    global ficheiro_atual
    texto_md.delete("1.0", "end")
    ficheiro_atual = None
    janela.title("Editor Markdown - Novo ficheiro")

def abrir_ficheiro():
    global ficheiro_atual
    caminho = filedialog.askopenfilename(defaultextension=".md", filetypes=[("Ficheiros Markdown", "*.md"), ("Todos os ficheiros", "*.*")])
    if caminho:
        with open(caminho, "r", encoding="utf-8") as f:
            conteudo = f.read()
            texto_md.delete("1.0", "end")
            texto_md.insert("1.0", conteudo)
        ficheiro_atual = caminho
        janela.title(f"Editor Markdown - {os.path.basename(caminho)}")

def guardar_ficheiro():
    global ficheiro_atual
    if ficheiro_atual:
        with open(ficheiro_atual, "w", encoding="utf-8") as f:
            f.write(texto_md.get("1.0", "end-1c"))
    else:
        guardar_como()

def guardar_como():
    global ficheiro_atual
    caminho = filedialog.asksaveasfilename(defaultextension=".md", filetypes=[("Ficheiros Markdown", "*.md")])
    if caminho:
        with open(caminho, "w", encoding="utf-8") as f:
            f.write(texto_md.get("1.0", "end-1c"))
        ficheiro_atual = caminho
        janela.title(f"Editor Markdown - {os.path.basename(caminho)}")

def sair():
    if messagebox.askokcancel("Sair", "Deseja sair do editor?"):
        janela.destroy()

def inserir_md(tag_inicio, tag_fim=""):
    try:
        selecao = texto_md.get("sel.first", "sel.last")
        texto_md.delete("sel.first", "sel.last")
        texto_md.insert("insert", f"{tag_inicio}{selecao}{tag_fim}")
    except:
        texto_md.insert("insert", f"{tag_inicio}{tag_fim}")

def atualizar_preview():
    markdown_texto = texto_md.get("1.0", "end-1c")
    html_convertido = markdown.markdown(markdown_texto)

    preview_html.configure(state="normal")
    preview_html.delete("1.0", "end")
    preview_html.insert("1.0", html_convertido)
    preview_html.configure(state="disabled")

def ao_digitar(event=None):
    janela.after(300, atualizar_preview)

texto_md.bind("<KeyRelease>", ao_digitar)

# Frame de botões
frame_botoes = ctk.CTkFrame(janela)
frame_botoes.pack(pady=10)

ctk.CTkButton(frame_botoes, text="Negrito", command=lambda: inserir_md("**", "**")).pack(side="left", padx=5)
ctk.CTkButton(frame_botoes, text="Itálico", command=lambda: inserir_md("*", "*")).pack(side="left", padx=5)
ctk.CTkButton(frame_botoes, text="Código", command=lambda: inserir_md("`", "`")).pack(side="left", padx=5)
ctk.CTkButton(frame_botoes, text="Link", command=lambda: inserir_md("[Texto](URL)")).pack(side="left", padx=5)

# Menu
import tkinter as tk
menu_principal = tk.Menu(janela)

menu_ficheiro = tk.Menu(menu_principal, tearoff=0)
menu_ficheiro.add_command(label="Novo", command=novo_ficheiro)
menu_ficheiro.add_command(label="Abrir", command=abrir_ficheiro)
menu_ficheiro.add_command(label="Guardar", command=guardar_ficheiro)
menu_ficheiro.add_command(label="Guardar Como", command=guardar_como)
menu_ficheiro.add_separator()
menu_ficheiro.add_command(label="Sair", command=sair)

menu_principal.add_cascade(label="Ficheiro", menu=menu_ficheiro)
janela.config(menu=menu_principal)

# Iniciar aplicação
janela.mainloop()
