import streamlit as st

st.set_page_config(page_title="Análise de Imagens Médicas", layout="wide")

st.title("Sistema de Apoio ao Diagnóstico")
st.write("Bem-vindo ao sistema de análise de imagens mamográficas!")

# Simula upload de imagem
uploaded_file = st.file_uploader("Faça upload de uma imagem", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Imagem enviada", use_column_width=True)
    st.success("Imagem carregada com sucesso!")

    # Aqui você pode futuramente chamar o modelo de IA para fazer análise
    # resultado = seu_modelo.predict(uploaded_file)
    # st.write("Resultado:", resultado)
