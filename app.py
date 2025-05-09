import streamlit as st
from PIL import Image, ImageDraw
import io

# Função para carregar a imagem
def carregar_imagem():
    uploaded_file = st.file_uploader("Carregue uma imagem", type=["png", "jpg", "jpeg"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption="Imagem carregada", use_column_width=True)
        return image
    return None

# Função para desenhar retângulo na imagem
def marcar_area(image, x, y, largura, altura):
    img_copy = image.copy()
    draw = ImageDraw.Draw(img_copy)
    draw.rectangle([x, y, x + largura, y + altura], outline="red", width=3)
    return img_copy

# Função para iniciar a análise
def iniciar_analise():
    st.success("Análise em andamento...")
    st.write("Resultado da análise: Área suspeita identificada.")
    return True

# Pontuação e feedback
def atualizar_pontuacao(pontos):
    st.sidebar.header("Sua Pontuação")
    st.sidebar.write(f"Pontos: {pontos}")

def main():
    st.title("Sistema de Apoio ao Diagnóstico - Gamificado")

    pontos = 0  # Pontuação inicial

    imagem = carregar_imagem()

    if imagem:
        st.subheader("Delimite a área suspeita")
        x = st.number_input("Coordenada X", min_value=0, value=50)
        y = st.number_input("Coordenada Y", min_value=0, value=50)
        largura = st.number_input("Largura da área", min_value=1, value=100)
        altura = st.number_input("Altura da área", min_value=1, value=100)

        if st.button("Confirmar seleção e iniciar análise"):
            imagem_marcada = marcar_area(imagem, x, y, largura, altura)
            st.image(imagem_marcada, caption="Área marcada", use_column_width=True)

            if iniciar_analise():
                pontos += 10

    atualizar_pontuacao(pontos)

    if pontos > 0:
        st.success(f"Parabéns! Você ganhou {pontos} pontos!")
    else:
        st.info("Carregue uma imagem e marque uma área para começar!")

if __name__ == "__main__":
    main()
