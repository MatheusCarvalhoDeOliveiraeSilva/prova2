import ply.yacc as yacc
import ply.lex as lex

# Definição dos tokens
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
)

# Regras da gramática
def p_expression(p):
    '''
    expression : expression PLUS expression
               | expression MINUS expression
               | expression TIMES expression
               | expression DIVIDE expression
    '''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]

def p_expression_number(p):
    '''
    expression : NUMBER
    '''
    p[0] = p[1]

def p_expression_paren(p):
    '''
    expression : LPAREN expression RPAREN
    '''
    p[0] = p[2]

# Tratamento de erros
def p_error(p):
    print("Erro de sintaxe!")

# Definição dos tokens e expressões regulares
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

t_ignore = ' \t\n'  # Ignora espaços em branco e tabulações

# Tratamento de erros léxicos
def t_error(t):
    print("Caractere ilegal: '%s'" % t.value[0])
    t.lexer.skip(1)

# Construção do analisador léxico
lexer = lex.lex()

# Construção do analisador sintático
parser = yacc.yacc()

# Função para análise de uma expressão
def analyze_expression(expression):
    result = parser.parse(expression, lexer=lexer)
    return result

# Teste
expression = "3 + 4 * (2 - 1)"
result = analyze_expression(expression)
print("Resultado:", result)
