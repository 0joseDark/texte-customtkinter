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
---
**compatível com Windows 10 e Ubuntu Linux**.

---

## ✅ Módulos Usados no Script

### 1. **`customtkinter`**

* **Descrição**: Interface gráfica moderna baseada no `tkinter`, com temas escuros, claros e estilos modernos.
* **Instalação**:

  ```bash
  pip install customtkinter
  ```
* **Compatível com**: Windows 10 e Ubuntu Linux.
* **Função no script**: Cria a janela principal, caixas de texto, botões e estrutura visual com aparência moderna.

---

### 2. **`tkinter` (embutido no Python)**

* **Descrição**: Toolkit de GUI nativo do Python (usado por `customtkinter` internamente).
* **Instalação**:

  * Windows: já vem com o Python.
  * Ubuntu:

    ```bash
    sudo apt install python3-tk
    ```
* **Compatível com**: Windows 10 e Ubuntu Linux.
* **Função no script**:

  * Utilizado indiretamente por `customtkinter`.
  * Também usado diretamente para criar o **menu** da janela (`tk.Menu`).

---

### 3. **`markdown`**

* **Descrição**: Biblioteca Python que converte texto em Markdown para HTML.
* **Instalação**:

  ```bash
  pip install markdown
  ```
* **Compatível com**: Windows 10 e Ubuntu Linux.
* **Função no script**:

  * Converte o conteúdo do editor (Markdown) em HTML.
  * O HTML convertido é exibido na caixa de pré-visualização do lado direito.

---

### 4. **`os`** (módulo padrão do Python)

* **Descrição**: Permite interações com o sistema operativo (caminhos, ficheiros, nomes).
* **Instalação**: Já vem com o Python.
* **Função no script**:

  * Obtém o nome do ficheiro ao abrir ou guardar.
  * Trabalha com caminhos de ficheiros de forma portátil.

---

### 5. **`filedialog` e `messagebox` do `tkinter`**

* **Descrição**: Janelas para abrir/guardar ficheiros e mostrar mensagens de confirmação ou erro.
* **Instalação**:

  * Windows: incluído com o Python.
  * Ubuntu: com `python3-tk`.
* **Função no script**:

  * `filedialog.askopenfilename()`: abrir ficheiro.
  * `filedialog.asksaveasfilename()`: guardar ficheiro.
  * `messagebox.askokcancel()`: perguntar ao utilizador se deseja sair.

---

## 📦 Instalação de Todos os Módulos

### ✅ Para Windows 10

1. Garante que tens Python 3 instalado:

   ```bash
   python --version
   ```
2. Instala os módulos:

   ```bash
   pip install customtkinter markdown
   ```

---

### ✅ Para Ubuntu Linux

1. Garante que tens Python 3 e o pip:

   ```bash
   sudo apt update
   sudo apt install python3 python3-pip -y
   ```
2. Instala o `tkinter` (interface gráfica):

   ```bash
   sudo apt install python3-tk
   ```
3. Instala os módulos Python necessários:

   ```bash
   pip install customtkinter markdown
   ```

---

## ✅ Resumo Rápido (Tabela)

| Módulo          | Descrição                         | Instalação Windows          | Instalação Ubuntu Linux       |
| --------------- | --------------------------------- | --------------------------- | ----------------------------- |
| `customtkinter` | Interface gráfica moderna         | `pip install customtkinter` | `pip install customtkinter`   |
| `tkinter`       | Interface gráfica base (padrão)   | Incluído no Python          | `sudo apt install python3-tk` |
| `markdown`      | Conversor Markdown → HTML         | `pip install markdown`      | `pip install markdown`        |
| `os`            | Sistema de ficheiros e caminhos   | Já incluído                 | Já incluído                   |
| `filedialog`    | Abrir/guardar ficheiros (tkinter) | Incluído no `tkinter`       | Incluído em `python3-tk`      |
| `messagebox`    | Janelas de mensagem (tkinter)     | Incluído no `tkinter`       | Incluído em `python3-tk`      |

---

gerar um script `requirements.txt` e um `.sh` para instalar tudo no Ubuntu automaticamente.
---
Perfeito! Aqui estão os dois ficheiros que pediste:

---

## 📄 1. `requirements.txt`

Este ficheiro define os módulos Python necessários:

```txt
customtkinter
markdown
```

---

## ⚙️ 2. Script Bash: `instalar_dependencias.sh`

