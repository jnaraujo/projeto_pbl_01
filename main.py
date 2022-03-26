""" /*******************************************************************************

    Autor: Jônatas Araújo Silva Santos
    Componente Curricular: Algoritmos I
    Concluido em: 30/03/2022
    Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
    trecho de código de outro colega ou de outro autor, tais como provindos de livros e
    apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código de
    outra autoria que não a minha está destacado com uma citação para o autor e a fonte do
    código, e estou ciente que estes trechos não serão considerados para fins de avaliação.

******************************************************************************************/ """

########## CONSTANTES ##########

# Quantidades de itens por cesta básica

CESTA_QNT_ACUCAR = 1  # KG
CESTA_QNT_ARROZ = 4  # KG
CESTA_QNT_CAFE = 2  # KG
CESTA_QNT_EXTRATO_DE_TOMATE = 2  # UNIDADE
CESTA_QNT_MACARRAO = 3  # UNIDADE
CESTA_QNT_PCT_BOLACHA = 1  # UNIDADE
CESTA_QNT_OLEO = 1  # LITRO
CESTA_QNT_FARINHA_DE_TRIGO = 1  # KG
CESTA_QNT_FEIJAO = 4  # KG
CESTA_QNT_SAL = 1  # KG

########## VARIÁVEIS ##########

# Quantidades de itens doados
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

# Quantidades de itens sobrando por cesta básica
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
quantidade_de_cestas=0
quantidade_de_cestas_com_item_extra=0
quantidade_de_cestas_sem_item_extra=0

# Quantidades por tipo de pessoa (física ou juridica)
qnt_de_doacoes_por_pessoa_fisica = 0
qnt_de_doacoes_por_pessoa_juridica = 0

# Variáveis para controle de funcionamento
deve_continuar = True


########## FUNÇÕES ##########

# Recebe do usuário um input do tipo int e verifica se o valor informado está dentre os limites pra estabelecidos
# Se estiver, o valor é retornado.
# Se não, uma mensagem de erro é exibido e o usuário é novamente pedido para informar o valor correto
def ler_e_validar_input_de_numeros(v_min, v_max, mensagem, erro):
    try:
        entrada = int(input(mensagem))
        while entrada < v_min or entrada > v_max:
            entrada = int(input(erro))
        return entrada
    except:
        print("Valor inválido.")
        return ler_e_validar_input_de_numeros(v_min, v_max, mensagem, erro)

# Recebe do usuário um input do tipo int e verifica se o valor informado é valido
# Se positivo, o valor é retornado.
# Se negativo, uma mensagem de erro é exibido e o usuário é novamente pedido para informar o valor correto
def ler_e_validar_item(mensagem):
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
    entrada = input(mensagem).lower()

    # verifica se o tipo de doador é valido
    if entrada == "fisica" or entrada == "juridica":
        return entrada
    else:
        print("Valor informado é inválido.")
        return ler_e_validar_tipo_do_doador(mensagem)

# Retorna quantas cestas básicas poderão ser formadas com os itens doados
def calcular_cestas():
    # quantos itens podem ser feitos por cesta
    cestas_com_acucar = qnt_acucar // CESTA_QNT_ACUCAR
    cestas_com_arroz = qnt_arroz // CESTA_QNT_ARROZ
    cestas_com_cafe = qnt_cafe // CESTA_QNT_CAFE
    cestas_com_extrato_de_tomate = qnt_extrato_de_tomate // CESTA_QNT_EXTRATO_DE_TOMATE
    cestas_com_macarrao = qnt_macarrao // CESTA_QNT_MACARRAO
    cestas_com_pct_bolacha = qnt_pct_bolacha // CESTA_QNT_PCT_BOLACHA
    cestas_com_oleo = qnt_oleo // CESTA_QNT_OLEO
    cestas_com_farinha_de_trigo = qnt_farinha_de_trigo // CESTA_QNT_FARINHA_DE_TRIGO
    cestas_com_feijao = qnt_feijao // CESTA_QNT_FEIJAO
    cestas_com_sal = qnt_sal // CESTA_QNT_SAL

    return min(cestas_com_acucar, cestas_com_arroz, cestas_com_cafe, cestas_com_extrato_de_tomate, cestas_com_macarrao, cestas_com_pct_bolacha, cestas_com_oleo, cestas_com_farinha_de_trigo, cestas_com_feijao, cestas_com_sal)

