from flask import Flask, render_template, request
from ocrmodel import extract_text_from_image
import cv2
import numpy as np
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if 'image' in request.files:
        image_file = request.files['image']
        image = cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), cv2.IMREAD_COLOR)
        r=extract_text_from_image(image)
        return "<h2>Extracted Text From Image: </h2>" + r


if __name__ == '__main__':
    app.run(debug=True)
