import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import io

# Função para carregar a imagem
def carregar_imagem():
    uploaded_file = st.file_uploader("Carregue uma imagem", type=["png", "jpg", "jpeg"])
    if uploaded_file is not None:
        imagem = Image.open(uploaded_file)
        st.image(imagem, caption="Imagem carregada", use_column_width=True)
        return imagem, uploaded_file
    return None, None

# Função para iniciar a análise
def iniciar_analise(imagem):
    if imagem is not None:
        st.success("Análise em andamento...")
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

    imagem, uploaded_file = carregar_imagem()

    if imagem:
        st.subheader("Delimite a área suspeita:")
        canvas_result = st_canvas(
            fill_color="rgba(255, 0, 0, 0.3)",  # Cor do preenchimento do retângulo
            stroke_width=3,
            background_image=imagem,
            update_streamlit=True,
            height=500,
            drawing_mode="rect",
            key="canvas"
        )

        if st.button("Iniciar Análise"):
            if iniciar_analise(imagem):
                pontos += 10

    atualizar_pontuacao(pontos)

    if pontos > 0:
        st.success(f"Parabéns! Você ganhou {pontos} pontos!")
    else:
        st.info("Carregue uma imagem e delimite a área suspeita para começar!")

if __name__ == "__main__":
    main()
