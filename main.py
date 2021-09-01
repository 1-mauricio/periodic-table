import pandas as pd

tabela = pd.read_excel("data\periodic_table.xlsx")
reatividade = pd.read_excel(r'data\\reactivity_series.xlsx')

fim = False
while not fim:
    print("\n----------------------------------------------------")
    print("------------------------MENU------------------------")
    print("1 - Tabela Periodica")
    print("2 - Reatividade")
    print("----------------------------------------------------")
    print("----------------------------------------------------")
    res = int(input(": "))
    while res>2 or res<0:
        print("A entrada não condiz com uma opção. Tente novamente")
        res = int(input(": "))

    if res == 1:
        print("\n----------------------------------------------------")
        print("{:^50}".format("TABELA PERIODICA"))
        print("----------------------------------------------------")
        i = int(input("\nDigite o número atômico do elemento procurado (0 para parar): "))
        if i>118 or i<0:
            print("\nSó existem 118 elementos, então digite um número positivo entre 1 e 118.")
            i = int(input("Digite o número atômico do elemento procurado (0 para parar): "))
        while i != 0:
            i -= 1

            numero = tabela["number"][i]
            nome = tabela["name"][i]
            simbolo = tabela["symbol"][i]
            aparencia = tabela["appearance"][i]
            grupo = tabela["group_block"][i]
            periodo = tabela["period"][i]
            categoria = tabela["element_category"][i]
            peso_ato = tabela["atomic_weight"][i]
            config_ele = tabela["electron_configuration"][i]
            fase = tabela["phase"][i]

            print("\n==========================================")
            print(f"ELEMENTO: {nome} - [{simbolo}]")
            print(f"NÚMERO ATÔMICO: {numero}")
            print(f"CONFIGURAÇÃO ELETRÔNICA: {config_ele}")
            print(f"PERÍODO: {periodo}")
            print(f"CATEGORIA: {categoria}")
            print(f"FASE: {fase}")
            print(f"PESO ATÔMICO: {peso_ato}")
            print(f"GRUPO: {grupo}")
            print(f"APARÊNCIA: {aparencia}")
            print("==========================================")
        
            i = int(input("\nDigite o número atômico do elemento procurado (0 para parar): "))
            if i>118 or i<0:
                print("\nSó existem 118 elementos, então digite um número positivo entre 1 e 118.")
                i = int(input("Digite o número atômico do elemento procurado (0 para parar): "))

    if res == 2:
        print("\n----------------------------------------------------")
        print("{:^50}".format("REATIVIDADE"))
        print("----------------------------------------------------")
        sym = input("\nDigite o simbolo(0 para parar): ").capitalize()
        while sym != "0":
            aux = 0

            for i in range(len(reatividade)):
                if sym == reatividade['symbol'][i]:
                    nome = reatividade['name'][i]
                    ion = reatividade['ion'][i]
                    print(f"O simbolo {sym} corresponde ao elemento {nome} e tem {ion} ion(s)")
                    aux += 1
            
            if aux == 0:
                print("Nenhum elemento foi encontrado. ")

            sym = input("\nDigite o simbolo(0 para parar): ").capitalize()



    cont = input("\nContinuar(S/N): ")
    while cont != "S" and cont != "N":
        cont = input("\nContinuar(S/N): ")
    if cont == "N":
        fim = True






    
    