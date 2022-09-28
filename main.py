menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = int(input(menu))
    valor_deposito =0
    valor_saque = 0

    if opcao == 1:
        valor_deposito = float(input("Informe o valor de depósito: "))
        if valor_deposito > 0:
         saldo += valor_deposito
         print("Depósito realizado com sucesso")
         extrato += f"Depósito............R$ {valor_deposito:.2f}\n"
        else:
            print("""
                Valor inválido
            Operação não realizada""")
    elif opcao == 2:
        valor_saque = float(input("Informe o valor a sacar: "))
        if(valor_saque < 0):
            print("""
            Valor inválido
            Operação não realizada""")
        elif(numero_saques < LIMITE_SAQUES):
            if ((saldo - valor_saque) > 0):
                if (valor_saque <= 500):
                    saldo -= valor_saque
                    print("Saque realizado com sucesso")
                    extrato += f"Saque...............R$ {valor_saque:.2f}\n"
                    numero_saques += 1
                else:
                    print("""
                    Valor superior ao limite
                     Operação não realizada""")
            else:
                print("Saldo insuficiente")
        else:
            print("Limite de saques diário atingido")
    elif opcao == 3:
       print("Extrato".center(31))
       print("="*31)
       print("Não foram realizadas transações" if not extrato else extrato)
       print(f"Saldo...............R$ {saldo:.2f}\n")
    elif opcao == 4:
        break
    else:
        print("""
                     Operação inválida
            Selecione novamente a operação desejada.""")