# Web Scraping e Download de Arquivos

Este projeto tem como objetivo realizar o web scraping de uma página web específica, filtrar os links que correspondem a um padrão específico e fazer o download dos arquivos encontrados. Além disso, os arquivos baixados são compactados em um arquivo zip.

## Bibliotecas Utilizadas

O projeto utiliza as seguintes bibliotecas:

- `requests`: Utilizada para realizar requisições HTTP e obter o conteúdo da página web.
- `BeautifulSoup`: Utilizada para fazer o parsing do HTML e extrair os links da página.
- `re`: Utilizada para realizar correspondência de padrões utilizando expressões regulares.
- `zipfile`: Utilizada para criar e manipular arquivos zip.

Certifique-se de ter as bibliotecas instaladas antes de executar o projeto. Caso precise instalá-las, você pode utilizar o gerenciador de pacotes `pip` para instalar as dependências. Veja os exemplo abaixo:

- ```bash pip install requests```
- ```bash pip install beautifulsoup4```
- ```bash pip install re```
- ```bash pip install zipfile```

Certifique-se de ter uma conexão com a internet durante a instalação para que o `pip` possa baixar e instalar as bibliotecas necessárias.

## Funções Implementadas

O projeto conta com as seguintes funções:

- `download_arquivo(url, destino)`: Realiza o download de um arquivo a partir de uma URL especificada. O arquivo é salvo no caminho de destino especificado.
- `zipar_arquivos(destino, arquivos)`: Cria um arquivo zip no caminho de destino especificado e adiciona os arquivos da lista fornecida ao arquivo zip.

## Como Utilizar

1. Clone o repositório para sua máquina local utilizando o seguinte comando:
```bash git clone https://github.com/MrGabrielBP/WebScraping.git```
2. Navegue para o diretório do projeto:
3. Defina a URL da página web que deseja acessar na variável `url`.
4. Execute o script Python e aguarde a conclusão.
```bash python codigo.py```
5. Os arquivos que correspondem ao padrão desejado serão baixados e salvos na pasta atual.
6. Após o download, os arquivos serão compactados em um arquivo zip com o destino especificados.
7. Verifique o arquivo zip gerado para acessar os arquivos baixados.

Tenha em mente que você pode personalizar o padrão utilizado para filtrar os links desejados ajustando a expressão regular na variável `padrao` no arquivo.

## Expressão Regular Utilizada

A expressão regular utilizada no projeto é:
```bash r'https://www\..+Anexo.+\.pdf'```

Essa expressão regular procura por links que comecem com "https://www.", tenham qualquer sequência de caracteres (`.+`), seguida da palavra "Anexo", novamente qualquer sequência de caracteres, e finalizem com a extensão ".pdf". Isso permite filtrar os links que contêm a palavra "Anexo" e terminam com ".pdf".

---

Este projeto é um exemplo básico de web scraping e manipulação de arquivos usando Python. Sinta-se à vontade para adaptar e expandir o código de acordo com suas necessidades.
