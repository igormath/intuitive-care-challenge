from scraper.scraper import link_anexo1, link_anexo2
import requests
import os

def pdfs_get():
    try:
        response_anexo1 = requests.get(link_anexo1, stream=True)
        response_anexo2 = requests.get(link_anexo2, stream=True)

        if not os.path.exists('./downloaded_pdfs'):
            os.makedirs('./downloaded_pdfs')
        
        with open('./downloaded_pdfs/AnexoI.pdf', 'wb') as pdf_file:
            for chunk in response_anexo1.iter_content(chunk_size=8192):
                pdf_file.write(chunk)

        with open('./downloaded_pdfs/AnexoII.pdf', 'wb') as pdf_file:
            for chunk in response_anexo2.iter_content(chunk_size=8192):
                pdf_file.write(chunk)

        print('Os PDFs foram baixados com sucesso!')

    except requests.exceptions.RequestException as e:
        print(f'Houve um erro ao baixar o pdf: {e}')
    except IOError as e:
        print(f'Houve um erro ao salvar o arquivo: {e}')
