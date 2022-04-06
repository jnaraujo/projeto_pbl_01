""" /*******************************************************************************

    Autor: Jônatas Araújo Silva Santos
    Componente Curricular: Algoritmos I
    Concluido em: 06/04/2022
    Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
    trecho de código de outro colega ou de outro autor, tais como provindos de livros e
    apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código de
    outra autoria que não a minha está destacado com uma citação para o autor e a fonte do
    código, e estou ciente que estes trechos não serão considerados para fins de avaliação.

******************************************************************************************/ """

########## LIBS ##########

import os


########## CONSTANTES ##########

# Quantidades de itens necessários minimos em cada cesta básica
ACUCAR_QNT_POR_CESTA = 1  # KG
ARROZ_QNT_POR_CESTA = 4  # KG
CAFE_QNT_POR_CESTA = 2  # KG
EXTRATO_DE_TOMATE_QNT_POR_CESTA = 2  # UNIDADE
MACARRAO_QNT_POR_CESTA = 3  # UNIDADE
PCT_BOLACHA_QNT_POR_CESTA = 1  # UNIDADE
OLEO_QNT_POR_CESTA = 1  # LITRO
FARINHA_DE_TRIGO_QNT_POR_CESTA = 1  # KG
FEIJAO_QNT_POR_CESTA = 4  # KG
SAL_QNT_POR_CESTA = 1  # KG


########## VARIÁVEIS ##########

# Quantidades de itens doados por tipo
qnt_acucar = 0
qnt_arroz = 0
qnt_cafe = 0
qnt_extrato_de_tomate = 0
qnt_macarrao = 0
qnt_pct_bolacha = 0
qnt_oleo = 0
qnt_farinha_de_trigo = 0
qnt_feijao = 0
qnt_sal = 0
qnt_outros = 0

# Quantidades de itens que sobraram após a montagem das cestas básicas
sobra_acucar = 0
sobra_arroz = 0
sobra_cafe = 0
sobra_extrato_de_tomate = 0
sobra_macarrao = 0
sobra_pct_bolacha = 0
sobra_oleo = 0
sobra_farinha_de_trigo = 0
sobra_feijao = 0
sobra_sal = 0
sobra_outros = 0

# SOBRE A CESTA
quantidade_de_cestas=0 # Quantas cestas serão montadas
quantidade_de_cestas_com_item_extra=0 # Quantas cestas receberam itens extras
quantidade_de_cestas_sem_item_extra=0 # Quantas cestas NÃO receberam itens extras

# Quantidades por tipo de pessoa (física ou juridica)
qnt_de_doacoes_por_pessoa_fisica = 0
qnt_de_doacoes_por_pessoa_juridica = 0

# Variáveis para controle de funcionamento
deve_continuar = True
mostrar_relatorio = True

########## FUNÇÕES ##########

# Função que limpa a tela do terminal
def clear():
    os.system("clear")

# Recebe do usuário um input do tipo int e verifica se o valor informado está dentre os limites pra estabelecidos
# Se estiver, o valor é retornado.
# Se não, uma mensagem de erro é exibido e o usuário é novamente pedido para informar o valor correto
def ler_e_validar_input_de_numeros(v_min, v_max, mensagem, mensagem_erro):
    # v_min é o menor valor válido que o usuário pode digitar
    # v_max é o maior valor válido que o usuário pode digitar
    # mensagem é a mensagem que será exibida para o usuário para pedir a entrada
    # mensagem_erro é a mensagem que será exibida caso o usuário digite um valor inválido
    try:
        entrada = int(input(mensagem))
        while entrada < v_min or entrada > v_max:
            entrada = int(input(mensagem_erro))
        return entrada
    except:
        print("Valor inválido.")
        return ler_e_validar_input_de_numeros(v_min, v_max, mensagem, mensagem_erro)

'''
    Recebe do usuário um input do tipo int e verifica se o valor informado é valido
    Se positivo, o valor é retornado.
    Se negativo, uma mensagem de erro é exibido e o usuário é novamente pedido para informar o valor correto
'''
def ler_e_validar_item(mensagem):
    # mensagem é a mensagem que será exibida para o usuário para pedir a entrada
    try:
        entrada = int(input(mensagem))

        # Verifica se o valor é nagativo
        if entrada < 0:
            print("O valor informado não pode ser negativo.")
            return ler_e_validar_item(mensagem)

        return entrada
    except:
        # Verifica se o usuário tentou digitar um valor invalido, como uma string
        print("Valor inválido.")
        return ler_e_validar_item(mensagem)