# Retorna quantas cestas básicas terão itens extras
def cestas_com_item_extra():
    return min(qnt_outros, quantidade_de_cestas)

# Calcula quantos itens sobraram após a montagem das cestas e altera as varíaveis globalmente
def calcular_sobra_de_itens():
    global sobra_acucar, sobra_arroz, sobra_cafe, sobra_extrato_de_tomate, sobra_macarrao, sobra_pct_bolacha, sobra_oleo, sobra_farinha_de_trigo, sobra_feijao, sobra_sal, sobra_outros  # adiciona as variáveis globais ao escopo local para poderem ser alteradas

    sobra_acucar = qnt_acucar - (quantidade_de_cestas * CESTA_QNT_ACUCAR)
    sobra_arroz = qnt_arroz - (quantidade_de_cestas * CESTA_QNT_ARROZ)
    sobra_cafe = qnt_cafe - (quantidade_de_cestas * CESTA_QNT_CAFE)
    sobra_extrato_de_tomate = qnt_extrato_de_tomate - (quantidade_de_cestas * CESTA_QNT_EXTRATO_DE_TOMATE)
    sobra_macarrao = qnt_macarrao - (quantidade_de_cestas * CESTA_QNT_MACARRAO)
    sobra_pct_bolacha = qnt_pct_bolacha - (quantidade_de_cestas * CESTA_QNT_PCT_BOLACHA)
    sobra_oleo = qnt_oleo - (quantidade_de_cestas * CESTA_QNT_OLEO)
    sobra_farinha_de_trigo = qnt_farinha_de_trigo - (quantidade_de_cestas * CESTA_QNT_FARINHA_DE_TRIGO)
    sobra_feijao = qnt_feijao - (quantidade_de_cestas * CESTA_QNT_FEIJAO)
    sobra_sal = qnt_sal - (quantidade_de_cestas * CESTA_QNT_SAL)
    sobra_outros = max(qnt_outros - quantidade_de_cestas, 0)


########## PARTE VISUAL DO PROJETO ##########

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print(" Olá, usuário!")
print(" Seja bem-vindo(a) ao")
print(" Sistema de Registro de Doações do Dispensário Santana ( SRDDS )")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

input("Aperte ENTER para cadastrar um novo doador: ")  # somente para não iniciar diretamente no cadastro de usuários

