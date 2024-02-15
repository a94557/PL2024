from collections import Counter

def processar_dados_emd(ficheiro_csv):
    # Ler o ficheiro
    with open(ficheiro_csv, 'r', encoding='utf-8') as file:
        lines = file.readlines()[1:]  # Ignora o cabeçalho

    modalidades = Counter()
    aptos = 0
    inaptos = 0
    escaloes = Counter()

    for line in lines:
        fields = line.strip().split(',')
        idade = int(fields[5])
        modalidade = fields[8]
        resultado = fields[-1]

        # Contagem das modalidades
        modalidades[modalidade] += 1

        # Contagem de atletas aptos e inaptos
        if resultado == 'true':
            aptos += 1
        else:
            inaptos += 1

        # Escalão etário
        escalao = 5 * (idade // 5)
        escaloes[f'{escalao}-{escalao+4}'] += 1

    # Ordena as modalidades
    modalidades_ordenadas = sorted(modalidades)

    # Calcula as percentagens
    total_atletas = aptos + inaptos
    percent_aptos = (aptos / total_atletas) * 100
    percent_inaptos = (inaptos / total_atletas) * 100

    # Ordena os escalões etários
    escaloes_ordenados = sorted(escaloes.items())

    return modalidades_ordenadas, percent_aptos, percent_inaptos, escaloes_ordenados

# Caminho para o ficheiro CSV
ficheiro_csv = 'emd.csv'

# Processar os dados
modalidades_ordenadas, percentagem_aptos, percentagem_inaptos, escaloes_ordenados = processar_dados_emd(ficheiro_csv)

# Exibir os resultados
print("Modalidades Desportivas Ordenadas Alfabeticamente:", modalidades_ordenadas)
print("Percentagem de Atletas Aptos:", percentagem_aptos)
print("Percentagem de Atletas Inaptos:", percentagem_inaptos)
print("Distribuição de Atletas por Escalão Etário:", escaloes_ordenados)