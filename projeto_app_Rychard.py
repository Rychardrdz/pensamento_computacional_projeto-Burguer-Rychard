'''
CRUD

    Hamburgueria

Este sistema irá  criar um menu para a Hamburgueria
Rychard
Rychard
'''
while True:

    print("\n== Sistema da Hamburgueria ===")
    print("1. Cadastro") #Para o cliete criar a conta, irá precisar colocar o, Email, Numero de telefone, CPF
    print("2. Esqueceu a senha") #Enviar um codigo de 6 digitos para o email cadastrado, Criar nova senha
    print("3. Menu") #Combos e opções
    print("4. Carrinho") #Adicionar os combos ou opções no carrinho
    print("5. Opções") #Retirar algum ingrediente
    print("6. Finalizar pedido") # O cliente precisará colocar o, CEP, Endereço, Numero da casa, Ponto de referencia, Forma de pagamento para calcular a entrega
    print("7. Cupom") #Cada compra, o cliente ira acumular 5% para a o proximo pedido que o cliente fizer
    print("8. Chat da loja") #Pontos que podem ser melhorados na loja
    print("9. Feedback") #O cliente dar uma avaliação de 0-5 para a loja
    print("0. Sair") #Sair do atendimento


    escolha = input("\nEscolha uma opção:")

    if escolha == '1':
        print("\n--- Novo Cadastro ---")
        nome = input("Nome: ")
        email = input("Email: ")
        telefone = input("Telefone: ")
        cpf = input("CPF: ")
        senha = input("Senha: ")
        
        cliente = {
            "nome": nome,
            "email": email,
            "telefone": telefone,
            "cpf": cpf,
            "senha": senha
        }


    elif escolha == '2':
        print("Esqueceu a senha")
    
    elif escolha == '3':
        while True:
            print("\n--- Menu ---")
            print("1. Lanches ")
            print("2. Combos  ")
            print("3. Bebidas ")
            
            sub_escolha = input("Escolha uma opção do menu: ")
        
            
            if sub_escolha == '1':
                print("Lanches disponiveis")
                print("- X-Burguer - 15,00R$ ")
                print("- X-Salada 18,00R$")
                print("- X-Bacon 20,00R$")

            elif sub_escolha == '2':
                print("Combos disponiveis")
                print("- Combo Familia - 45,00R$ ")
                print("- Combo Duplo 30,00R$")
                print("- Combo Kid 20,00R$")
            
            elif sub_escolha == '3':
                print("Bebidas Disponiveis")
                print("- Refrigerante - 5,00R$ ")
                print("- Suco 7,00R$")
                print("- Agua 3,00R$")
            
            elif sub_escolha == '4':
                print("Voltando ao menu principal...")
                break

            else:
                print("Opção invalida. Tente Novamente")

    
    elif escolha == '4':
        print("Aqui fica registrado os pedido")


    elif escolha == '5':
        print("Retirar algo")


    elif escolha == '6':
        print("Finalizar pedido")


    elif escolha == '7':
        print("Nossos cupons!") 


    elif escolha == '8':
        print("Entre em contato")


    elif escolha == '9':
        print("Nos diga oque achou")



    elif escolha == '0':
        print("Saindo do sistema. Até logo")
        break



else:
    print("Opção inválida, Por favor, Tente novamente")    