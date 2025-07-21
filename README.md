O Projeto postado possui finalidade de estudo / acadêmica. Nesse projeto foi realizado um webscraping com o Projeto Gutenberg. O Projeto Gutenberg disponibiliza títulos famosos disponíveis em domínio público visando fins acadêmicos. O projeto retorna uma planilha csv, contendo os títulos, o número de downloads nos últimos 30 dias e o link para a Obra

Após baixar esse projeto do Github, no terminal, instale as seguintes bibliotecas a partir dos seguinte comando:

- pip install requests beautifulsoup4

Então, rode a aplicação:

- python web_scraping.py
  
Será gerado um arquivo CSV de nome 'database' + 'Dia do Scraping', que pode ser acessada.
