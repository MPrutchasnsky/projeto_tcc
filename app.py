import streamlit as st
from ultralytics import YOLO
from PIL import Image

# carregue seu modelo treinado (ajuste o caminho do .pt)
model = YOLO("D:/backuptcc/projeto_tcc/modelo/best.pt")

st.title("Sistema de Apoio ao Diagnóstico")
st.write("Carregue uma imagem e o modelo irá detectar possíveis anomalias.")

# Upload de imagem
uploaded_file = st.file_uploader("Carregar imagem", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # abrir a imagem
    img = Image.open(uploaded_file).convert("RGB")
    st.image(img, caption="Imagem Original", use_container_width=True)

    # botão para rodar a análise
    if st.button("Analisar"):
        with st.spinner("Analisando a imagem..."):
            # roda o modelo
            results = model.predict(img)

            # mostra resultados
            for r in results:
                st.write(f"**Detecções:** {len(r.boxes)}")
                for box in r.boxes:
                    cls = int(box.cls[0])
                    conf = float(box.conf[0])
                    st.write(f"- {model.names[cls]} ({conf:.2f})")

                # renderiza imagem anotada
                annotated = r.plot()  # numpy array com caixas desenhadas
                st.image(annotated, caption="Detecções do Modelo", use_container_width=True)
