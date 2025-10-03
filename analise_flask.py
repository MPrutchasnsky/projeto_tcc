from ultralytics import YOLO
import cv2
from PIL import Image, ImageDraw

# Carrega o modelo YOLO treinado
model = YOLO("D:/backuptcc/projeto_tcc/modelo/best.pt")

def analisar_imagem(img):
    # Executa a predição no YOLO
    results = model(img)
    r = results[0]

    # Converte imagem original para PIL
    im_pil = Image.fromarray(cv2.cvtColor(r.orig_img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(im_pil, "RGBA")

    # Desenha bounding boxes manualmente
    for box in r.boxes.xyxy:  # cada box tem [x1, y1, x2, y2]
        x1, y1, x2, y2 = box.tolist()
        # Borda vermelha grossa
        draw.rectangle([x1, y1, x2, y2], outline="red", width=6)
        # Preenchimento leve (vermelho transparente)
        draw.rectangle([x1, y1, x2, y2], fill=(255, 0, 0, 60))

    # Resumo textual
    resumo = f"Detectadas {len(r.boxes)} anomalias"

    return resumo, im_pil
