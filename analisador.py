import ply.lex as lex
import ply.yacc as yacc

# Lista de tokens
tokens = (
    'IDENTIFICADOR',
    'NUMERO',
    'OPERADOR',
    'ATRIBUICAO',
)

# Tabela de símbolos
tabela_simbolos = {}

# Regras de expressão regular para tokens simples
t_IDENTIFICADOR = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_OPERADOR = r'[-+*/]'
t_ATRIBUICAO = r'='

# Regra de token para número
def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignorar espaços em branco
t_ignore = ' \t'

# Tratamento de erros
def t_error(t):
    print("Caractere inválido: '%s'" % t.value[0])
    t.lexer.skip(1)

# Construção do lexer
lexer = lex.lex()

# Regras de precedência dos operadores
precedence = (
    ('left', 'OPERADOR'),
)

# Variáveis globais para rastrear erros
erro_encontrado = False
erro_msg = ""

# Regra para expressão
def p_expression(p):
    '''
    expression : IDENTIFICADOR ATRIBUICAO expression
               | expression OPERADOR expression
               | IDENTIFICADOR
               | NUMERO
    '''
    global erro_encontrado, erro_msg

    if len(p) == 4 and p[2] == '=':
        if isinstance(p[3], tuple):
            # Verificar erros de mais de três operandos ou operadores após o símbolo de atribuição
            if len(p[3]) > 3:
                erro_encontrado = True
                erro_msg = "Erro: Foram encontrados mais de três operandos ou operadores após o símbolo de atribuição"
            else:
                p[0] = p[3]
                tabela_simbolos[p[1]] = p[0]
        else:
            p[0] = p[3]
            tabela_simbolos[p[1]] = p[0]
    else:
        p[0] = p[1]

        # Verificar erros de operandos e operadores consecutivos
        if isinstance(p[0], str) and len(p[0]) > 1:
            erro_encontrado = True
            erro_msg = "Erro: Dois operandos consecutivos encontrados separados por espaços em branco"

        if isinstance(p[0], str) and p[0] in ['+', '-', '*', '/']:
            erro_encontrado = True
            erro_msg = "Erro: Dois operadores consecutivos encontrados separados por espaços em branco"

# Tratamento de erros de sintaxe
def p_error(p):
    global erro_encontrado, erro_msg

    if p:
        erro_encontrado = True
        erro_msg = f"Erro de sintaxe: '{p.value}'"
    else:
        erro_encontrado = True
        erro_msg = "Erro de sintaxe: fim de arquivo inesperado"

# Construção do parser
parser = yacc.yacc()

# Função para analisar a entrada
def analisar_entrada(entrada):
    global erro_encontrado, erro_msg

    # Resetar variáveis de erro
    erro_encontrado = False
    erro_msg = ""

    tabela_simbolos.clear()

    lexer.input(entrada)
    while True:
        token = lexer.token()
        if not token:
            break
        print(f"{token.value} : {token.type}")

    parser.parse(entrada)

    if not erro_encontrado:
        print("Análise léxica concluída sem erros.")
        print("Tabela de Símbolos:")
        for chave, valor in tabela_simbolos.items():
            print(f"{chave} : {valor}")
    else:
        print(erro_msg)

# Loop principal para entrada de dados
while True:
    entrada = input("Entrada de dados (digite 'sair' para encerrar): ")
    if entrada == 'sair':
        break
    analisar_entrada(entrada)
