import re


def markdown_to_html(markdown):
    # cabeçalhos
    markdown = re.sub(r'### (.*?)\n', r'<h3>\1</h3>\n', markdown)
    markdown = re.sub(r'## (.*?)\n', r'<h2>\1</h2>\n', markdown)
    markdown = re.sub(r'# (.*?)\n', r'<h1>\1</h1>\n', markdown)

    # negrito e itálico
    markdown = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', markdown)
    markdown = re.sub(r'\*(.*?)\*', r'<i>\1</i>', markdown)

    # listas numeradas
    def replace_list(match):
        items = match.group(0).split('\n')
        html_list = '<ol>\n' + ''.join(f'    <li>{item[3:]}</li>\n' for item in items if item.strip()) + '</ol>'
        return html_list

    markdown = re.sub(r'(\d+\..+(?:\n\d+\..+)*)', replace_list, markdown, flags=re.MULTILINE)

    # imagens
    markdown = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1"/>', markdown)

    # links
    markdown = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', markdown)

    return markdown


# exemplo
markdown_text = """
# Exemplo
Este é um **exemplo** 
Este é um *exemplo*
1. Primeiro item
2. Segundo item
3. Terceiro item
Como pode ser consultado em [página da UC](http://www.uc.pt)
Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coellho.com)
"""

html_output = markdown_to_html(markdown_text)
print(html_output)
