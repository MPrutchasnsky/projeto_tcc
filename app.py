import streamlit as st
from PIL import Image, ImageDraw

# Função para carregar a imagem
def carregar_imagem():
    uploaded_file = st.file_uploader("Carregue uma imagem", type=["png", "jpg", "jpeg"])
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Imagem carregada", use_column_width=True)
        return uploaded_file
    return None

# Função para desenhar o quadrante selecionado
def desenhar_quadrante(imagem, quadrante):
    # Obter as dimensões da imagem
    img = Image.open(imagem)
    largura, altura = img.size
    draw = ImageDraw.Draw(img)

    # Definir as coordenadas dos quadrantes
    if quadrante == "Superior Esquerdo":
        coordenadas = (0, 0, largura // 2, altura // 2)
    elif quadrante == "Superior Direito":
        coordenadas = (largura // 2, 0, largura, altura // 2)
    elif quadrante == "Inferior Esquerdo":
        coordenadas = (0, altura // 2, largura // 2, altura)
    elif quadrante == "Inferior Direito":
        coordenadas = (largura // 2, altura // 2, largura, altura)

    # Desenhar o retângulo
    draw.rectangle(coordenadas, outline="red", width=5)
    
    return img

def main():
    st.title("Sistema de Apoio ao Diagnóstico - Gamificado")

    imagem = carregar_imagem()

    if imagem:
        quadrante = st.radio("Escolha o quadrante que você acha suspeito:", 
                             ["Superior Esquerdo", "Superior Direito", "Inferior Esquerdo", "Inferior Direito"])

        if quadrante:
            img_destacada = desenhar_quadrante(imagem, quadrante)
            st.image(img_destacada, caption=f"Região suspeita: {quadrante}", use_column_width=True)

        st.sidebar.header("Instruções")
        st.sidebar.write("Selecione o quadrante que você acha que pode ter uma anomalia e a região será destacada.")

if __name__ == "__main__":
    main()
