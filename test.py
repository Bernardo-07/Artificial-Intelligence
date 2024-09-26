import pandas as pd

def create_image_percentage_dict(csv_path):
    df = pd.read_csv(csv_path)
    
    # Dicionário para armazenar os caminhos das imagens e seus respectivos valores
    image_percentage_dict = {}
    
    for index, row in df.iterrows():
        image_name = row[0]  # Nome da imagem da primeira coluna
        percentage_value = row[4]  # Valor da quinta coluna
        image_percentage_dict[image_name] = percentage_value
        
    return image_percentage_dict

csv_path = 'D:\Documents\Mecatrônica\LTAD\Arquivos-csv\Banco de Dados CSV.csv'  # Substitua pelo caminho do seu CSV

image_percentage_dict = create_image_percentage_dict(csv_path)

print(image_percentage_dict)
