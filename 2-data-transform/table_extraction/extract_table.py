import pdfplumber
import os
import pandas as pd

diretorio_csvs = './csvs'
arquivo_saida = diretorio_csvs + '/rol_de_procedimentos_e_eventos_em_saude.csv'

def data_extraction():

    if not os.path.exists(diretorio_csvs):
        os.makedirs(diretorio_csvs)

    # Abrindo o PDF
    pdf = pdfplumber.open('../1-web-scraping/downloaded_pdfs/AnexoI.pdf')

    # Lista para armazenar os dados concatenados
    dados_concatenados = []

    # Iterando pelas páginas desejadas (da página 3 até a 180)
    for i in range(2, 180):
        pagina_pdf = pdf.pages[i]
        tabela = pagina_pdf.extract_table()

        if tabela:
            if i == 2:
                dados_concatenados.extend(tabela)
            else:
            # Ignorar a primeira linha (cabeçalho)
                dados_concatenados.extend(tabela[1:])

    # Fechando o PDF
    pdf.close()

    dados_processados = [[col.replace("\n", " ") if col else "" for col in linha] for linha in dados_concatenados]

    df = pd.DataFrame(dados_processados[1:], columns=dados_processados[0])

    df['OD'] = df['OD'].replace('OD', 'Seg. Odontológica')
    df['AMB'] = df['AMB'].replace('AMB', 'Seg. Ambulatorial')

    df.to_csv(arquivo_saida, index=False, encoding='utf-8')

    print(f'Arquivo CSV salvo como {arquivo_saida}')
