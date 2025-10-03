from ultralytics import YOLO
from ultralytics.utils.downloads import GITHUB_ASSETS_STEMS
GITHUB_ASSETS_STEMS
from ultralytics import YOLO, settings
settings
settings.update({'runs_dir': 'D:/treinos_yolo'})
settings


def main():
    model = YOLO("yolov8n.pt")

    model.train(
        data='D:/data/yolov8n_vindr.yaml',
        epochs=50,          # aumentei para 50 (treino mais estável, mas pode mudar)
        patience=10,        # espera mais antes de parar
        batch=8,            # reduzido para não travar em CPU (aumente se rodar liso)
        imgsz=640,
        workers=4,          # menos workers para evitar travamentos no Windows
        pretrained=True,
        resume=False,       
        single_cls=False,   
        project='D:/treinos_yolo',  # onde salvar
        name='vindr',              # subpasta fixa para esse dataset
        box=7.5,
        cls=0.5,
        dfl=1.5,
        val=True,
        degrees=0.3,
        hsv_s=0.3,
        hsv_v=0.3,
        scale=0.5,
        fliplr=0.5
    )
    metrics = model.val()

if __name__ == '__main__':
    main()
