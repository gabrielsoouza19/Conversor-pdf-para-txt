import PyPDF2
import os

def converte_pdf_para_txt(caminho_pasta):
    # Cria a subpasta "convertidos" dentro do caminho especificado
    pasta_convertidos = os.path.join(caminho_pasta, 'convertidos')
    os.makedirs(pasta_convertidos, exist_ok=True)

    # Lista os arquivos na pasta fornecida
    arquivos_pdf = [arquivo for arquivo in os.listdir(caminho_pasta) if arquivo.lower().endswith('.pdf')]

    for arquivo_pdf in arquivos_pdf:
        caminho_arquivo_pdf = os.path.join(caminho_pasta, arquivo_pdf)
        caminho_arquivo_txt = os.path.join(pasta_convertidos, f'{os.path.splitext(arquivo_pdf)[0]}.txt')

        texto = readpdf(caminho_arquivo_pdf)

        # Salva o texto extraído em um arquivo TXT
        with open(caminho_arquivo_txt, 'w', encoding='utf-8') as txt_file:
            txt_file.write(texto)

        print(f'{arquivo_pdf} convertido para {caminho_arquivo_txt}')

def readpdf(path):
    with open(path, 'rb') as aqv:
        ler_pdf = PyPDF2.PdfReader(aqv)

        full_text = ""
        for num in range(len(ler_pdf.pages)):
            page = ler_pdf.pages[num]
            text = page.extract_text()
            full_text += f"\n{text}\n"

        return full_text

if __name__ == "__main__":
    # Pergunta ao usuário o caminho da pasta
    caminho_pasta_usuario = input("Digite o caminho da pasta contendo os arquivos PDF: ")

    # Verifica se o caminho da pasta é válido
    if os.path.isdir(caminho_pasta_usuario):
        converte_pdf_para_txt(caminho_pasta_usuario)
        print("Conversão concluída.")
    else:
        print("Caminho inválido. Certifique-se de fornecer um caminho válido para a pasta.")