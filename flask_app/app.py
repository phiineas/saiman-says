from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

import os

# Get the absolute path to the model file
model_path = os.path.join(os.path.dirname(__file__), 'model', 'best_rf.pkl')
scaler_path = os.path.join(os.path.dirname(__file__), 'model', 'scaler.pkl')

# Load the trained model and scaler
model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

# Selected features (from the notebook)
# selected_features = ['rank', 'subscribers', 'video_views_rank', 'video_views_for_the_last_30_days', 'lowest_monthly_earnings', 'highest_monthly_earnings', 'lowest_yearly_earnings', 'highest_yearly_earnings', 'views_per_upload']  # Replace with your features

selected_features = ['rank', 'subscribers', 'video_views_for_the_last_30_days', 'lowest_monthly_earnings', 'highest_monthly_earnings', 'lowest_yearly_earnings', 'highest_yearly_earnings', 'views_per_upload']  # Replace with your features


@app.route('/')
def index():
    return render_template('index.html', features=selected_features)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract input values
        input_data = [float(request.form[feature]) for feature in selected_features]
        input_scaled = scaler.transform([input_data])  # Scale input data

        # Predict using the model
        prediction = model.predict(input_scaled)[0] / 100

        # Get feature importance
        feature_importances = model.feature_importances_
        importance_dict = {feature: round(importance, 4) for feature, importance in zip(selected_features, feature_importances)}

        return render_template('result.html', prediction=round(prediction, ), importances=importance_dict)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
