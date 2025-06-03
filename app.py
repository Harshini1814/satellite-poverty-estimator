import os
import cv2
import numpy as np
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from tensorflow.keras.models import load_model
from tensorflow.keras import losses 
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB
app.secret_key = 'supersecretkey'

# Load model
model = load_model('wealth_index_model.h5', custom_objects={'mse': losses.MeanSquaredError()})

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg'}

def predict_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (64, 64)) / 255.0
    prediction = model.predict(np.array([img]))[0][0] * 100
    return round(prediction, 2)

def classify_wealth(index):
    if index < 20: return ('Very Poor', '#ff4757')
    elif index < 40: return ('Poor', '#ff7f50')
    elif index < 60: return ('Moderate', '#f1c40f')
    elif index < 80: return ('Wealthy', '#2ecc71')
    else: return ('Very Wealthy', '#27ae60')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'files' not in request.files:
        return redirect(url_for('home'))
    
    files = request.files.getlist('files')
    results = []
    
    for file in files[:10]:  # Limit to 10 files
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # Make prediction
            wealth_index = predict_image(filepath)
            class_name, class_color = classify_wealth(wealth_index)
            
            results.append({
                'filename': filename,
                'index': wealth_index,
                'class': class_name,
                'color': class_color
            })
    
    return render_template('results.html', predictions=results)

@app.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)