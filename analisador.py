import ply.lex as lex
import ply.yacc as yacc

# Lista de tokens
tokens = (
    'IDENTIFICADOR',
    'NUMERO',
    'OPERADOR',
    'ATRIBUICAO',
)

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

# Regra para expressão
def p_expression(p):
    '''
    expression : IDENTIFICADOR ATRIBUICAO expression
               | expression OPERADOR expression
               | IDENTIFICADOR
               | NUMERO
    '''
    if len(p) == 4:
        if p[2] == '=':
            p[0] = p[3]
            print(f"{p[1]} = {p[0]}")
        else:
            print("Erro: Após o símbolo de atribuição não pode aceitar mais de três operandos ou operadores")
            p[0] = None
    else:
        p[0] = p[1]

# Tratamento de erros de sintaxe
def p_error(p):
    if p:
        print("Erro de sintaxe: '%s'" % p.value)
    else:
        print("Erro de sintaxe: fim de arquivo inesperado")

# Construção do parser
parser = yacc.yacc()

# Função para analisar a entrada
def analisar_entrada(entrada):
    lexer.input(entrada)
    while True:
        token = lexer.token()
        if not token:
            break
        print(f"{token.value} : {token.type}")
    parser.parse(entrada)

# Loop para entrada de dados
while True:
    entrada = input("Entrada de dados (digite 'sair' para encerrar): ")
    if entrada == 'sair':
        break
    analisar_entrada(entrada)
