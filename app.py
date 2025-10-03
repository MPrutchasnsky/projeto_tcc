import streamlit as st
from PIL import Image, ImageDraw
import streamlit_image_coordinates

# Inicializa coordenadas na sessão
if "coordinates" not in st.session_state:
    st.session_state["coordinates"] = None

# Função para carregar a imagem
def carregar_imagem():
    uploaded_file = st.file_uploader("Carregue uma imagem", type=["png", "jpg", "jpeg"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Imagem carregada", use_container_width=True)
        return image
    return None

# Função para iniciar a análise
def iniciar_analise(subregion):
    if subregion is not None:
        st.success("Análise em andamento...")
        # Aqui você chamaria o modelo de IA usando 'subregion'
        st.write("Resultado da análise: Nenhuma anomalia detectada.")
        return True
    else:
        st.warning("Por favor, selecione uma sub-região antes de iniciar a análise.")
        return False

# Pontuação e feedback
def atualizar_pontuacao(pontos):
    st.sidebar.header("Sua Pontuação")
    st.sidebar.write(f"Pontos: {pontos}")

# Converte coordenadas da sessão para tupla de recorte
def get_rectangle_coords(coords):
    (x1, y1), (x2, y2) = coords
    return (min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2))

def main():
    st.title("Sistema de Apoio ao Diagnóstico - Gamificado")

    pontos = 0
    img = carregar_imagem()

    if img:
        draw = ImageDraw.Draw(img)

        # Desenha retângulo caso já exista
        if st.session_state["coordinates"]:
            coords = get_rectangle_coords(st.session_state["coordinates"])
            draw.rectangle(coords, fill=None, outline="red", width=2)

        # Colunas para interface
        cols = st.columns([1, 1, 4])
        with cols[0]:
            value = streamlit_image_coordinates.image_coordinates(img, key="rectangle", click_and_drag=True)

        # Atualiza coordenadas na sessão
        if value is not None:
            point1 = (value["x1"], value["y1"])
            point2 = (value["x2"], value["y2"])
            if (
                point1[0] != point2[0]
                and point1[1] != point2[1]
                and st.session_state["coordinates"] != (point1, point2)
            ):
                st.session_state["coordinates"] = (point1, point2)
                st.experimental_rerun()

        # Mostra sub-região recortada e ampliada
        if st.session_state["coordinates"]:
            coords = get_rectangle_coords(st.session_state["coordinates"])
            subregion = img.crop(coords)
            subregion = subregion.resize((int(subregion.width * 1.5), int(subregion.height * 1.5)))
            with cols[1]:
                st.image(subregion, use_column_width=False)

            # Botão de análise
            if st.button("Iniciar Análise"):
                if iniciar_analise(subregion):
                    pontos += 10

    atualizar_pontuacao(pontos)

    if pontos > 0:
        st.success(f"Parabéns! Você ganhou {pontos} pontos!")
    else:
        st.info("Carregue uma imagem e selecione uma área para começar a análise e ganhar pontos!")

if __name__ == "__main__":
    main()
