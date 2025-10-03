from ultralytics import YOLO
import cv2

# Carrega o modelo
model = YOLO("D:/backuptcc/projeto_tcc/treinos_yolo/vindr2/weights/best.pt")

# Carrega uma imagem para testar
img_path = "D:/backuptcc/projeto_tcc/imagens/347b32bd628a543c96ba6baf027e9781.png"

# Faz a detecção
results = model(img_path)

# Mostra a imagem com as detecções
results[0].show()

# Salva a imagem com detecções (opcional)
results[0].save("D:/data/detectar/teste1_resultado.png")
