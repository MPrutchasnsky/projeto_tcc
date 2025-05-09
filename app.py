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

# Função para selecionar áreas com checkboxes
def selecionar_area_com_checkbox(imagem):
    if imagem:
        st.sidebar.header("Seleção da área de interesse")
        
        # Ajustar coordenadas e tamanho da caixa
        width, height = imagem.size

        # Definir algumas áreas de exemplo para o usuário escolher
        areas = [
            {"nome": "Canto Superior Esquerdo", "x1": 0, "y1": 0, "x2": 150, "y2": 150},
            {"nome": "Centro Superior", "x1": width//3, "y1": 0, "x2": width//3*2, "y2": 150},
            {"nome": "Canto Inferior Direito", "x1": width-150, "y1": height-150, "x2": width, "y2": height},
            {"nome": "Centro Inferior", "x1": width//3, "y1": height//3*2, "x2": width//3*2, "y2": height},
        ]
        
        selected_areas = []
        
        for area in areas:
            if st.sidebar.checkbox(area["nome"]):
                selected_areas.append(area)
        
        # Se alguma área for selecionada, desenha as áreas na imagem
        if selected_areas:
            for area in selected_areas:
                imagem_crop = imagem.crop((area["x1"], area["y1"], area["x2"], area["y2"]))
                st.image(imagem_crop, caption=f"{area['nome']} selecionada", use_column_width=True)
                
        return selected_areas
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
        areas_selecionadas = selecionar_area_com_checkbox(img_obj)

        if st.button("Iniciar Análise"):
            iniciar_analise(areas_selecionadas)

if __name__ == "__main__":
    main()
