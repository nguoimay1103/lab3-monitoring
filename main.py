from fastapi import FastAPI, UploadFile, File
from prometheus_fastapi_instrumentator import Instrumentator
from predictor import predict_image
from PIL import Image
import io
import logging
import os

app = FastAPI()

# Cấu hình logging
logging.basicConfig(filename='/app/app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Thêm Prometheus instrumentation
instrumentator = Instrumentator(
    should_group_status_codes=True,
    should_ignore_untemplated=True,
    should_respect_env_var=False,
    should_instrument_requests_inprogress=True
)
instrumentator.instrument(app).expose(app)

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    logging.info("Received request for prediction")
    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents)).convert("RGB")
        pred_class = predict_image(image)
        logging.info(f"Predicted class: {pred_class}")
        return {"predicted_class": pred_class}
    except Exception as e:
        logging.error(f"Error during prediction: {str(e)}")
        raise