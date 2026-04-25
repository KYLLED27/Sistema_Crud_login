from uteis import carregar_usuarios, carregar_adms, salvar_usuarios, salvar_adms
from crud import cadastrar_usuario, cadastrar_adm, logar, listar_usuarios, listar_adms, excluir

usuarios = carregar_usuarios()
adms = carregar_adms()

# LOOP  - Permite voltar ao login
while True:
    administrador = logar(usuarios, adms)

    # MENU DO ADMINISTRADOR
    if administrador is True:
        while True:
        
            print("\n--- MENU DO ADMINISTRADOR ---")
            print("1 - Cadastrar Usuário")
            print("2 - Cadastrar Administrador")
            print("3 - Excluir Usuário/Administrador")
            print("4 - Listar Usuários")
            print("5 - Listar Administradores")
            print("6 - Sair")
            escolha = input("Escolha uma opção: ")
            
            if escolha == "1":
                cadastrar_usuario(usuarios)
                salvar_usuarios(usuarios) 

            elif escolha == "2":
                cadastrar_adm(adms)
                salvar_adms(adms)

            elif escolha == "3":
                excluir(usuarios, adms, administrador)
                salvar_usuarios(usuarios)
                salvar_adms(adms) 

            elif escolha == "4":
                listar_usuarios(usuarios)
            
            elif escolha == "5":
                listar_adms(adms)
                
            elif escolha == "6":
                print("Voltando ao login...")
                break  # Sai do menu
            else:
                print("Opção inválida, tente novamente.")

    # MENU DO USUÁRIO COMUM
    else:
        while True:
        
            print("\n--- MENU DO USUÁRIO ---")
            print("1 - EM BREVE: Acessar Área do Usuário")
            print("2 - Sair")
            
            escolha = input("Escolha uma opção: ")
            
            if escolha == "1":
                listar_usuarios(usuarios)
            
            elif escolha == "2":
                print("Voltando ao login...")
                break  
            else:
                print("Opção inválida, tente novamente.")