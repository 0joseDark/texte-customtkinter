import customtkinter as ctk
from tkinter import filedialog, messagebox
import os
import markdown  # Para converter Markdown em HTML

# Configuração
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# Janela principal
janela = ctk.CTk()
janela.title("Editor Markdown com Pré-Visualização")
janela.geometry("1000x600")

# Frame principal dividido em dois: editor e pré-visualização
frame_principal = ctk.CTkFrame(janela)
frame_principal.pack(padx=10, pady=(10, 0), fill="both", expand=True)

# Editor Markdown
texto_md = ctk.CTkTextbox(frame_principal, width=480, font=("Consolas", 14))
texto_md.pack(side="left", fill="both", expand=True, padx=(0, 5))

# Pré-visualização (HTML)
preview_html = ctk.CTkTextbox(frame_principal, width=480, font=("Arial", 12), state="disabled")
preview_html.pack(side="right", fill="both", expand=True, padx=(5, 0))

# Variável para guardar o caminho atual
ficheiro_atual = None

# Funções
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

# Ligação do evento de digitação
def ao_digitar(event=None):
    janela.after(300, atualizar_preview)  # Atualiza após 300ms

texto_md.bind("<KeyRelease>", ao_digitar)

# Frame de botões
frame_botoes = ctk.CTkFrame(janela)
frame_botoes.pack(pady=10)

btn_negrito = ctk.CTkButton(frame_botoes, text="Negrito", command=lambda: inserir_md("**", "**"))
btn_negrito.pack(side="left", padx=5)

btn_italico = ctk.CTkButton(frame_botoes, text="Itálico", command=lambda: inserir_md("*", "*"))
btn_italico.pack(side="left", padx=5)

btn_codigo = ctk.CTkButton(frame_botoes, text="Código", command=lambda: inserir_md("`", "`"))
btn_codigo.pack(side="left", padx=5)

btn_link = ctk.CTkButton(frame_botoes, text="Link", command=lambda: inserir_md("[Texto](URL)"))
btn_link.pack(side="left", padx=5)

# Menu
menu = ctk.CTkMenu(janela)
janela.config(menu=menu)

menu_ficheiro = ctk.CTkMenu(menu, tearoff=0)
menu.add_cascade(label="Ficheiro", menu=menu_ficheiro)
menu_ficheiro.add_command(label="Novo", command=novo_ficheiro)
menu_ficheiro.add_command(label="Abrir", command=abrir_ficheiro)
menu_ficheiro.add_command(label="Guardar", command=guardar_ficheiro)
menu_ficheiro.add_command(label="Guardar Como", command=guardar_como)
menu_ficheiro.add_separator()
menu_ficheiro.add_command(label="Sair", command=sair)

# Iniciar janela
janela.mainloop()
