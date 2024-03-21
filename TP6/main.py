from lexer import tokens
import ply.yacc as yacc

variables = {}


precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE'),
    ('right', 'UMINUS'),
)

# Regras de produção

def p_statement_assign(p):
    'statement : ID ASSIGN expression'
    variables[p[1]] = p[3]

def p_statement_expr(p):
    'statement : expression'
    print(p[1])

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression MULTIPLY expression
                  | expression DIVIDE expression'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]

def p_expression_uminus(p):
    'expression : MINUS expression %prec UMINUS'
    p[0] = -p[2]

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_expression_name(p):
    'expression : ID'
    try:
        p[0] = variables[p[1]]
    except LookupError:
        print(f"Undefined name '{p[1]}'")
        p[0] = 0

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")


parser = yacc.yacc()



input_text = '''
a = 3 + 4 * (10 - 5)
b = a * 2
! b
'''

parser.parse(input_text)

