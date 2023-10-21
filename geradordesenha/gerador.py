import random, string

# Define uma função chamada "geraasenha" que é responsável pela lógica da geração de senhas do sistema
def gerasenha():
    # Gera 2 letras maiúsculas aleatórias e armazena em uma lista
    letras = [random.choice(string.ascii_uppercase) for x in range(0, 2)]

    # Gera 3 números inteiros aleatórios entre 0 e 9 e armazena em outra lista
    numeros = [random.randint(0,9) for x in range(0, 3)]

    # Combina as duas listas (letras e números) para formar a senha
    senha = letras + numeros

    # Converte os elementos da lista senha em strings e una-os em uma única string
    return "".join(map(str,senha))