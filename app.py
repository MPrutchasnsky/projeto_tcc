import streamlit as st
from PIL import Image
from streamlit_image_coordinates import st_image_coordinates

# Função para carregar a imagem
def carregar_imagem():
    uploaded_file = st.file_uploader("Carregue uma imagem", type=["png", "jpg", "jpeg"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Imagem carregada", use_container_width=True)
        return image
    return None

# Função para iniciar a análise
def iniciar_analise(imagem, coords):
    if imagem is not None and coords is not None:
        st.success("Análise em andamento...")
        
        x1, y1 = coords["x"], coords["y"]
        x2, y2 = coords["x"] + coords["width"], coords["y"] + coords["height"]
        st.write(f"Área selecionada pelo usuário: ({x1}, {y1}) -> ({x2}, {y2})")
        
        # Aqui você integraria o modelo de IA e compararia com a seleção do usuário
        st.write("Resultado da análise: Nenhuma anomalia detectada.")
        return True
    else:
        st.warning("Por favor, carregue a imagem e selecione uma área antes de iniciar a análise.")
        return False

# Pontuação e feedback
def atualizar_pontuacao(pontos):
    st.sidebar.header("Sua Pontuação")
    st.sidebar.write(f"Pontos: {pontos}")

def main():
    st.title("Sistema de Apoio ao Diagnóstico - Gamificado")

    pontos = 0  # Inicializando a pontuação

    # Carregar imagem
    imagem = carregar_imagem()

    coords = None
    if imagem:
        st.subheader("Selecione uma área na imagem")
        coords = st_image_coordinates(imagem, key="image_coords")

        # Botão de análise
        if st.button("Iniciar Análise"):
            if iniciar_analise(imagem, coords):
                pontos += 10

    # Exibe a pontuação
    atualizar_pontuacao(pontos)

    # Mensagem motivacional
    if pontos > 0:
        st.success(f"Parabéns! Você ganhou {pontos} pontos!")
    else:
        st.info("Carregue uma imagem e selecione uma área para começar a análise e ganhar pontos!")

if __name__ == "__main__":
    main()