# Recebe do usuário o tipo de doador e verifica se o dado é valido
# Se positivo, o valor é retornado.
# Se negativo, uma mensagem de erro é exibido e o usuário é novamente pedido para informar o valor correto
def ler_e_validar_tipo_do_doador(mensagem):
    # mensagem é a mensagem que será exibida para o usuário para pedir a entrada

    entrada = input(mensagem).lower() # pede a entrada e converte para minusculo

    # verifica se o tipo de doador é valido
    if entrada == "fisica" or entrada == "juridica":
        return entrada
    else:
        print("Valor informado é inválido.")
        return ler_e_validar_tipo_do_doador(mensagem)


########## PARTE VISUAL DO PROJETO ##########

clear() # limpa a tela do terminal

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print(" Olá, usuário!")
print(" Seja bem-vindo(a) ao")
print(" Sistema de Registro de Doações do Dispensário Santana ( SRDDS )")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

print("Escolha o que você deseja fazer:")
print("[0] Adicionar doação")
print("[1] Ir para o relatório")
print("[2] Sair")

opcao_inicial = ler_e_validar_input_de_numeros(0, 2, "Sua Opção: ", "Digite um número entre 0 (zero) e 2 (dois): ") # recebe e valida a opção do usuário

if opcao_inicial == 0: # se a opção for 0, o usuário irá adicionar uma doação
    deve_continuar = True
elif opcao_inicial == 1: # se a opção for 1, o usuário irá para o relatório
    deve_continuar = False
else: # se a opção for 2, o usuário irá sair do programa
    deve_continuar = False
    mostrar_relatorio = False

while deve_continuar: # enquanto o usuário não sair do programa
    clear() # limpa a tela do terminal
    print("\n=-=-=-=-=-=-=-= Sobre o doador =-=-=-=-=-=-=-=")

    # Recebe os dados sobre o doador
    nome = str(input("Qual o nome do doador? ")).upper() # nome do doador
    tipo_do_doador = ler_e_validar_tipo_do_doador("Qual o tipo de pessoa? (fisica ou juridica) ") # recebe e valida o tipo de doador ( fisica ou juridica)

    # Mostra na tela os itens do menu
    print("\n=-=-=-=-=-=-=-= Escolha o item para adicionar =-=-=-=-=-=-=-=")
    print("[0] {:<25} [7] {:<25}".format("Açúcar", "Farinha de Trigo"))
    print("[1] {:<25} [8] {:<25}".format("Arroz", "Feijão"))
    print("[2] {:<25} [9] {:<25}".format("Café", "Sal"))
    print("[3] {:<25} [10] {:<25}".format("Extrato de Tomate", "Outros Itens"))
    print("[4] {:<25}".format("Macarrão", ""))
    print("[5] {:<25}".format("Pacote de Bolacha", ""))
    print("[6] {:<25} [11] {:<25}".format("Óleo", "Finalizar doação"))
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

    numero_da_opcao = 0 # pré define o item do menu como 0

    while numero_da_opcao != 11: # Equanto o usuário não pedir o relatório
        numero_da_opcao = ler_e_validar_input_de_numeros(0, 11, "Sua Opção: ", "Digite um número entre 0 (zero) e 11 (onze): ") # pede e valida a opção de menu do usuário

        # Pré define as variáveis locais e iguala seus valores a 0
        local_qnt_acucar = local_qnt_arroz = local_qnt_cafe = local_qnt_extrato_de_tomate = local_qnt_macarrao = local_qnt_pct_bolacha = local_qnt_oleo = local_qnt_farinha_de_trigo = local_qnt_feijao = local_qnt_sal = local_qnt_outros = 0

        # Verifica a opção que o usuário digitou
        # Se for um tipo valido, ele pede um input de entrada e atualiza o valor da variável correspondente
        if numero_da_opcao == 0: # açucar
            local_qnt_acucar = ler_e_validar_item(f"Quanto de Açúcar foi doado por {nome}? (KG) ") # recebe e valida a quantidade do item
        elif numero_da_opcao == 1: # arroz
            local_qnt_arroz = ler_e_validar_item(f"Quanto de Arroz foi doado por {nome}? (KG) ")
        elif numero_da_opcao == 2: # café
            local_qnt_cafe = ler_e_validar_item(f"Quanto de Café foi doado por {nome}? (KG) ")
        elif numero_da_opcao == 3: # extrato de tomate
            local_qnt_extrato_de_tomate = ler_e_validar_item(f"Quanto de Extrato de Tomate foi doado por {nome}? (unidades) ")
        elif numero_da_opcao == 4: # macarrão
            local_qnt_macarrao = ler_e_validar_item(f"Quanto de Macarrão foi doado por {nome}? (unidades) ")
        elif numero_da_opcao == 5: # pacote de bolacha
            local_qnt_pct_bolacha = ler_e_validar_item(f"Quanto de Pacote de Bolacha foi doado por {nome}? (unidades) ")
        elif numero_da_opcao == 6: # óleo
            local_qnt_oleo = ler_e_validar_item(f"Quanto de Óleo foi doado por {nome}? (litros) ")
        elif numero_da_opcao == 7: # farinha de trigo
            local_qnt_farinha_de_trigo = ler_e_validar_item(f"Quanto de Farinha de Trigo foi doado por {nome}? (KG) ")
        elif numero_da_opcao == 8: # feijão
            local_qnt_feijao = ler_e_validar_item(f"Quanto de Feijão foi doado por {nome}? (KG) ")
        elif numero_da_opcao == 9: # sal
            local_qnt_sal = ler_e_validar_item(f"Quanto de Sal foi doado por {nome}? (KG) ")
        elif numero_da_opcao == 10: # outro itens
            local_qnt_outros = ler_e_validar_item(f"Quanto de Outros Itens foi doado por {nome}? (unidades) ")

        # Adiciona o item doado pelo usuário aos itens totais doados
        qnt_acucar += local_qnt_acucar
        qnt_arroz += local_qnt_arroz
        qnt_cafe += local_qnt_cafe
        qnt_extrato_de_tomate += local_qnt_extrato_de_tomate
        qnt_macarrao += local_qnt_macarrao
        qnt_pct_bolacha += local_qnt_pct_bolacha
        qnt_oleo += local_qnt_oleo
        qnt_farinha_de_trigo += local_qnt_farinha_de_trigo
        qnt_feijao += local_qnt_feijao
        qnt_sal += local_qnt_sal
        qnt_outros += local_qnt_outros

        # Soma todos os itens doados numa variável local
        total_itens_doados_pelo_usuario = local_qnt_acucar + local_qnt_arroz + local_qnt_cafe + local_qnt_extrato_de_tomate + local_qnt_macarrao + local_qnt_pct_bolacha + local_qnt_oleo + local_qnt_farinha_de_trigo + local_qnt_feijao + local_qnt_sal + local_qnt_outros

        # Verifica o tipo de pessoa e adiciona a quantidade total doada ao tipo de pessoa ( fisica ou juridica )
        if tipo_do_doador == "fisica":
            qnt_de_doacoes_por_pessoa_fisica += total_itens_doados_pelo_usuario
        elif tipo_do_doador == "juridica":
            qnt_de_doacoes_por_pessoa_juridica += total_itens_doados_pelo_usuario

    clear() # limpa a tela do terminal

    print(f"\nMuito bem! O doador {nome} foi devidamente cadastrado!")
    print("Você deseja continuar a cadastrar outro doador?")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("[0] {:<25} [1] {:<25}".format("Adicionar novo doador", "Ir para relatórios"))
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    deve_continuar = ler_e_validar_input_de_numeros(0, 1, "Sua opção: ", "Valor informado é inválido.") == 0 # recebe e valida a opção de continuar ou não no programa



