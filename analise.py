from PIL import Image
import torch
from ultralytics import YOLO  # Certifique-se que ultralytics está no requirements

# Carregar o modelo
# Coloque seu modelo YOLO dentro da pasta 'modelo' com o nome 'best.pt'
modelo_path = "D:/backuptcc/projeto_tcc/modelo/best.pt"
modelo = YOLO(modelo_path)

def analisar_imagem(imagem: Image.Image):
    """
    Recebe uma imagem PIL e retorna o resultado da análise do modelo.
    """
    # Converte para RGB caso não esteja
    if imagem.mode != "RGB":
        imagem = imagem.convert("RGB")

    # Faz a predição
    results = modelo.predict(source=imagem, conf=0.5, verbose=False)  # ajusta confiança se quiser
    resultados_texto = []

    for result in results:
        for box in result.boxes:
            cls = int(box.cls[0])
            conf = float(box.conf[0])
            resultados_texto.append(f"Classe {cls} com confiança {conf:.2f}")

    if not resultados_texto:
        return "Nenhuma anomalia detectada."
    
    return "\n".join(resultados_texto)

def recortar_regiao(imagem: Image.Image, coords: tuple):
    """
    Recorta a região da imagem baseada nas coordenadas (x1, y1, x2, y2)
    """
    return imagem.crop(coords)
