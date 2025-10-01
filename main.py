from autenticacao import autenticar_usuario, obter_usuarios_cadastrados

def main():
    usuarios = obter_usuarios_cadastrados()
    
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    
    if autenticar_usuario(usuario, senha, usuarios):
        print("Autenticação bem-sucedida!")
        print(f"Bem-vindo(a), {usuario}!")
    else:
        print("Usuário ou senha incorretos.")

if __name__ == "__main__":
    main()
