from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model and encoders
with open('model.pkl', 'rb') as file:
    model_data = pickle.load(file)
    model = model_data['model']
    le_day = model_data['le_day']
    le_month = model_data['le_month']


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form inputs
        temperature = float(request.form['temperature'])
        rainfall = float(request.form['rainfall'])
        day_of_week_num = int(request.form['day_of_week'])
        month_num = int(request.form['month'])
        
        # Map numeric inputs to day/month names
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        months = ['January', 'February', 'March', 'April', 'May', 'June', 
                  'July', 'August', 'September', 'October', 'November', 'December']
        
        day_of_week = days[day_of_week_num - 1]
        month = months[month_num - 1]
        
        # Encode categorical variables
        day_encoded = le_day.transform([day_of_week])[0]
        month_encoded = le_month.transform([month])[0]
        
        # Prepare features for prediction
        features = np.array([[temperature, rainfall, day_encoded, month_encoded]])
        
        # Make prediction
        prediction = model.predict(features)[0]
        prediction_text = f"🎉 Predicted Ice Creams Sold: {prediction:.2f} 🎉"
        
        return render_template('index.html', prediction_text=prediction_text)
    
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")


if __name__ == '__main__':
    app.run(debug=True)
