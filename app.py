import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image

def main():
    st.title("Sistema de Apoio ao Diagnóstico - Gamificado")

    # Upload da imagem
    uploaded_file = st.file_uploader("Carregue uma imagem", type=["png", "jpg", "jpeg"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Imagem carregada", use_container_width=True)


        # Criar canvas para o usuário desenhar
        st.subheader("Marque a região suspeita na imagem:")
        canvas_result = st_canvas(
            fill_color="rgba(255, 0, 0, 0.3)",  # cor do preenchimento
            stroke_width=3,
            stroke_color="red",
            background_image=image,
            update_streamlit=True,
            height=image.height if image.height < 800 else 800,
            width=image.width if image.width < 800 else 800,
            drawing_mode="rect",  # pode ser "rect", "circle", "freedraw"
            key="canvas",
        )

        # Quando o usuário terminar de desenhar
        if st.button("Comparar com IA"):
            if canvas_result.json_data is not None:
                user_shapes = canvas_result.json_data["objects"]
                if user_shapes:
                    st.success(f"Você desenhou {len(user_shapes)} região(ões).")
                    
                    # Aqui entra sua IA: carregar modelo e fazer predição
                    st.write("Rodando IA...")
                    # Exemplo fictício de bounding box da IA
                    ai_bbox = [50, 50, 150, 150]  # xmin, ymin, xmax, ymax
                    
                    # Recupera primeira região desenhada pelo usuário
                    user_bbox = user_shapes[0]["left"], user_shapes[0]["top"], \
                                user_shapes[0]["left"]+user_shapes[0]["width"], \
                                user_shapes[0]["top"]+user_shapes[0]["height"]
                    
                    st.write(f"Região do usuário: {user_bbox}")
                    st.write(f"Região da IA: {ai_bbox}")

                    # Exemplo: cálculo de interseção (IoU simplificado)
                    iou = calcular_iou(ai_bbox, user_bbox)
                    st.write(f"IoU entre usuário e IA: {iou:.2f}")

                    if iou > 0.5:
                        st.success("Parabéns, sua marcação está muito próxima da IA!")
                    else:
                        st.warning("A marcação da IA está em outra região.")
                else:
                    st.warning("Nenhuma região foi desenhada.")
            else:
                st.warning("Nenhuma anotação recebida do canvas.")

def calcular_iou(boxA, boxB):
    # boxA e boxB = (xmin, ymin, xmax, ymax)
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    xB = min(boxA[2], boxB[2])
    yB = min(boxA[3], boxB[3])

    interArea = max(0, xB - xA) * max(0, yB - yA)
    boxAArea = (boxA[2] - boxA[0]) * (boxA[3] - boxA[1])
    boxBArea = (boxB[2] - boxB[0]) * (boxB[3] - boxB[1])
    iou = interArea / float(boxAArea + boxBArea - interArea)
    return iou

if __name__ == "__main__":
    main()
