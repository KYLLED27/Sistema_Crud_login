import json

def carregar_usuarios():
    try:
        with open("usuarios.json", "r") as arquivo:
            conteudo = arquivo.read()
            if not conteudo:  # Se arquivo está vazio
                return []
            return json.loads(conteudo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def carregar_adms():
    try:
        with open("adms.json", "r") as arquivo:
            conteudo = arquivo.read()
            if not conteudo:  # Se arquivo está vazio
                return []
            return json.loads(conteudo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def salvar_usuarios(usuarios):
    with open("usuarios.json", "w") as arquivo:
        json.dump(usuarios, arquivo, indent=4)

def salvar_adms(adms):
    with open("adms.json", "w") as arquivo:
        json.dump(adms, arquivo, indent=4)
    