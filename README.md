# text editor with customtkinter 
**pré-visualização Markdown em tempo real** ao teu editor!
- Usado o módulo `markdown` para converter o texto para HTML, e um widget de `CTkTextbox` à direita para mostrar o conteúdo convertido.

---

### ✅ Pré-requisitos:

Instala o módulo necessário:

```bash
pip install markdown
```

---

### 🧩 Melhorias incluídas:

* **Divisão da janela** em duas partes:

  * À esquerda: Editor Markdown
  * À direita: Pré-visualização em HTML (convertido)
* **Atualização automática** da pré-visualização sempre que o texto muda (tempo real)

---

### 🎯 Resultado:

* Tudo o que escreveres na esquerda (Markdown), aparece formatado como HTML na direita.
* Atualização ocorre em tempo real com cada tecla.
* Visualização serve para ver a estrutura final do Markdown (ideal para testes rápidos!).
---
- **Ubuntu Linux**

1. O script seja **compatível com o ambiente gráfico do Ubuntu**.
2. O `CustomTkinter`, `markdown` e os demais pacotes estejam instalados.
3. O script funcione bem com **fontes e codificação UTF-8**, comuns no Ubuntu.

---

### ✅ Passos prévios no Ubuntu:

Abre o terminal e instala as dependências:

```bash
sudo apt update
sudo apt install python3 python3-pip -y
pip install customtkinter markdown
```

> ⚠️ No Ubuntu, `tkinter` pode já vir instalado. Se não, instala com:

```bash
sudo apt install python3-tk
```

### 🧪 Testar:

1. Corre o script com:

   ```bash
   python3 editor_markdown_linux.py
   ```
2. Abre, edita e grava ficheiros `.md`.
3. Vê a pré-visualização em tempo real à direita.
