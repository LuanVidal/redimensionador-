import os
from PIL import Image
from tqdm import tqdm

def resize_images(input_folder, output_folder, size=(
        
        ,
)):
    # Verifica se a pasta de saída existe, senão a cria
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Lista todos os arquivos na pasta de entrada
    files = os.listdir(input_folder)
    # Filtra apenas os arquivos .jpg
    jpg_files = [f for f in files if f.endswith('.jpg')]

    # Cria uma barra de progresso para acompanhar o processo
    progress_bar = tqdm(total=len(jpg_files), desc='Redimensionando imagens')

    # Loop através de cada arquivo .jpg na pasta de entrada
    for filename in jpg_files:
        # Caminho do arquivo de entrada
        input_path = os.path.join(input_folder, filename)
        # Caminho do arquivo de saída (mesmo nome, mas na pasta de saída)
        output_path = os.path.join(output_folder, filename)

        # Abre a imagem
        image = Image.open(input_path)
        # Redimensiona a imagem
        resized_image = image.resize(size)
        # Salva a imagem redimensionada na pasta de saída
        resized_image.save(output_path)

        # Atualiza a barra de progresso
        progress_bar.update(1)

    # Fecha a barra de progresso
    progress_bar.close()

# Exemplo de uso
if __name__ == "__main__":
    input_folder = 'D:/FIAT/Produto NOK/work cam 2'
    output_folder = 'C:/Users/io/Documents/PROJECTS_PYTHON/conversor_de_imagem/img_redimencionada'
    resize_images(input_folder, output_folder)