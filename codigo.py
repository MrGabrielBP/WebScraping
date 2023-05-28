import requests
from bs4 import BeautifulSoup
import re
import zipfile

# Função para realizar o download de um arquivo a partir de uma URL
def download_arquivo(url, destino):
  response = requests.get(url)
  if response.status_code == 200:
    with open(destino, mode='wb') as arquivo:
      arquivo.write(response.content)

# Função para zipar uma lista de arquivos
def zipar_arquivos(destino, arquivos):
  with zipfile.ZipFile(destino, 'w', zipfile.ZIP_DEFLATED) as arquivozip:
    for arquivo in arquivos:
      arquivozip.write(arquivo, arquivo)

# URL da página web a ser acessada
url = 'https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/o-que-e-o-rol-de-procedimentos-e-evento-em-saude'

# Realiza a requisição GET para obter o conteúdo da página
response = requests.get(url)

# Padrão para filtrar os links desejados (links que contenham 'Anexo' e terminem com '.pdf')
padrao = r'https://www\..+Anexo.+\.pdf'

if response.status_code == 200:
  # Parseia o conteúdo HTML utilizando o BeautifulSoup
  soup = BeautifulSoup(response.content, 'html.parser')

  # Encontra todos os elementos 'a' que contêm os links
  links = soup.find_all('a')

  # Lista para armazenar os nomes dos arquivos que serão baixados
  nome_dos_arquivos = []

  # Itera sobre os links encontrados
  for l in links:
    # Obtém o atributo 'href' do elemento 'a'
    href = l.get('href')

    # Verifica se o link corresponde ao padrão desejado
    if re.search(padrao, href):
      # Define o destino do arquivo como o texto dentro do elemento 'a' seguido de '.pdf'
      destino = l.string + '.pdf'

      # Adiciona o nome do arquivo à lista
      nome_dos_arquivos.append(destino)

      # Realiza o download do arquivo a partir do link
      download_arquivo(href, destino)

# Chama a função para zipar os arquivos baixados
zipar_arquivos('Teste 1.zip', nome_dos_arquivos)