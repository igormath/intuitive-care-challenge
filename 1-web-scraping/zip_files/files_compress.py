import zipfile
import os

def compress():
    anexo1 = './downloaded_pdfs/AnexoI.pdf'
    anexo2 = './downloaded_pdfs/AnexoII.pdf'

    if not os.path.exists(anexo1) or not os.path.exists(anexo2):
        raise FileNotFoundError('Um ou mais arquivos PDF não foram encontrados.')
        

    zip_file = zipfile.ZipFile('downloaded_pdfs/Anexos.zip', 'w', zipfile.ZIP_DEFLATED)

    try:
        zip_file.write(anexo1, 'AnexoI.pdf')
        zip_file.write(anexo2, 'AnexoII.pdf')
        print('Arquivos PDF compactados com sucesso!')

    except FileNotFoundError as e:
        print(f'Houve um erro ao compactar os pdfs: {e}')
