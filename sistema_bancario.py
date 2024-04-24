def depositar(saldo, extrato, /):
    deposito = int(input("\nInsira o valor que deseja depositar: "))
    if deposito <= 0:
        print("\nImpossível depositar valores negativos ou nenhum valor, por favor insira um valor positivo para depositar na próxima!")
    else:
        saldo += deposito
        extrato += f"\nDEPÓSITO: R$ {deposito:.2f}"
        print("\nDepósito efetuado com sucesso!")
        return saldo, extrato

def sacar(*, saldo, limite_saque, extrato):
    if limite_saque == 0:
        print("\nNão há mais saques disponíveis, tente de novo outro dia!")
    else:
        saque = int(input("\nInsira o valor que deseja sacar: "))
        if saque <= 0:
            print("\nImpossível sacar valores negativos ou nenhum valor, por favor insira um valor positivo para sacar na próxima!")
        elif saque > 500:
            print("\nValor do saque maior do que o limite, por favor insira um valor de 1 até 500!")
        elif saque > saldo:
            print(f"""
Valor excede o valor do seu saldo em conta, que no momento é: R${saldo:.2f}
Insira um valor de saque condizente com a quantidade de seu saldo""")
        else:
            saldo -= saque
            limite_saque -= 1
            extrato += f"\nSAQUE: R${saque:.2f}"
            print("\nSaque efetuado com sucesso!")
            return saldo, limite_saque, extrato
        
def mostrar_extrato(saldo, /, *, extrato):
    print((extrato if extrato else "\nNão foram realizadas operações no momento.") + f"\n\nSALDO: R$ {saldo:.2f}")

def sair(decisao_sair):
    while decisao_sair != 1 and decisao_sair != 2:
            print("\nTem certeza que deseja sair?")
            decisao_sair = int(input("\nSelecione 1 para SIM ou 2 para NÃO: "))
            if decisao_sair == 1:
                print("\nEntão tá :( até outro dia!\n")
                return 1
            elif decisao_sair != 2:
                print("\nSelecione uma das opções para sua decisão!")
            else:
                print("\nObrigado por continuar conosco :D")
                return 0
            
def criar_usuario(usuarios):
    cpf = input("Digite seu CPF (somente números): ")
    for usuario in usuarios:
        if cpf == usuario["cpf"]:
            print("\nUsuário já existe em nosso banco!")
            return usuarios
    else:
        nome = input("Digite seu nome: ")
        data_nascimento = input("Digite sua data de nascimento (dd-mm-aaaa): ")
        endereco = input("Digite seu endereço (logradouro, número - bairro - cidade/sigla_estado): ")
        usuarios.append({"cpf": cpf, "nome": nome, "nascimento": data_nascimento, "endereço": endereco})
        print(f"\nUsuário cadastrado com sucesso, seja bem-vindo {nome}!")
        return usuarios

def criar_conta(*, contas, usuarios):
    cpf = input("Digite seu CPF (somente números): ")
    for usuario in usuarios:
        if cpf == usuario["cpf"]:
            contas.append({"conta" : len(contas) + 1, "Agência" : "0001", "Conta_dono" : usuario["nome"]})
            print("\nConta criada com sucesso!")
            return contas
    print("\nNão foi encontrado usuário com este CPF, insira um CPF existente entre nossos usuários!!")
    return contas

        
saldo = 0
limite_saque = 3
extrato = """"""
decisao_sair = 0
usuarios = []
contas = []
while decisao_sair != 1:
    print("""
        Bem-vindo ao nosso banco!!
        O que deseja fazer hoje?
          
        1 - Depositar
        2 - Sacar
        3 - Ver extrato
        4 - Criar usuário
        5 - Criar conta corrente
        6 - Sair
    """)
    opcao = int(input())
    if opcao == 1:
        saldo, extrato = depositar(saldo, extrato)
    elif opcao == 2:
        saldo, limite_saque, extrato = sacar(saldo = saldo, limite_saque = limite_saque, extrato = extrato)
    elif opcao == 3:
        mostrar_extrato(saldo, extrato = extrato)
    elif opcao == 4:
        usuarios = criar_usuario(usuarios)
    elif opcao == 5:
        contas = criar_conta(contas = contas, usuarios = usuarios)
    elif opcao == 6:
        decisao_sair = sair(decisao_sair)
    else:
        print("\nSelecione uma das opções do menu para prosseguir com sua ação!")