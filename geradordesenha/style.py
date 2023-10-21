# Importa as bibliotecas tkinter para criar a interface gráfica e o módulo "gerador" que contém a lógica de geração de senhas.
import tkinter as tk
import gerador

# Define uma função chamada "gerar" que gera senhas e as exibe em um widget de texto.
def gerar(text_widget):
    # Gera uma senha chamando a função "gerasenha" do módulo "gerador".
    senha = gerador.gerasenha()
    # Insere a senha no final do widget de texto, seguida por dois espaços para separar as senhas.
    text_widget.insert("end", senha + "  ")

# Define uma função chamada "limpar" que remove todo o conteúdo de um widget de texto.
def limpar(text_widget):
    # Deleta todo o conteúdo do widget de texto.
    text_widget.delete("1.0", "end")

# Define uma função chamada "excluir" para remover a senha mais antiga do widget de texto.
def excluir(text_widget):
    # Obtém o conteúdo atual do widget de texto.
    content = text_widget.get("1.0", "end-1c")
    # Divide o conteúdo em senhas individuais com base em dois espaços ("  ").
    lines = content.split("  ")
    # Verifica se há mais de uma senha.
    if len(lines) > 1:
        # Se houver, cria um novo conteúdo sem a senha mais antiga.
        new_content = "  ".join(lines[1:])
        # Limpa o conteúdo atual do widget de texto.
        text_widget.delete("1.0", "end")
        # Insere o novo conteúdo no final do widget de texto.
        text_widget.insert("end", new_content)


# Define uma função para criar uma nova janela de interface gráfica.
def new_window():
    # Cria uma nova janela principal.
    root = tk.Tk()
    # Define o título da janela.
    root.title("Gerador de senhas")

    # Configura as dimensões da janela.
    largura = 300
    altura = 200
    root.geometry(f"{largura}x{altura}")

    # Cria um frame na janela para organizar os elementos.
    frame = tk.Frame(root)
    frame.pack(pady=30) # Adiciona um espaço entre o conteúdo e as bordas da janela.

    # Adiciona um título à janela.
    titulo = tk.Label(frame, text="Gerador de Senhas", font=("Helvetica", 16))
    titulo.grid(row=0, column=0, columnspan=3)

    # Cria um widget de texto para exibir as senhas geradas.
    senha_text = tk.Text(frame, wrap=tk.WORD, height=3, width=19, font=("Helvetica", 12))
    senha_text.grid(row=1, column=0, columnspan=3)

    # Cria um botão "Gerar senha" associado à função "gerar".
    bt_gerasenha = tk.Button(frame, text="Gerar senha", command=lambda: gerar(senha_text), font=("Helvetica", 8, "bold"), bg="green", fg="white")
    bt_gerasenha.grid(pady= 7, row=2, column=0)
    
    # Cria um botão "Excluir" associado à função "excluir".
    bt_excluir = tk.Button(frame, text="Excluir", command=lambda: excluir(senha_text), font=("Helvetica", 8, "bold"), bg="darkorange", fg="white")
    bt_excluir.grid(row=2, column=1)

    # Cria um botão "Limpar" associado à função "limpar".
    bt_limpar = tk.Button(frame, text="Limpar", command=lambda: limpar(senha_text), font=("Helvetica", 8, "bold"), bg="red", fg="white")
    bt_limpar.grid(row=2, column=2)

    # Inicia a aplicação e exibe a janela principal.
    root.mainloop()