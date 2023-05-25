# Importando a biblioteca ply
import ply.lex as lex
import ply.yacc as yacc

# Definindo os tokens
tokens = [
    'IDENTIFICADOR',
    'NUMERO',
    'ATRIBUICAO',
    'ADD',
    'SUB',
    'MULT',
    'DIV',
    'DELIMITADOR'
]

# Definindo as expressões regulares para os tokens
t_IDENTIFICADOR = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_NUMERO = r'\d+(\.\d+)?'
t_ATRIBUICAO = r'='
t_ADD = r'\+'
t_SUB = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_DELIMITADOR = r';'

# Ignorando espaços em branco
t_ignore = ' \t'

# Definindo uma função para tratar erros léxicos


def t_error(t):
    print(f"Caractere ilegal: {t.value[0]}")
    t.lexer.skip(1)


# Criando o analisador léxico
lexer = lex.lex()

# Definindo a gramática da expressão de três endereços
"""
expressao : IDENTIFICADOR ATRIBUICAO expressao DELIMITADOR
          | termo ADD termo
          | termo SUB termo
          | termo MULT termo
          | termo DIV termo
          | IDENTIFICADOR
          | NUMERO

termo : IDENTIFICADOR
      | NUMERO
"""

# Definindo uma função para tratar erros sintáticos


def p_error(p):
    if p:
        print(f"Erro sintático: {p.value} na posição {p.lexpos}")
    else:
        print("Erro sintático: fim de arquivo inesperado")

# Definindo uma função para mostrar a tabela de símbolos


def mostrar_tabela(tabela):
    print("Tabela de Símbolos")
    print("lexema\ttoken")
    for lexema, token in tabela.items():
        print(f"{lexema}\t{token}")

# Definindo uma função para analisar a expressão de três endereços


def p_expressao(p):
    """
    expressao : IDENTIFICADOR ATRIBUICAO expressao DELIMITADOR
              | termo ADD termo
              | termo SUB termo
              | termo MULT termo
              | termo DIV termo
              | IDENTIFICADOR
              | NUMERO
    """
    # Criando uma tabela de símbolos vazia
    tabela = {}

    # Verificando se a expressão é válida (tem três operandos e dois operadores além da atribuição)
    if len(p) == 5 and p[2] == '=':
        # Contando o número de operandos e operadores na subexpressão
        operandos = 0
        operadores = 0
        for i in range(3, len(p) - 1):
            if p[i] in ('+', '-', '*', '/'):
                operadores += 1
            else:
                operandos += 1

        # Se o número de operandos for maior que três ou o número de operadores for maior que dois, mostrar uma mensagem de erro
        if operandos > 3 or operadores > 2:
            print(
                f"Erro: foram encontrados mais de três operandos e mais de dois operadores na expressão de três endereços: {p[1]} {p[2]} {' '.join(p[3:-1])} {p[-1]}")
            return

        # Caso contrário, adicionar os lexemas e tokens na tabela de símbolos
        else:
            tabela[p[1]] = 'IDENTIFICADOR'
            tabela[p[2]] = 'ATRIBUICAO'
            for i in range(3, len(p) - 1):
                if p[i] in ('+', '-', '*', '/'):
                    tabela[p[i]] = f'OPERADOR_{p[i]}'
                elif p[i].isalpha():
                    tabela[p[i]] = 'IDENTIFICADOR'
                else:
                    tabela[p[i]] = 'NUMERO'
            tabela[p[-1]] = 'DELIMITADOR'

# Se a expressão não for válida, mostrar uma mensagem de erro
    else:
    # Verificar se p[1] é diferente de None
        if p[1] is not None:
        # Usar o método join para juntar os elementos da lista p[1:] em uma string
            print(
                f"Erro: expressão de três endereços inválida: {' '.join(p[1:])}")
        else:
        # Mostrar uma mensagem genérica de erro
            print("Erro: expressão de três endereços inválida")
        return


    # Mostrar a tabela de símbolos na tela
    mostrar_tabela(tabela)

# Definindo as regras para os termos da expressão


def p_termo(p):
    """
    termo : IDENTIFICADOR
          | NUMERO
    """
    pass


# Criando o analisador sintático
parser = yacc.yacc()

# Criando uma variável para armazenar a entrada do usuário
entrada = ""

# Criando um loop while para perguntar a entrada até que o usuário digite "sair"
while entrada != "sair":
 # Lendo a entrada de dados do usuário
 entrada = input("Entrada de dados (digite sair para encerrar): ")

 # Verificando se a entrada é diferente de "sair"
 if entrada != "sair":
 # Analisando a entrada com o analisador sintático e léxico
    parser.parse(entrada)