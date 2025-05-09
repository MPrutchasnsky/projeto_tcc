import streamlit as st
from PIL import Image

# Função para carregar a imagem
def carregar_imagem():
    uploaded_file = st.file_uploader("Carregue uma imagem", type=["png", "jpg", "jpeg"])
    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        st.image(img, caption="Imagem carregada", use_column_width=True)
        return uploaded_file, img
    return None, None

# Função para definir a área de interesse
def selecionar_area(imagem):
    if imagem:
        st.sidebar.header("Seleção da área de interesse")
        
        # Ajustar coordenadas e tamanho da caixa
        width, height = imagem.size

        x1 = st.sidebar.slider("Posição X inicial", 0, width, 50)
        y1 = st.sidebar.slider("Posição Y inicial", 0, height, 50)
        x2 = st.sidebar.slider("Posição X final", x1, width, x1 + 100)
        y2 = st.sidebar.slider("Posição Y final", y1, height, y1 + 100)

        # Exibe os valores de coordenadas
        st.sidebar.write(f"Área selecionada: ({x1}, {y1}) -> ({x2}, {y2})")

        # Desenha a área sobre a imagem
        st.image(imagem.crop((x1, y1, x2, y2)), caption="Área selecionada", use_column_width=True)
        
        return (x1, y1, x2, y2)
    return None

# Função para iniciar a análise
def iniciar_analise(area):
    if area:
        st.success("Análise em andamento...")
        st.write("Resultado da análise: Nenhuma anomalia detectada.")
    else:
        st.warning("Por favor, selecione uma área de interesse.")

def main():
    st.title("Sistema de Apoio ao Diagnóstico - Gamificado")

    imagem, img_obj = carregar_imagem()
    if imagem:
        area = selecionar_area(img_obj)

        if st.button("Iniciar Análise"):
            iniciar_analise(area)

if __name__ == "__main__":
    main()
