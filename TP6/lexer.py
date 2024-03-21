import ply.lex as lex


tokens = (
    'NUMBER',
    'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE',
    'LPAREN', 'RPAREN',
    'ID', 'ASSIGN',
    'QUERY', 'EXCLAM'
)


t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ASSIGN = r'='
t_QUERY = r'\?'
t_EXCLAM = r'!'


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t


t_ignore = ' \t'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


lexer = lex.lex()



data = '''
a = 3 + 4 * (10 - 5)
b = a * 2
! b
'''


lexer.input(data)


while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
