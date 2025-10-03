import streamlit as st
from PIL import Image
from streamlit_drawable_canvas import st_canvas  # canvas desenhável

# Função para carregar a imagem
def carregar_imagem():
    uploaded_file = st.file_uploader("Carregue uma imagem", type=["png", "jpg", "jpeg"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Imagem carregada", use_container_width=True)
        return image
    return None

# Função para iniciar a análise
def iniciar_analise(imagem, desenho):
    if imagem is not None:
        st.success("Análise em andamento...")
        
        # Aqui você integraria o modelo de IA
        # Exemplo de simulação de análise:
        if desenho is not None:
            st.write("Região desenhada pelo usuário detectada!")
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

    # Carregar imagem
    imagem = carregar_imagem()

    desenho = None
    if imagem:
        st.subheader("Desenhe sobre a imagem")
        # Cria o canvas com a imagem de fundo
        canvas_result = st_canvas(
            background_image=imagem,
            height=500,
            width=500,
            stroke_width=3,
            stroke_color="red",
            drawing_mode="freedraw",
            key="canvas",
        )
        desenho = canvas_result.image_data  # matriz RGBA do desenho

        # Botão de análise
        if st.button("Iniciar Análise"):
            if iniciar_analise(imagem, desenho):
                pontos += 10  # Incrementa pontos após análise bem-sucedida

    # Exibe a pontuação
    atualizar_pontuacao(pontos)

    # Mensagem motivacional
    if pontos > 0:
        st.success(f"Parabéns! Você ganhou {pontos} pontos!")
    else:
        st.info("Carregue uma imagem e desenhe sobre ela para começar a análise e ganhar pontos!")

if __name__ == "__main__":
    main()
