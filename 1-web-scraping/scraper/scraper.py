from bs4 import BeautifulSoup
import requests

html = requests.get("https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos").content
soup = BeautifulSoup(html, 'html.parser')

link_anexo1 = soup.find('a', {'data-mce-href': 'resolveuid/f710899c6c7a485ea62a1acc75d86c8c'}).get('href')
link_anexo2 = soup.find('a', {'data-mce-href': 'resolveuid/85adaa3de5464d8aadea11456bfb4f94'}).get('href')