########## PRINT DOS RELATÓRIOS ##########

if mostrar_relatorio: # se foi escolhido a opção de mostrar o relatório
    clear() # limpa a tela do terminal

    print("\n=-=-=-=-=-=-=-= Relatório das Doações =-=-=-=-=-=-=-=\n")
    print("Itens doados:")
    print(f"     {qnt_acucar} KG de Açúcar")
    print(f"     {qnt_arroz} KG de Arroz")
    print(f"     {qnt_cafe} KG de Café")
    print(f"     {qnt_extrato_de_tomate} unidade(s) de Extrato de Tomate")
    print(f"     {qnt_macarrao} unidade(s) de Macarrão")
    print(f"     {qnt_pct_bolacha} unidade(s) de Pacote de Bolacha")
    print(f"     {qnt_oleo} litro(s) de Óleo")
    print(f"     {qnt_farinha_de_trigo} unidade(s) de Farinha de Trigo")
    print(f"     {qnt_feijao} KG de Feijão")
    print(f"     {qnt_sal} KG de Sal")
    print(f"     {qnt_outros} unidade(s) de Outros Produtos")
    print("")
    print("Itens doados por tipo de pessoa:")
    print(f"     {qnt_de_doacoes_por_pessoa_fisica} item(ns) doado(s) por PESSOA FÍSICA")
    print(f"     {qnt_de_doacoes_por_pessoa_juridica} item(ns) doado(s) por PESSOA JURÍDICA\n")


    # calcula quantas cestas básicas poderão ser formadas
    cestas_com_acucar = qnt_acucar // ACUCAR_QNT_POR_CESTA # divide a quatidade do item doado pela quantidade necessaria deste item por cesta, retornando valor inteiro da divisão, sem resto
    cestas_com_arroz = qnt_arroz // ARROZ_QNT_POR_CESTA
    cestas_com_cafe = qnt_cafe // CAFE_QNT_POR_CESTA
    cestas_com_extrato_de_tomate = qnt_extrato_de_tomate // EXTRATO_DE_TOMATE_QNT_POR_CESTA
    cestas_com_macarrao = qnt_macarrao // MACARRAO_QNT_POR_CESTA
    cestas_com_pct_bolacha = qnt_pct_bolacha // PCT_BOLACHA_QNT_POR_CESTA
    cestas_com_oleo = qnt_oleo // OLEO_QNT_POR_CESTA
    cestas_com_farinha_de_trigo = qnt_farinha_de_trigo // FARINHA_DE_TRIGO_QNT_POR_CESTA
    cestas_com_feijao = qnt_feijao // FEIJAO_QNT_POR_CESTA
    cestas_com_sal = qnt_sal // SAL_QNT_POR_CESTA

    quantidade_de_cestas = min(cestas_com_acucar, cestas_com_arroz, cestas_com_cafe, cestas_com_extrato_de_tomate, cestas_com_macarrao, cestas_com_pct_bolacha, cestas_com_oleo, cestas_com_farinha_de_trigo, cestas_com_feijao, cestas_com_sal) # pega o menor valor dentre as cestas calculadas.

    # fim do calculo

    print("Cestas básicas que poderão ser formadas:")
    print(f"     {quantidade_de_cestas} cesta(s) básica(s) completa(s)\n")

    quantidade_de_cestas_com_item_extra = min(qnt_outros, quantidade_de_cestas)  # calcula quantas cestas terão itens extras

    print("Cestas básicas que receberão itens extras:")
    print(f"     {quantidade_de_cestas_com_item_extra} cesta(s) básica(s)\n")

    quantidade_de_cestas_sem_item_extra = quantidade_de_cestas - quantidade_de_cestas_com_item_extra # calcula quantas cestas não terão itens extras

    print("Cestas básicas que NÃO receberão itens extras:")
    print(f"     {quantidade_de_cestas_sem_item_extra} cesta(s) básica(s)\n")

    # calcula quantos itens sobraram após a montagem das cestas
    sobra_acucar = qnt_acucar - (quantidade_de_cestas * ACUCAR_QNT_POR_CESTA)
    sobra_arroz = qnt_arroz - (quantidade_de_cestas * ARROZ_QNT_POR_CESTA)
    sobra_cafe = qnt_cafe - (quantidade_de_cestas * CAFE_QNT_POR_CESTA)
    sobra_extrato_de_tomate = qnt_extrato_de_tomate - (quantidade_de_cestas * EXTRATO_DE_TOMATE_QNT_POR_CESTA)
    sobra_macarrao = qnt_macarrao - (quantidade_de_cestas * MACARRAO_QNT_POR_CESTA)
    sobra_pct_bolacha = qnt_pct_bolacha - (quantidade_de_cestas * PCT_BOLACHA_QNT_POR_CESTA)
    sobra_oleo = qnt_oleo - (quantidade_de_cestas * OLEO_QNT_POR_CESTA)
    sobra_farinha_de_trigo = qnt_farinha_de_trigo - (quantidade_de_cestas * FARINHA_DE_TRIGO_QNT_POR_CESTA)
    sobra_feijao = qnt_feijao - (quantidade_de_cestas * FEIJAO_QNT_POR_CESTA)
    sobra_sal = qnt_sal - (quantidade_de_cestas * SAL_QNT_POR_CESTA)
    sobra_outros = max(qnt_outros - quantidade_de_cestas, 0)
    # fim do calculo

    print("Itens que sobraram após a montagem das Cestas Básicas:")
    print(f"     {sobra_acucar} KG de Açucar")
    print(f"     {sobra_arroz} KG de Arroz")
    print(f"     {sobra_cafe} KG de Café")
    print(f"     {sobra_extrato_de_tomate} unidade(s) de Extrato de Tomate")
    print(f"     {sobra_macarrao} unidade(s) de Macarrão")
    print(f"     {sobra_pct_bolacha} unidade(s) de Pacote de Bolacha")
    print(f"     {sobra_oleo} litro(s) de Óleo")
    print(f"     {sobra_farinha_de_trigo} unidade(s) de Farinha de Trigo")
    print(f"     {sobra_feijao} KG de Feijão")
    print(f"     {sobra_sal} KG de Sal")
    print(f"     {sobra_outros} unidade(s) de Outros Produtos")