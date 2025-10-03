import streamlit as st
from PIL import Image
from ultralytics import YOLO

# Carregar o modelo YOLOv8 treinado
@st.cache_resource  # para não recarregar toda vez que interagir com o app
def carregar_modelo(caminho_modelo):
    model = YOLO(caminho_modelo)
    return model

# Função para carregar a imagem
def carregar_imagem():
    uploaded_file = st.file_uploader("Carregue uma imagem", type=["png", "jpg", "jpeg"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Imagem carregada", use_container_width=True)
        return image
    return None

# Função para iniciar a análise
def iniciar_analise(modelo, imagem):
    if imagem is not None:
        st.success("Análise em andamento...")
        
        # Converte a imagem para RGB (caso não esteja)
        if imagem.mode != "RGB":
            imagem = imagem.convert("RGB")
        
        # Rodar a predição do YOLO
        results = modelo.predict(source=imagem, save=False)  # Não salva a imagem
        r = results[0]
        
        # Mostrar os resultados no Streamlit
        if len(r.boxes) > 0:
            st.write(f"Anomalias detectadas: {len(r.boxes)}")
            for i, box in enumerate(r.boxes):
                xyxy = box.xyxy[0].tolist()  # [x_min, y_min, x_max, y_max]
                conf = float(box.conf[0])
                cls = int(box.cls[0])
                st.write(f"Anomalia {i+1}: Classe {cls}, Confiança {conf:.2f}, Box {xyxy}")
        else:
            st.write("Resultado da análise: Nenhuma anomalia detectada.")
        return True
    else:
        st.warning("Por favor, carregue uma imagem antes de iniciar a análise.")
        return False

# Pontuação e feedback
def atualizar_pontuacao(pontos):
    st.sidebar.header("Sua Pontuação")
    st.sidebar.write(f"Pontos: {pontos}")

def main():
    st.title("Sistema de Apoio ao Diagnóstico - Gamificado")

    pontos = 0  # Inicializando a pontuação

    # Carregar modelo
    modelo = carregar_modelo("D:/backuptcc/projeto_tcc/treinos_yolo/vindr2/weights/best.pt")  # substitua pelo caminho real

    # Carregar imagem
    imagem = carregar_imagem()

    if imagem:
        if st.button("Iniciar Análise"):
            if iniciar_analise(modelo, imagem):
                pontos += 10  # Incrementa pontos após análise bem-sucedida

    # Exibe a pontuação
    atualizar_pontuacao(pontos)

    # Mensagem motivacional
    if pontos > 0:
        st.success(f"Parabéns! Você ganhou {pontos} pontos!")
    else:
        st.info("Carregue uma imagem para começar a análise e ganhar pontos!")

if __name__ == "__main__":
    main()
