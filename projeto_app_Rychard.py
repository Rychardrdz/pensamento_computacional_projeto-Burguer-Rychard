'''
CRUD - Sistema de Hamburgueria

Este sistema simula um atendimento simples de uma hamburgueria.
O cliente pode se cadastrar, ver o cardápio, adicionar itens no carrinho
e finalizar um pedido.

Autor: Rychard
'''


# Loop principal do sistema
# Ele mantém o programa rodando até o usuário escolher sair
while True:

    print("\n== Sistema da Hamburgueria ===")
    print("1. Cadastro")        # Criar conta do cliente
    print("2. Esqueceu a senha")# Recuperação de senha
    print("3. Menu")            # Mostrar cardápio
    print("4. Carrinho")        # Mostrar pedidos adicionados
    print("5. Opções")          # Retirar ingredientes (simulação)
    print("6. Finalizar pedido")# Inserir endereço e pagamento
    print("7. Cupom")           # Mostrar desconto acumulado
    print("8. Chat da loja")    # Sugestões para a loja
    print("9. Feedback")        # Avaliação do cliente
    print("0. Sair")            # Encerrar o sistema


    escolha = input("\nEscolha uma opção: ")


# ==============================
# 1 - CADASTRO DE CLIENTE
# ==============================
    if escolha == '1':

        print("\n--- Novo Cadastro ---")

        # Dados solicitados ao cliente
        nome = input("Nome: ")
        email = input("Email: ")
        telefone = input("Telefone: ")
        cpf = input("CPF: ")
        senha = input("Senha: ")
        
        input(f"Seja bem vindo(a) {nome}")

        # Criando um dicionário com os dados do cliente
        cliente = {
            "nome": nome,
            "email": email,
            "telefone": telefone,
            "cpf": cpf,
            "senha": senha
        }

        # Salvando o cliente na lista de clientes
        cliente.append(cliente)

        print("Cadastro realizado com sucesso!")


# ==============================
# 2 - RECUPERAÇÃO DE SENHA
# ==============================
    elif escolha == '2':

        print("\n--- Recuperação de senha ---")

        email = input("Digite seu email cadastrado: ")

        codigo = print("Um código de recuperação foi enviado para seu email...")
        
        digite = input("Digite o código: ")


# ==============================
# 3 - MENU / CARDÁPIO
# ==============================
    elif escolha == '3':

        # Loop interno do cardápio
        while True:

            print("\n--- Menu ---")
            print("1. Lanches")
            print("2. Combos")
            print("3. Bebidas")
            print("4. Voltar")

            sub_escolha = input("Escolha uma opção do menu: ")


# ------------------------------
# Lanches
# ------------------------------
            if sub_escolha == '1':

                print("\nLanches disponíveis:")
                print("1 - X-Burguer - 15,00R$")
                print("2 - X-Salada - 18,00R$")
                print("3 - X-Bacon - 20,00R$")

                item = input("Escolha um lanche para adicionar ao carrinho: ")

                if item == '1':
                    carrinho.append("X-Burguer")
                elif item == '2':
                    carrinho.append("X-Salada")
                elif item == '3':
                    carrinho.append("X-Bacon")

                print("Item adicionado ao carrinho!")


# ------------------------------
# Combos
# ------------------------------
            elif sub_escolha == '2':

                print("\nCombos disponíveis:")
                print("1 - Combo Família - 45,00R$")
                print("2 - Combo Duplo - 30,00R$")
                print("3 - Combo Kid - 20,00R$")

                item = input("Escolha um combo: ")

                if item == '1':
                    carrinho.append("Combo Família")
                elif item == '2':
                    carrinho.append("Combo Duplo")
                elif item == '3':
                    carrinho.append("Combo Kid")

                print("Combo adicionado ao carrinho!")


# ------------------------------
# Bebidas
# ------------------------------
            elif sub_escolha == '3':

                print("\nBebidas disponíveis:")
                print("1 - Refrigerante - 5,00R$")
                print("2 - Suco - 7,00R$")
                print("3 - Água - 3,00R$")

                item = input("Escolha uma bebida: ")

                if item == '1':
                    carrinho.append("Refrigerante")
                elif item == '2':
                    carrinho.append("Suco")
                elif item == '3':
                    carrinho.append("Água")

                print("Bebida adicionada ao carrinho!")


# ------------------------------
# Voltar ao menu principal
# ------------------------------
            elif sub_escolha == '4':

                print("Voltando ao menu principal...")
                break

            else:
                print("Opção inválida.")


# ==============================
# 4 - CARRINHO
# ==============================
    elif escolha == '4':

        print("\n--- Seu Carrinho ---")
        carrinho = []

# ==============================
# 5 - REMOVER INGREDIENTES
# ==============================
    elif escolha == '5':

        print("\nOpção de remover ingredientes")
        print("Exemplo: tirar cebola, tomate ou molho...")
        print("0 - Voltar para tela inicial")
        remover = input("Oque deseja remover do lanche: ")
        print("Removido!")
    
    if escolha == '0':
        break

# ==============================
# 6 - FINALIZAR PEDIDO
# ==============================
    elif escolha == '6':

        print("\n--- Finalizar Pedido ---")

        cep = input("CEP: ")
        endereco = input("Endereço: ")
        numero = input("Número da casa: ")
        referencia = input("Ponto de referência: ")
        pagamento = input("Forma de pagamento: ")

        print("\nPedido finalizado com sucesso!")
        print("Seu pedido chegará em breve.")
        
        print("1 - Sim")
        print("2 - Não")
        input("Deseja salvar as informações para a proxima compra?")
        print("Deseja salvar as informações para a proxima compra?")
        
        if escolha == '1':
            print("Informações salva para a proxima compra.")
        
        elif escolha == '2':
            print("Informações não salva.")



# ==============================
# 7 - CUPOM
# ==============================
    elif escolha == '7':

        print("\nCupom disponível:")
        print("A cada compra você acumula 5% de desconto para o próximo pedido.")


# ==============================
# 8 - CHAT DA LOJA
# ==============================
    elif escolha == '8':

        sugestao = input("\nDigite sua sugestão para a loja: ")
        print("Obrigado pela sugestão!")


# ==============================
# 9 - FEEDBACK
# ==============================
    elif escolha == '9':

        nota = input("\nAvalie nossa loja de 0 a 5: ")
        print("Obrigado pela avaliação!")


# ==============================
# 0 - SAIR
# ==============================
    elif escolha == '0':

        print("Saindo do sistema. Até logo!")
        break


# ==============================
# OPÇÃO INVÁLIDA
# ==============================
    else:
        print("Opção inválida. Tente novamente.")