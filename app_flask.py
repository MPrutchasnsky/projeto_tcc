from flask import Flask, render_template
from PIL import Image
import os, random
from analise_flask import analisar_imagem

app = Flask(__name__)

IMAGE_FOLDER = "D:/backuptcc/tcc_flask/static/images"
OUTPUT_FOLDER = "D:/backuptcc/tcc_flask/static/output_images"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Lista global para controlar imagens já usadas
imagens_disponiveis = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/carregar")
def carregar():
    global imagens_disponiveis

    # carrega todas as imagens se a lista estiver vazia
    if not imagens_disponiveis:
        imagens_disponiveis = [
            img for img in os.listdir(IMAGE_FOLDER)
            if img.lower().endswith(('.png', '.jpg', '.jpeg'))
        ]
        random.shuffle(imagens_disponiveis)  # embaralha a ordem

    if not imagens_disponiveis:
        return "Nenhuma imagem encontrada em static/images", 500

    # pega a próxima imagem da lista (sem repetição até reset)
    filename = imagens_disponiveis.pop()
    filepath = os.path.join(IMAGE_FOLDER, filename)

    # roda análise
    img = Image.open(filepath)
    resumo, img_result = analisar_imagem(img)

    # salva resultado
    output_filename = f"result_{filename}"
    output_path = os.path.join(OUTPUT_FOLDER, output_filename)
    img_result.save(output_path)

    # renderiza template
    return render_template(
        "resultados.html",
        original=f"/static/images/{filename}",
        resultado=f"/static/output_images/{output_filename}",
        resumo=resumo
    )

if __name__ == "__main__":
    app.run(debug=True)
