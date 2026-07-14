# ESTE PROGRAMA LERÁ OS DADOS CADASTRADOS, E SE FOR VERDADEIRO LIBERARA O ACESSO
# CASO CONTRÁRIO ELE CADASTRARA UM NOVO USUARIO E SENHA

import csv

def leitor_arquivo(seila):
    with open(seila) as dados:
        return list(csv.DictReader(dados))
        
def verificar_login(usuario, senha):
    for item in leitor_arquivo("dados.csv"):
        if usuario == item['usuario'] and senha == item['senha']:
            print("Acesso permitido")
            return True
    print("Acesso negado")
    resposta = input("Deseja cadastrar um novo usuário? (s/n): ")
    if resposta == "s":
        cadastrar_usuario(usuario, senha)
        inputs()
        verificar_login(codificar_usuario(input_usuario), codificar_senha(input_senha))
    return False

def cadastrar_usuario(usuario, senha):
    with open("dados.csv", "a", newline='') as dados:
        writer = csv.writer(dados)
        writer.writerow([usuario, senha])
    print("Usuário cadastrado com sucesso!")

def inputs():
    global input_usuario, input_senha
    input_usuario = input("Digite o usuário: ")
    input_senha = input("Digite a senha: ")

def codificar_usuario(usuario):
    resultado = ""
    for letra in usuario:
        if letra.isalpha():
            base = 97 if letra.islower() else 65
            letra_codificada = chr((ord(letra) - base + 10) % 26 + base)
            resultado += letra_codificada
        else:
            resultado += letra
    return resultado

def codificar_senha(senha):
    resultado = ""
    for numero in senha:
        if numero.isdigit():
            numero_codificado = str((int(numero) + 3) % 10)
            resultado += numero_codificado
        else:
            resultado += numero
    return resultado

inputs()
verificar_login(codificar_usuario(input_usuario), codificar_senha(input_senha))
    


    