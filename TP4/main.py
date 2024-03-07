import ply.lex as lex

# List of token names.   This is always required
tokens = (
    'SELECT',
    'FROM',
    'WHERE',
    'ID',
    'COMMA',
    'NUMBER',
    'GE'  # Greater than or Equal
)

# Regular expression rules for simple tokens
t_SELECT = r'Select'
t_FROM = r'From'
t_WHERE = r'Where'
t_COMMA = r','
t_GE = r'>='

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

# Erro handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test it out
data = 'Select id, nome, salario From empregados Where salario >= 820'

# Give the lexer some input
lexer.input(data)

for tok in lexer:
    print(tok)
    print(tok.type, tok.value, tok.lineno, tok.lexpos)
