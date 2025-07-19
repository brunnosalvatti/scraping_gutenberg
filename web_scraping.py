import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

basic_url = 'https://www.gutenberg.org/ebooks/search/?sort_order=downloads&start_index='         # URL Básica de Busca para Web Scraping
initial_url = 'https://www.gutenberg.org'                                                        # URL Básica de Livro
n = 1                                                                                            # Index de Página
headers = {'User-Agent': 'Mozilla/5.0'}                                                          # Header para Acesso
data_atual = datetime.now()
dia = data_atual.day
mes = data_atual.month
ano = data_atual.year

while True:                                                                                      # Loop
    url = basic_url + str(n)                                                                     # Geração da Nova URL de Scraping
    r = requests.get(url, headers=headers)                                                       # Requisição

    if r.status_code != 200:                                                                     # Condição de Quebra de Loop Quando Requests Não Obter Sucsso
        print('Acesso Finalizado')
        break

    soup = BeautifulSoup(r.text, 'html.parser')                                                  # Método BeautifulSoup Aplicado ao html Gerado
    livros = soup.find_all('li', class_='booklink')                                              # Busca Realizada nas Tags <li class = 'booklink'></li>, que Contém as Informações de Interesse de Cada um dos Livros na Página                                        

    if not livros:                                                                               # Se Não Encontrar Nada Nessa Tag, Houve Problema!
        print('Problema no Index ' + str(n))
        break


    titulos_pagina = []                                                                          # Lista que Receberá os Títulos
    downloads = []                                                                               # Lisa que Receberá o Número de Downloads
    urls_pagina = []                                                                             # Lista que Receberá a URL da Página

    for livro in livros:                                                                         # Para Cada Elemento da Lista que Contém as Informações Relevantes a Cada um dos Livros, Fará uma Busca
        link_tag = livro.find('a', class_='link')                                                # Se Encontrará o Link que se Encontra Dentro de <a class = 'link'></a>
        titulo_tag = livro.find('span', class_='title')                                          # Se Encontrará o Título que se Encontra Dentro de <span class = 'title'></span>
        load = livro.find('span', class_='extra')                                                # Se Encontrará o Número de Downloads que se Encontra Dentro de <span class = 'extra'></span>

        if link_tag and titulo_tag and load:                                                     # Se Existirem os 3 Elementos
            href = link_tag['href']                                                              # Coleta-se o Link em href
            titulo = titulo_tag.get_text(strip=True)                                             # Coleta-se o Texto entre as Tags
            loads = load.get_text(strip=True)                                                    # Coleta-se os Downloads entre as Tags

            titulos_pagina.append(titulo)                                                        # Se Acrescenta o Título na Lista
            downloads.append(loads)                                                              # Se Acrescenta o Número de Downloads na Lista
            urls_pagina.append(initial_url + href)                                               # Se Acrescenta a URL nas URLs


    # Configurando o Salvamento do Arquivo de Webscraping

    modo_abertura = 'w' if n == 1 else 'a'                                                      # Existirá um Modo que Configurará se O Conteúdo Será Escrito (w) ou Adicionado (a) 

    with open('database_' + str(dia) + '_' + str(mes) + '_' + str(ano) + '.csv', modo_abertura, newline='', encoding='utf-8') as f:      # Abertura de um Novo Arquivo Chamado database
        writer = csv.writer(f, delimiter=';')
        if n == 1:                                                                              # Se n for 1, Estamos no Início, Devemos Então Escrever o que Cada Coluna se Refere
            writer.writerow(['Título', 'Downloads', 'URL'])                      
        for titulo, dl, url in zip(titulos_pagina, downloads, urls_pagina):                     # Então Escrevemos os Valores Obtidos
            writer.writerow([titulo, dl, url])                                                  # Escrita em Forma de Linha dos Conteúdos  

    print(f'Scraping Página: {n}')                                                              # Print do Scraping para Acompanhar a Execução do Algoritmo em Tempo Real
    n += 25                                                                                     # Soma-se 25, Pois Cada Página Exibe 25 Resultados