Este script instala tudo automaticamente no **Ubuntu Linux**:

```bash
#!/bin/bash

echo "🔧 Atualizar o sistema..."
sudo apt update

echo "🧱 Instalar Python3 e pip3..."
sudo apt install -y python3 python3-pip

echo "🖼️ Instalar tkinter para GUI..."
sudo apt install -y python3-tk

echo "📦 Instalar dependências Python com pip..."
pip3 install -r requirements.txt

echo "✅ Instalação completa!"
```

---

## ✅ Como Usar

1. **Cria os ficheiros:**

   * Guarda o seguinte conteúdo como `requirements.txt`.
   * Guarda o script como `instalar_dependencias.sh`.

2. **Dá permissões de execução ao script:**

   ```bash
   chmod +x instalar_dependencias.sh
   ```

3. **Executa o script:**

   ```bash
   ./instalar_dependencias.sh
   ```

---

Claro! Vamos **listar, desenvolver e explicar todos os módulos usados** no script do editor Markdown com pré-visualização em tempo real, **compatível com Windows 10 e Ubuntu Linux**.

---

## ✅ Módulos Usados no Script

### 1. **`customtkinter`**

* **Descrição**: Interface gráfica moderna baseada no `tkinter`, com temas escuros, claros e estilos modernos.
* **Instalação**:

  ```bash
  pip install customtkinter
  ```
* **Compatível com**: Windows 10 e Ubuntu Linux.
* **Função no script**: Cria a janela principal, caixas de texto, botões e estrutura visual com aparência moderna.

---

### 2. **`tkinter` (embutido no Python)**

* **Descrição**: Toolkit de GUI nativo do Python (usado por `customtkinter` internamente).
* **Instalação**:

  * Windows: já vem com o Python.
  * Ubuntu:

    ```bash
    sudo apt install python3-tk
    ```
* **Compatível com**: Windows 10 e Ubuntu Linux.
* **Função no script**:

  * Utilizado indiretamente por `customtkinter`.
  * Também usado diretamente para criar o **menu** da janela (`tk.Menu`).

---

### 3. **`markdown`**

* **Descrição**: Biblioteca Python que converte texto em Markdown para HTML.
* **Instalação**:

  ```bash
  pip install markdown
  ```
* **Compatível com**: Windows 10 e Ubuntu Linux.
* **Função no script**:

  * Converte o conteúdo do editor (Markdown) em HTML.
  * O HTML convertido é exibido na caixa de pré-visualização do lado direito.

---

### 4. **`os`** (módulo padrão do Python)

* **Descrição**: Permite interações com o sistema operativo (caminhos, ficheiros, nomes).
* **Instalação**: Já vem com o Python.
* **Função no script**:

  * Obtém o nome do ficheiro ao abrir ou guardar.
  * Trabalha com caminhos de ficheiros de forma portátil.

---

### 5. **`filedialog` e `messagebox` do `tkinter`**

* **Descrição**: Janelas para abrir/guardar ficheiros e mostrar mensagens de confirmação ou erro.
* **Instalação**:

  * Windows: incluído com o Python.
  * Ubuntu: com `python3-tk`.
* **Função no script**:

  * `filedialog.askopenfilename()`: abrir ficheiro.
  * `filedialog.asksaveasfilename()`: guardar ficheiro.
  * `messagebox.askokcancel()`: perguntar ao utilizador se deseja sair.

---

## 📦 Instalação de Todos os Módulos

### ✅ Para Windows 10

1. Garante que tens Python 3 instalado:

   ```bash
   python --version
   ```
2. Instala os módulos:

   ```bash
   pip install customtkinter markdown
   ```

---

### ✅ Para Ubuntu Linux

1. Garante que tens Python 3 e o pip:

   ```bash
   sudo apt update
   sudo apt install python3 python3-pip -y
   ```
2. Instala o `tkinter` (interface gráfica):

   ```bash
   sudo apt install python3-tk
   ```
3. Instala os módulos Python necessários:

   ```bash
   pip install customtkinter markdown
   ```

---

## ✅ Resumo Rápido (Tabela)

