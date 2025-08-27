#Aqui é um projeto simples de sistema de depósito, saque e extrato bancário Inicial. O projeto ainda está em construção!

menu = """
########### Sistema V_bank ################

-> Escolha uma das opções abaixo:
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
#Variáveis iniciais para utilizar
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

#Sessão de Depósito
while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! o valor informado é inválido.")
#Sessão de Saque, levando em consideração 3 verificações como o limite referente ao valor que é possivel sacar, assim como a quantidade de vezes que é
#possivel utilizar o serviço no dia. Nesse caso limitamos os valores em 500 reais de limite e sendo possivel realizar operação de saque 3 vezes por dio
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

#Nesses blocos foram colocadas as formas de que se caso se tenha excedentes, será notficado a falha
        if excedeu_saldo:
            print("Operação falhou! você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! o valor do saque excede o limite.")
        
        elif excedeu_saques:
            print("Operação falhou! Número maximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saques: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! o valor informado é inválido.")


#Sessão Extrato
    elif opcao == "e":
        print("\n###################### EXTRATO #######################")
        print("Não foram realizados movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("########################################################")

#Sessão de saida e finalização do programa
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")