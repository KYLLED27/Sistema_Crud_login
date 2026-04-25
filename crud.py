
def cadastrar_usuario(usuarios):
    print("=== Cadastro de Usuário ===")
    while True:
        nome = input("Digite o nome do usuário: ")
        if len(nome) < 3:
            print("O nome deve conter pelo menos 3 caracteres. Por favor, tente novamente.")
        else:
            break

    while True:
        email = input("Digite o email do usuário: ")
        if "@" not in email or "." not in email:
            print("Email inválido. Por favor, tente novamente.")
        elif email in [usuario["email"] for usuario in usuarios]:
            print("Este email já está cadastrado. Por favor, tente novamente.")
        else:
            break

    while True:
        senha = input("Digite a senha do usuário: ")
        if len(senha) < 6:
            print("A senha deve conter pelo menos 6 caracteres. Por favor, tente novamente.")
        else:
            break

    usuario = {
        "nome": nome,
        "email": email,
        "senha": senha
    }
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")    
def cadastrar_adm(adms):
    print("=== Cadastro de Administrador ===")
    while True:
        nome = input("Digite o nome do usuário: ")
        if len(nome) < 3:
            print("O nome deve conter pelo menos 3 caracteres. Por favor, tente novamente.")
        else:
            break

    while True:
        email = input("Digite o email do usuário: ")
        if "@" not in email or "." not in email:
            print("Email inválido. Por favor, tente novamente.")
        elif email in [adm["email"] for adm in adms]:
            print("Este email já está cadastrado. Por favor, tente novamente.")
        else:
            break

    while True:
        senha = input("Digite a senha do ADM: ")
        if len(senha) < 6:
            print("A senha deve conter pelo menos 6 caracteres. Por favor, tente novamente.")
        else:
            break

    adm = {
        "nome": nome,
        "email": email,
        "senha": senha
    }
    adms.append(adm)
    print("Administrador cadastrado com sucesso!")


def listar_usuarios(usuarios):
    print("=== Lista de Usuários ===")
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        for idx, usuario in enumerate(usuarios, start=1):
            print(f"{idx}. Nome: {usuario['nome']}, Email: {usuario['email']}")

def listar_adms(adms):
    print("=== Lista de Administradores ===")
    if not adms:
        print("Nenhum administrador cadastrado.")
    else:
        for idx, adm in enumerate(adms, start=1):
            print(f"{idx}. Nome: {adm['nome']}, Email: {adm['email']}")

def logar(usuarios, adms):
    while True:
        print("=== Login ===")
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")
        
        # Verifica se é usuário
        for usuario in usuarios:
            if usuario["email"] == email and usuario["senha"] == senha:
                print(f"Login bem-sucedido! Bem-vindo, {usuario['nome']}!")
                return False  # Não é admin
        
        # Verifica se é administrador
        for adm in adms:
            if adm["email"] == email and adm["senha"] == senha:
                print("Login bem-sucedido! Bem-vindo, administrador!")
                return True  # É admin
        
        # Se não encontrou
        print("Email ou senha incorretos. Por favor, tente novamente.")

def excluir(usuarios, adms, administrador):
    if not usuarios and not adms:
        print("Nenhum usuário ou administrador cadastrado para excluir.")
        return
    if not administrador:
        print("Apenas administradores podem excluir usuários.")
        return
    escolha = input("Deseja excluir um usuário ou um administrador? (u/a): ").lower()
    if escolha == "u":
        print("=== Excluir Usuário ===")
        email = input("Digite o email do usuário a ser excluído: ")
        for usuario in usuarios:
            if usuario["email"] == email:
                usuarios.remove(usuario)
                print("Usuário excluído com sucesso!")
                return
        print("Usuário não encontrado.")
    elif escolha == "a":
        print("=== Excluir Administrador ===")   
        email = input("Digite o email do adm a ser excluído: ")
        for adm in adms:
            if adm["email"] == email:
                adms.remove(adm)
                print("Administrador excluído com sucesso!")
                return
        print("Administrador não encontrado.")