while deve_continuar:
    # Informações do usuário
    print("\n=-=-=-=-=-=-=-= Sobre o doador =-=-=-=-=-=-=-=")
    nome = str(input("Qual o nome do doador? ")).upper()
    tipo_do_doador = ler_e_validar_tipo_do_doador("Qual o tipo de pessoa? (fisica ou juridica) ")

    print("\n=-=-=-=-=-=-=-= Escolha o item para adicionar =-=-=-=-=-=-=-=")
    print("[0] {:<25} [7] {:<25}".format("Açúcar", "Farinha de Trigo"))
    print("[1] {:<25} [8] {:<25}".format("Arroz", "Feijão"))
    print("[2] {:<25} [9] {:<25}".format("Café", "Sal"))
    print("[3] {:<25} [10] {:<25}".format("Extrato de Tomate", "Outros Itens"))
    print("[4] {:<25}".format("Macarrão", ""))
    print("[5] {:<25}".format("Pacote de Bolacha", ""))
    print("[6] {:<25} [11] {:<25}".format("Óleo", "Finalizar doação"))

    numero_da_opcao = 0

    while numero_da_opcao != 11: # Equanto o usuário não pedir o relatório
        numero_da_opcao = ler_e_validar_input_de_numeros(0, 11, "Sua Opção: ", "Digite um número entre 0 (zero) e 11 (onze): ")

        # Pré define as variáveis locais e iguala seus valores a 0
        local_qnt_acucar = local_qnt_arroz = local_qnt_cafe = local_qnt_extrato_de_tomate = local_qnt_macarrao = local_qnt_pct_bolacha = local_qnt_oleo = local_qnt_farinha_de_trigo = local_qnt_feijao = local_qnt_sal = local_qnt_outros = 0

        # Verifica a opção que o usuário digitou
        if numero_da_opcao == 0:
            local_qnt_acucar = ler_e_validar_item(f"Quanto de Açúcar foi doado por {nome}? (KG) ")
        elif numero_da_opcao == 1:
            local_qnt_arroz = ler_e_validar_item(f"Quanto de Arroz foi doado por {nome}? (KG) ")
        elif numero_da_opcao == 2:
            local_qnt_cafe = ler_e_validar_item(f"Quanto de Café foi doado por {nome}? (KG) ")
        elif numero_da_opcao == 3:
            local_qnt_extrato_de_tomate = ler_e_validar_item(f"Quanto de Extrato de Tomate foi doado por {nome}? (unidades) ")
        elif numero_da_opcao == 4:
            local_qnt_macarrao = ler_e_validar_item(f"Quanto de Macarrão foi doado por {nome}? (unidades) ")
        elif numero_da_opcao == 5:
            local_qnt_pct_bolacha = ler_e_validar_item(f"Quanto de Pacote de Bolacha foi doado por {nome}? (unidades) ")
        elif numero_da_opcao == 6:
            local_qnt_oleo = ler_e_validar_item(f"Quanto de Óleo foi doado por {nome}? (litros) ")
        elif numero_da_opcao == 7:
            local_qnt_farinha_de_trigo = ler_e_validar_item(f"Quanto de Farinha de Trigo foi doado por {nome}? (KG) ")
        elif numero_da_opcao == 8:
            local_qnt_feijao = ler_e_validar_item(f"Quanto de Feijão foi doado por {nome}? (KG) ")
        elif numero_da_opcao == 9:
            local_qnt_sal = ler_e_validar_item(f"Quanto de Sal foi doado por {nome}? (KG) ")
        elif numero_da_opcao == 10:
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

        total_itens_doados_pelo_usuario = local_qnt_acucar + local_qnt_arroz + local_qnt_cafe + local_qnt_extrato_de_tomate + local_qnt_macarrao + local_qnt_pct_bolacha + local_qnt_oleo + local_qnt_farinha_de_trigo + local_qnt_feijao + local_qnt_sal + local_qnt_outros

        # Verifica o tipo de pessoa e adiciona o item doado ao tipo
        if tipo_do_doador == "fisica":
            qnt_de_doacoes_por_pessoa_fisica += total_itens_doados_pelo_usuario
        elif tipo_do_doador == "juridica":
            qnt_de_doacoes_por_pessoa_juridica += total_itens_doados_pelo_usuario

    print(f"\nMuito bem! O doador {nome} foi devidamente cadastrado!")
    print("Você deseja continuar a cadastrar outro doador?")
    deve_continuar = ler_e_validar_input_de_numeros(0, 1, "[0] {:<25} [1] {:<25}".format("Adicionar novo doador", "Ir para relatórios"), "Valor informado é inválido.") == 0

########## PRINT DOS RELATÓRIOS ##########

print("\n=-=-=-=-=-=-=-= Relatório das Doações =-=-=-=-=-=-=-=")
print("")
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
print(f"     {qnt_de_doacoes_por_pessoa_juridica} item(ns) doado(s) por PESSOA JURÍDICA")
print("")

quantidade_de_cestas = calcular_cestas()  # calcula quantas cestas básicas poderão ser formadas

print("Cestas básicas que poderão ser formadas:")
print(f"     {quantidade_de_cestas} cesta(s) básica(s) completa(s)")
print("")

quantidade_de_cestas_com_item_extra = cestas_com_item_extra()  # calcula quantas cestas terão itens extras

print("Cestas básicas que receberão itens extras:")
print(f"     {quantidade_de_cestas_com_item_extra} cesta(s) básica(s)")
print("")

quantidade_de_cestas_sem_item_extra = quantidade_de_cestas - quantidade_de_cestas_com_item_extra

print("Cestas básicas que NÃO receberão itens extras:")
print(f"     {quantidade_de_cestas_sem_item_extra} cesta(s) básica(s)")
print("")

calcular_sobra_de_itens() # calcula quantos itens sobraram após a montagem das cestas

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
print("")