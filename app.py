import streamlit as st
from PIL import Image
from analise import analisar_imagem, recortar_regiao

def main():
    st.title("Sistema de Apoio ao Diagnóstico")

    uploaded_file = st.file_uploader("Carregue uma imagem", type=["png", "jpg", "jpeg"])
    if uploaded_file:
        img = Image.open(uploaded_file)
        st.image(img, caption="Imagem carregada", use_container_width=True)

        coords_input = st.text_input("Digite coords x1,y1,x2,y2", "0,0,100,100")
        coords = tuple(map(int, coords_input.split(",")))
        recorte = recortar_regiao(img, coords)
        st.image(recorte, caption="Região selecionada")

        if st.button("Analisar"):
            resultado = analisar_imagem(recorte)
            st.success(f"Resultado: {resultado}")

if __name__ == "__main__":
    main()
