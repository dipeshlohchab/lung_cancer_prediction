from flask import Flask, render_template, request, jsonify
import numpy as np
import pickle

app = Flask(__name__)

# Load the trained model from a pickle file
with open("artifacts/model.pkl", "rb") as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    try:
        data = request.get_json()

        features = [
            int(data['AGE']),  # Ensure integer conversion
            1 if data['GENDER'] == 'male' else 0,
            1 if data['SMOKING'] == 'yes' else 0,
            1 if data['FINGER_DISCOLORATION'] == 'yes' else 0,
            1 if data['LEVEL'] == 'yes' else 0,
            1 if data['EXPOSURE_POL'] == 'yes' else 0,
            1 if data['LONG_TERM_ILLNESS'] == 'yes' else 0,
            int(data['ENERGY']),  # Ensure integer conversion
            1 if data['IMMUNE_WEAKNESS'] == 'yes' else 0,
            1 if data['BREATHING_ISSUE'] == 'yes' else 0,
            1 if data['ALCOHOL_CONSUMPTION'] == 'yes' else 0,
            1 if data['THROAT_DISCOMFORT'] == 'yes' else 0,
            float(data['OXYGEN_SATURATION']),  # Ensure float conversion
            1 if data['CHEST_TIGHTNESS'] == 'yes' else 0,
            1 if data['FAMILY_HISTORY'] == 'yes' else 0,
            1 if data['SMOKING_FAMILY_HISTORY'] == 'yes' else 0,
            1 if data['STRESS_IMMUNE'] == 'yes' else 0
        ]

        # Ensure the model exists
        if not model:
            return jsonify({'error': 'Model not loaded'}), 500

        prediction = model.predict([features])
        result = 'yes' if prediction[0] == 1 else 'no'

        return jsonify({'prediction': result})

    except KeyError as e:
        return jsonify({'error': f'Missing key: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)