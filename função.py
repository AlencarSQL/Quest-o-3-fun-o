def autenticar_usuario(usuario, senha, usuarios):
    if usuarios.get(usuario) == senha:
        return True
    else:
        return False


def obter_usuarios_cadastrados():
      usuarios = {
        "admin": "1234",
        "joao": "senha123",
        "maria": "abc@2024"
    }
    return usuarios
