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

########## VARIÁVEIS ##########

# Quantidades de itens por cesta básica
cesta_qnt_acucar = 1  # kg
cesta_qnt_arroz = 4  # kg
cesta_qnt_cafe = 2  # kg
cesta_qnt_extrato_de_tomate = 2  # unidade
cesta_qnt_macarrao = 3  # unidade
cesta_qnt_pct_bolacha = 1  # unidade
cesta_qnt_oleo = 1  # litro
cesta_qnt_farinha_de_trigo = 1  # kg
cesta_qnt_feijao = 4  # kg
cesta_qnt_sal = 1  # kg

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

# Retorna quantas cestas básicas poderão ser formadas com os itens doados
def calcular_cestas():
    # quantos itens podem ser feitos por cesta
    cestas_com_acucar = qnt_acucar // cesta_qnt_acucar
    cestas_com_arroz = qnt_arroz // cesta_qnt_arroz
    cestas_com_cafe = qnt_cafe // cesta_qnt_cafe
    cestas_com_extrato_de_tomate = qnt_extrato_de_tomate // cesta_qnt_extrato_de_tomate
    cestas_com_macarrao = qnt_macarrao // cesta_qnt_macarrao
    cestas_com_pct_bolacha = qnt_pct_bolacha // cesta_qnt_pct_bolacha
    cestas_com_oleo = qnt_oleo // cesta_qnt_oleo
    cestas_com_farinha_de_trigo = qnt_farinha_de_trigo // cesta_qnt_farinha_de_trigo
    cestas_com_feijao = qnt_feijao // cesta_qnt_feijao
    cestas_com_sal = qnt_sal // cesta_qnt_sal

    return min(cestas_com_acucar, cestas_com_arroz, cestas_com_cafe, cestas_com_extrato_de_tomate, cestas_com_macarrao, cestas_com_pct_bolacha, cestas_com_oleo, cestas_com_farinha_de_trigo, cestas_com_feijao, cestas_com_sal)

# Retorna quantas cestas básicas terão itens extras
def cestas_com_item_extra():
    return min(qnt_outros, quantidade_de_cestas)

# Calcula quantos itens sobraram após a montagem das cestas
def calcular_sobra_de_itens():
    global sobra_acucar, sobra_arroz, sobra_cafe, sobra_extrato_de_tomate, sobra_macarrao, sobra_pct_bolacha, sobra_oleo, sobra_farinha_de_trigo, sobra_feijao, sobra_sal, sobra_outros  # adiciona as variáveis globais ao escopo local para poderem ser alteradas

    sobra_acucar = qnt_acucar - (quantidade_de_cestas * cesta_qnt_acucar)
    sobra_arroz = qnt_arroz - (quantidade_de_cestas * cesta_qnt_arroz)
    sobra_cafe = qnt_cafe - (quantidade_de_cestas * cesta_qnt_cafe)
    sobra_extrato_de_tomate = qnt_extrato_de_tomate - (quantidade_de_cestas * cesta_qnt_extrato_de_tomate)
    sobra_macarrao = qnt_macarrao - (quantidade_de_cestas * cesta_qnt_macarrao)
    sobra_pct_bolacha = qnt_pct_bolacha - (quantidade_de_cestas * cesta_qnt_pct_bolacha)
    sobra_oleo = qnt_oleo - (quantidade_de_cestas * cesta_qnt_oleo)
    sobra_farinha_de_trigo = qnt_farinha_de_trigo - (quantidade_de_cestas * cesta_qnt_farinha_de_trigo)
    sobra_feijao = qnt_feijao - (quantidade_de_cestas * cesta_qnt_feijao)
    sobra_sal = qnt_sal - (quantidade_de_cestas * cesta_qnt_sal)
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
    nome = ""  # nome do doador
    tipo_do_doador = ""  # física ou jurídica

    print("\n=-=-=-=-=-=-=-= Sobre o doador =-=-=-=-=-=-=-=")
    nome = str(input("Qual o nome do doador? "))
    tipo_do_doador = str(input("Qual o tipo de pessoa? (fisica ou juridica) ")).lower()

    print("\n=-=-=-=-=-=-=-= Itens doados =-=-=-=-=-=-=-=")
    local_qnt_acucar = int(input(f"Quanto de Açúcar foi doado por {nome}? (KG) "))
    local_qnt_arroz = int(input(f"Quanto de Arroz foi doado por {nome}? (KG) "))
    local_qnt_cafe = int(input(f"Quanto de Café foi doado por {nome}? (KG) "))
    local_qnt_extrato_de_tomate = int(input(f"Quanto de Extrato de Tomate foi doado por {nome}? (unidades) "))
    local_qnt_macarrao = int(input(f"Quanto de Macarrão foi doado por {nome}? (unidades) "))
    local_qnt_pct_bolacha = int(input(f"Quanto de Pacote de Bolacha foi doado por {nome}? (unidades) "))
    local_qnt_oleo = int(input(f"Quanto de Óleo foi doado por {nome}? (litros) "))
    local_qnt_farinha_de_trigo = int(input(f"Quanto de Farinha de Trigo foi doado por {nome}? (KG) "))
    local_qnt_feijao = int(input(f"Quanto de Feijão foi doado por {nome}? (KG) "))
    local_qnt_sal = int(input(f"Quanto de Sal foi doado por {nome}? (KG) "))
    local_qnt_outros = int(input(f"Quanto de Outros Itens foi doado por {nome}? (unidades) "))

    total_itens_doados_pelo_usuario = local_qnt_acucar + local_qnt_arroz + local_qnt_cafe + local_qnt_extrato_de_tomate + local_qnt_macarrao + local_qnt_pct_bolacha + local_qnt_oleo + local_qnt_farinha_de_trigo + local_qnt_feijao + local_qnt_sal + local_qnt_outros

    if tipo_do_doador == "fisica":
        qnt_de_doacoes_por_pessoa_fisica += total_itens_doados_pelo_usuario
    elif tipo_do_doador == "juridica":
        qnt_de_doacoes_por_pessoa_juridica += total_itens_doados_pelo_usuario

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

    print(f"\nMuito bem! O doador {nome} foi devidamente cadastrado!")
    print("Você deseja continuar a cadastrar outro doador?")
    deve_continuar = input("Digite SIM para continuar ou NAO para ir para os relatórios: ").lower() == "sim"

print("\n=-=-=-=-=-=-=-= Relatório do Dia =-=-=-=-=-=-=-=")
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