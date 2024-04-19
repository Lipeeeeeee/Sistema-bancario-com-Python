saldo = 0
limite_saque = 3
extrato = """"""
decisao_sair = 0
while decisao_sair != 1:
    decisao_sair = 0
    print("""
        Bem-vindo ao nosso banco!!
        O que deseja fazer hoje?
          
        1 - Depositar
        2 - Sacar
        3 - Ver extrato
        4 - Sair
    """)
    opcao = int(input())
    if opcao == 1:
        deposito = int(input("\nInsira o valor que deseja depositar: "))
        if deposito <= 0:
            print("\nImpossível depositar valores negativos ou nenhum valor, por favor insira um valor positivo para depositar na próxima!")
        else:
            saldo += deposito
            extrato += f"\nDEPÓSITO: R$ {deposito:.2f}"
            print("\nDepósito efetuado com sucesso!")
    elif opcao == 2:
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
    elif opcao == 3:
        print((extrato if extrato else "\nNão foram realizadas operações no momento.") + f"\n\nSALDO: R$ {saldo:.2f}")
    elif opcao == 4:
        while decisao_sair != 1 and decisao_sair != 2:
            print("\nTem certeza que deseja sair?")
            decisao_sair = int(input("\nSelecione 1 para SIM ou 2 para NÃO: "))
            if decisao_sair == 1:
                print("\nEntão tá :( até outro dia!\n")
                break
            elif decisao_sair != 2:
                print("\nSelecione uma das opções para sua decisão!")
            else:
                print("\nObrigado por continuar conosco :D")