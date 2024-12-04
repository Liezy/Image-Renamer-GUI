import os
import random
import shutil
from PIL import Image
from datetime import datetime

def obter_data_criacao_imagem(imagem_path):
    """Obtém a data de criação da imagem através dos metadados EXIF."""
    try:
        img = Image.open(imagem_path)
        exif_data = img._getexif()
        for tag, value in exif_data.items():
            if tag == 36867:  # Tag para data de criação
                data_criacao = value
                return datetime.strptime(data_criacao, '%Y:%m:%d %H:%M:%S')
    except Exception as e:
        print(f"Erro ao obter metadados da imagem {imagem_path}: {e}")
        return None

def renomear_imagens(pasta_imagens, pasta_saida, log_path):
    """Renomeia as imagens, as move para a pasta de saída e cria um log."""
    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)

    with open(log_path, 'a') as log_file:
        for imagem_nome in os.listdir(pasta_imagens):
            imagem_path = os.path.join(pasta_imagens, imagem_nome)
            if os.path.isfile(imagem_path):
                data_criacao = obter_data_criacao_imagem(imagem_path)
                if data_criacao:
                    # Formata a data
                    data_formatada = data_criacao.strftime('%d.%m.%Y')
                    # Gera um número aleatório
                    numero_aleatorio = random.randint(1000, 9999)
                    # Novo nome da imagem
                    novo_nome = f"{data_formatada}_{numero_aleatorio}.jpg"
                    # Caminho de destino
                    caminho_destino = os.path.join(pasta_saida, novo_nome)

                    # Copia a imagem para a pasta de saída com o novo nome
                    shutil.copy(imagem_path, caminho_destino)

                    # Registra o nome antigo e o novo no log
                    log_file.write(f"{imagem_nome} -> {novo_nome}\n")
                    print(f"Imagem renomeada: {imagem_nome} -> {novo_nome}")

if __name__ == "__main__":
    pasta_imagens = "images"
    pasta_saida = "output"
    log_path = "logs/rename_log.txt"

    renomear_imagens(pasta_imagens, pasta_saida, log_path)
    