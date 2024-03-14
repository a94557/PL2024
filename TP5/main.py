import ply.lex as lex
import json


tokens = [
    'MOEDA',
    'COMANDO',
    'IDENTIFICADOR',
    'VALOR_MOEDA'
]


t_MOEDA = r'MOEDA'
t_COMANDO = r'(LISTAR|SELECIONAR|SAIR|SALDO)'
t_IDENTIFICADOR = r'[A-Z0-9]+'
t_ignore = ' \t,.'


def t_VALOR_MOEDA(t):
    r'\d+e|\d+c'
    valor_moeda = t.value
    if valor_moeda in valores_moedas:
        t.value = valores_moedas[valor_moeda]
    else:
        print(f"Valor de moeda não reconhecido: {valor_moeda}")
        t.value = 0
    return t
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

def carregar_estoque():
    with open('stock.json', 'r') as f:
        data = json.load(f)
    return data['stock']

estoque = carregar_estoque()
saldo = 0.0

valores_moedas = {"1e": 1.0, "50c": 0.5, "20c": 0.2, "10c": 0.1, "5c": 0.05}

def processar_comando(comando):
    global saldo
    lexer.input(comando)
    token = lexer.token()
    while token:
        if token.type == 'COMANDO':
            if token.value == 'LISTAR':
                listar_produtos()
            elif token.value == 'SALDO':
                print(f"Saldo atual: {saldo:.2f}")
            elif token.value == 'SAIR':
                print("Até à próxima!")
                return False
        elif token.type == 'MOEDA':
            while True:
                token = lexer.token()
                if not token or token.type != 'VALOR_MOEDA':
                    break
                saldo += token.value
            print(f"Saldo atual: {saldo:.2f}")
            return True
        elif token.value == 'SELECIONAR':
            token = lexer.token()
            if token:
                selecionar_produto(token.value)
        token = lexer.token()
    return True

def listar_produtos():
    print("cod | nome | quantidade | preço")
    for produto in estoque:
        print(f"{produto['cod']} | {produto['nome']} | {produto['quant']} | {produto['preco']}")

def selecionar_produto(cod):
    global saldo
    for produto in estoque:
        if produto['cod'] == cod:
            if saldo >= produto['preco']:
                saldo -= produto['preco']
                print(f"Pode retirar o produto {produto['nome']}. Saldo restante: {saldo:.2f}")
                return
            else:
                print("Saldo insuficiente.")
                return
    print("Produto não encontrado.")

def main():
    global saldo
    saldo = 0.0
    print("maq: Máquina iniciada. Insira seu comando.")
    continuar = True
    while continuar:
        comando = input(">> ").upper()
        continuar = processar_comando(comando)

if __name__ == "__main__":
    main()