| Módulo          | Descrição                         | Instalação Windows          | Instalação Ubuntu Linux       |
| --------------- | --------------------------------- | --------------------------- | ----------------------------- |
| `customtkinter` | Interface gráfica moderna         | `pip install customtkinter` | `pip install customtkinter`   |
| `tkinter`       | Interface gráfica base (padrão)   | Incluído no Python          | `sudo apt install python3-tk` |
| `markdown`      | Conversor Markdown → HTML         | `pip install markdown`      | `pip install markdown`        |
| `os`            | Sistema de ficheiros e caminhos   | Já incluído                 | Já incluído                   |
| `filedialog`    | Abrir/guardar ficheiros (tkinter) | Incluído no `tkinter`       | Incluído em `python3-tk`      |
| `messagebox`    | Janelas de mensagem (tkinter)     | Incluído no `tkinter`       | Incluído em `python3-tk`      |

---

## 📄 1. `requirements.txt`

Este ficheiro define os módulos Python necessários:

```txt
customtkinter
markdown
```

---

## ⚙️ 2. Script Bash: `instalar_dependencias.sh`

Este script instala tudo automaticamente no **Ubuntu Linux**:

```bash
#!/bin/bash

echo "🔧 Atualizar o sistema..."
sudo apt update

echo "🧱 Instalar Python3 e pip3..."
sudo apt install -y python3 python3-pip

echo "🖼️ Instalar tkinter para GUI..."
sudo apt install -y python3-tk

echo "📦 Instalar dependências Python com pip..."
pip3 install -r requirements.txt

echo "✅ Instalação completa!"
```

---

## ✅ Como Usar

1. **Cria os ficheiros:**

   * Guarda o seguinte conteúdo como `requirements.txt`.
   * Guarda o script como `instalar_dependencias.sh`.

2. **Dá permissões de execução ao script:**

   ```bash
   chmod +x instalar_dependencias.sh
   ```

3. **Executa o script:**

   ```bash
   ./instalar_dependencias.sh
   ```

---
**ficheiro `.desktop`** para lançares o teu editor Markdown no Ubuntu com um **ícone no menu (tipo atalho de aplicação)**.

---

C**ficheiro `.desktop`** para lançares o teu editor Markdown no Ubuntu com um **ícone no menu (tipo atalho de aplicação)**.

---

## 🗂️ Estrutura do Projeto

Assumo que tens algo como:

```
/home/seu_utilizador/editor_markdown/
│
├── editor_markdown.py          ← o teu script principal
├── requirements.txt
├── instalar_dependencias.sh
├── icon.png                    ← ícone da aplicação (opcional)
```

---

## 📝 1. Ficheiro `.desktop`

Cria um ficheiro chamado, por exemplo:

```bash
~/.local/share/applications/editor_markdown.desktop
```

Com este conteúdo:

```desktop
[Desktop Entry]
Version=1.0
Type=Application
Name=Editor Markdown
Comment=Editor de texto com pré-visualização Markdown
Exec=python3 /home/seu_utilizador/editor_markdown/editor_markdown.py
Icon=/home/seu_utilizador/editor_markdown/icon.png
Terminal=false
Categories=Utility;TextEditor;
```

> 🔁 **Substitui** `/home/seu_utilizador/editor_markdown/` pelo caminho real no teu sistema.

---

## 📌 Explicação dos Campos

| Campo        | Função                                                                 |
| ------------ | ---------------------------------------------------------------------- |
| `Version`    | Versão da entrada `.desktop`.                                          |
| `Type`       | Tipo de entrada (`Application`).                                       |
| `Name`       | Nome que aparecerá no menu/aplicações.                                 |
| `Comment`    | Descrição da aplicação.                                                |
| `Exec`       | Comando para executar a aplicação (usa `python3` + caminho do script). |
| `Icon`       | Caminho para o ficheiro `.png` do ícone (opcional, mas recomendado).   |
| `Terminal`   | `false` para não abrir terminal ao iniciar.                            |
| `Categories` | Onde se encaixa no menu (ex: `Utility`, `TextEditor`, etc.).           |

---

## ✅ Passos Finais

1. **Torna o `.desktop` executável:**

   ```bash
   chmod +x ~/.local/share/applications/editor_markdown.desktop
   ```

2. **Atualiza o cache de ícones e entradas (opcional):**

   ```bash
   update-desktop-database ~/.local/share/applications
   ```

3. **Agora o teu editor aparece no menu do Ubuntu!** 🎉
   (Procura por "Editor Markdown" no menu.)

---

## 🖼️ Se não tiveres um ícone (`icon.png`)

Podes comentar a linha do ícone ou usar um ícone de sistema, por exemplo:

```desktop
Icon=accessories-text-editor
```



