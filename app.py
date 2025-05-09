import streamlit as st
from streamlit_image_coordinates import streamlit_image_coordinates
from PIL import Image

# Função para carregar imagem
def carregar_imagem():
    uploaded_file = st.file_uploader("Carregue uma imagem", type=["png", "jpg", "jpeg"])
    if uploaded_file is not None:
        imagem = Image.open(uploaded_file)
        return imagem
    return None

# Função principal
def main():
    st.title("Sistema de Apoio ao Diagnóstico - Gamificado")

    pontos = 0
    imagem = carregar_imagem()

    if imagem:
        st.subheader("Clique na imagem onde você acredita haver uma anomalia")
        coords = streamlit_image_coordinates(imagem, key="imagem")

        if coords is not None:
            st.success(f"Você clicou na posição: X={coords['x']}, Y={coords['y']}")
            pontos += 5

        if st.button("Iniciar Análise"):
            st.success("Análise em andamento...")
            st.write("Resultado da análise: Nenhuma anomalia detectada.")
            pontos += 10

    # Pontuação
    st.sidebar.header("Sua Pontuação")
    st.sidebar.write(f"Pontos: {pontos}")

if __name__ == "__main__":
    main()
