# Nomes: Felipe Men dos Santos; Otho Oliveira Candido; Lucas Rodrigues de Queiroz; João Pedro Silva Pinheiro
# RMs: 557571; 55054; 556323; 557013

import time

print("Seja Bem-Vindo(a) ao nosso sistema de estatísticas para os corredores da Fórmula E!")

corredores = {} # cria o dicionário vazio para poder inserir os novos corredores.

def adicionar_corredor():

    '''Essa função será a mais utilizada e mais importante do código, onde utiliza as informações passadas pelo usuário para criar um novo perfil para um corredor dentro do dicionário.'''

    corredor = {}
    while True:
        try:
            nome = str(input("Digite o NOME do corredor: "))
            volta = float(input("Digite a melhor tempo de volta do corredor: "))
            vitorias = int(input("Digite quantas vezes o corredor chegou em primeiro lugar na sua carreira: "))
        except Exception as mensagem:
            print(f"Um ERRO inesperado ocorreu: {mensagem}")
        else:
            corredor["VOLTAS"] = volta
            corredor["VITORIAS"] = vitorias
            corredores[nome.upper()] = corredor
            break

def remover_corredor(nome: str):

    '''Essa função remove o corredor solicitado pelo usuário utilizando a função "pop()".'''

    print("Removendo Corredor...")
    time.sleep(1)
    corredores.pop(nome.upper())
    print("Corredor Removido com sucesso!")

def consultar_corredores():

    '''Essa função utiliza com "for" para percorrer o dicionário "corredores" e mostra suas informações de um jeito mais organizado e bonito.'''

    for chave, valor in corredores.items():
        print(chave, valor)

def editar_corredor(nome: str, volta_nova: float, vitorias_nova: int):

    '''Essa função pega os parâmetros passados dentro do case em que é chamada e altera as informações do corredor inserido pelo usuário.'''

    print("Editando estatísticas...")
    corredor = {}
    corredor["VOLTAS"] = volta_nova
    corredor["VITORIAS"] = vitorias_nova
    corredores[nome.upper()] = corredor
    print("Informações editadas com sucesso!")

def melhor_volta():

    '''Essa função percorre o dicionário "corredores" e da um print com o corredor que possui o menor tempo de volta.'''

    if corredores:
        melhor_volta = min(corredores.items(), key=lambda x: x[1]["VOLTAS"])
        print(f"O corredor com a melhor volta é {melhor_volta[0]} com o tempo de {melhor_volta[1]['VOLTAS']:.2f} segundos.")
    else:
        print("Não há corredores cadastrados para comparar.")

def mais_vitorias():

    '''Essa função percorre o dicionário "corredores" e da um print com o corredor que possui a maior quantidade de vitórias.'''

    if corredores:
        corredor_vitorioso = max(corredores.items(), key=lambda x: x[1]["VITORIAS"])
        print(f"O corredor com mais vitórias é {corredor_vitorioso[0]} com {corredor_vitorioso[1]['VITORIAS']} vitórias.")
    else:
        print("Não há corredores cadastrados para comparar.")


def main():

    """Função principal do programa, junta as outras função para chama-las usando o match case."""

    while True:
        print("""
1 - Adicionar Corredor
2 - Remover Corredor
3 - Consultar Estatísticas
4 - Editar Estatísticas
5 - Mostrar Corredor com MENOR tempo de volta
6 - Mostrar Corredor com MAIOR número de vitórias
7 - Encerrar Programa                          
""")
        try:
            escolha = int(input("O que deseja fazer? (Digite o número): "))
        except TypeError as mensagem:
            print("ERRO - Digite um número inteiro: ")
        except ValueError as mensagem:
            print("ERRO - Digite um número inteiro: ")
        except Exception as mensagem:
            print(f"um ERRO inesperado ocorreu: {mensagem}")
        else:
            
            '''Se o usuário não encontrar nenhum erro no menu ele pula as mensagens e vem direto para o match case, onde está juntando todas as funções.'''

            match escolha:
                case 1:
                    adicionar_corredor()
                case 2:
                    while True:
                        if corredores != {}:
                            try:
                                nome = str(input("Digite o NOME do corredor: "))
                            except Exception as mensagem:
                                print(f"Um ERRO inesperado ocorreu: {mensagem}")
                            else:
                                if nome.upper() in corredores:
                                    remover_corredor(nome)
                                    break
                                else:
                                    print("Esse corredor não está no nosso sistema...")
                                    continue
                        else:
                            print("A lista de corredores está vazia...")
                            break
                    
                case 3:
                    consultar_corredores()
                case 4:
                    while True:
                        if not corredores == {}:
                            try:
                                nome = str(input("Digite o NOME do corredor que deseja editar: "))
                                volta_nova = float(input("Digite o novo valor da volta: "))
                                vitorias_nova = int(input("Digite a quantidade de vitórias do corredor: "))
                            except Exception as mensagem:
                                print(f"Um ERRO inesperado ocorreu: {mensagem}")
                            else:
                                editar_corredor(nome, volta_nova, vitorias_nova)
                                break
                        else:
                            print("A lista de corredores está vazia!")
                            break
                case 5:
                    melhor_volta()
                case 6:
                    mais_vitorias()
                case 7:
                    print("Obrigado por utilizar nosso programa")
                    print("Encerrando...")
                    break
                case _:
                    print("ERRO - Opção inválida!")
main()