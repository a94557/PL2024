import re

def somador_on_off(texto):
    interruptor = re.compile(r'\d+|[oO][nN]|[oO][fF]{2}|=')

    soma = 0
    somar = False  # inicia desligado
    resultado = ""

    for match in interruptor.finditer(texto):
        palavra = match.group()

        # verifica se é ON, OFF, um número ou o "="
        if palavra.lower() == "on":
            somar = True
        elif palavra.lower() == "off":
            somar = False
        elif palavra == "=":
            resultado += "Soma = " + str(soma) + "\n"
            soma = 0
        else:  # caso seja um número
            if somar:
                soma += int(palavra)

    return resultado.strip()


# exemplo
exemplo = "onjgi7fofgfhgidotn123=On456Off78On90Off=On100="
print(somador_on_off(exemplo))

