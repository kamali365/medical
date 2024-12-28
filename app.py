from flask import Flask, request, jsonify
import pickle
import numpy as np

# Load the model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json  # Expecting a JSON payload
    features = np.array([data['age'], data['bmi'], data['children']]).reshape(1, -1)
    prediction = model.predict(features)
    return jsonify({'prediction': float(prediction)})

if __name__ == '__main__':
    app.run(debug=True)
