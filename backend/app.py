from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np

app = Flask(__name__)
CORS(app)

# Load trained model
model = joblib.load("model.joblib")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    road_roughness = float(data['road_roughness'])
    ambient_temp = float(data['ambient_temp'])
    speed = float(data['speed'])
    is_raining = int(data['is_raining'])

    features = np.array([[road_roughness, ambient_temp, speed, is_raining]])
    prediction = model.predict(features)[0]

    suspension_map = {0: 'Soft', 1: 'Normal', 2: 'Stiff'}
    ac_map = {0: 'Low', 1: 'Medium', 2: 'High'}
    tire_map = {0: 'No Change', 1: 'Increase', 2: 'Decrease'}
    speed_map = {0: 'Normal', 1: 'Reduce Speed'}

    result = {
        'suspension_setting': suspension_map[int(prediction[0])],
        'ac_level': ac_map[int(prediction[1])],
        'tire_pressure_adjust': tire_map[int(prediction[2])],
        'speed_limit_adjust': speed_map[int(prediction[3])]
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
