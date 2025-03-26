import zipfile
import os
from table_extraction.extract_table import arquivo_saida

def compress():
    if not os.path.exists(arquivo_saida):
        raise FileNotFoundError('O arquivo CSV não foi encontrado.')
    
    zip_file = zipfile.ZipFile("Teste_Igor_Azevedo.zip", 'w', zipfile.ZIP_DEFLATED)

    try:
        zip_file.write(arquivo_saida, 'rol_de_procedimentos_e_eventos_em_saude.csv')
        print('Arquivo CSV compactado com sucesso!')
    except FileNotFoundError as e:
        print(f'Houve um erro ao compactar os pdfs: {e}')
