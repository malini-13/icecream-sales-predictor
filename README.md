# Ice Cream Sales Predictor 🍦💗

A machine learning web application that predicts ice cream sales based on weather conditions and day/month information.

## Features ✨

- 🤖 Linear Regression model trained on historical ice cream sales data
- 🌐 Beautiful baby pink themed web interface
- 📊 Predicts ice cream sales based on:
  - Temperature (°F)
  - Rainfall (inches)
  - Day of Week (1-7)
  - Month (1-12)
- 💗 Cute and playful UI with emojis

## Project Structure 📁

```
Ice-Cream Sales Predictor/
├── ice-cream.csv           # Training dataset
├── train_model.py          # Model training script
├── model.pkl               # Trained model (generated)
├── app.py                  # Flask web application
├── requirements.txt        # Python dependencies
├── README.md               # This file
├── templates/
│   └── index.html          # Web interface
└── static/
    └── style.css           # Cute pink styling
```

## Installation 🚀

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Local Setup

1. **Clone or navigate to the project directory:**
   ```bash
   cd "Ice-Cream Sales Predictor"
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv .venv
   ```

3. **Activate virtual environment:**
   - **Windows:**
     ```bash
     .venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage 🍨

### Train the Model
```bash
python train_model.py
```
This will:
- Load the ice cream sales dataset from `ice-cream.csv`
- Train a Linear Regression model
- Save the trained model and encoders to `model.pkl`

### Run the Web Application
```bash
python app.py
```
The application will start in debug mode at `http://127.0.0.1:5000/`

Open your browser and navigate to the URL to use the predictor!

## Deployment 🌍

### Deployment on Render

1. **Create a Render account** at [render.com](https://render.com)

2. **Push your code to GitHub**

3. **Create a new Web Service on Render:**
   - Connect your GitHub repository
   - Configure the following:
     - **Build Command:** `pip install -r requirements.txt`
     - **Start Command:** `gunicorn app:app`
     - **Environment:** Python

4. **Deploy** and your app will be live!

### Alternative Deployment Options
- Heroku (with Procfile)
- AWS Elastic Beanstalk
- Google Cloud Run
- Azure App Service

## Dataset Information 📊

The model is trained on `ice-cream.csv` containing:
- **Date:** Date of observation
- **DayOfWeek:** Day of the week (Monday-Sunday)
- **Month:** Month name (January-December)
- **Temperature:** Temperature in Fahrenheit
- **Rainfall:** Rainfall in inches
- **IceCreamsSold:** Number of ice creams sold (target variable)

Features used for prediction:
- Temperature
- Rainfall
- DayOfWeek
- Month

## Technologies Used 🛠️

- **Backend:** Flask, Python
- **ML Framework:** scikit-learn
- **Data Processing:** pandas, numpy
- **Frontend:** HTML5, CSS3
- **Deployment:** Gunicorn, Render

## Model Information 🤖

- **Algorithm:** Linear Regression
- **Input Features:** 4 (Temperature, Rainfall, DayOfWeek, Month)
- **Output:** Predicted number of ice creams sold
- **Encoding:** LabelEncoder for categorical variables (DayOfWeek, Month)

## How It Works 🔧

1. User enters weather conditions and day/month information
2. Form submits POST request to `/predict` endpoint
3. Flask converts numeric inputs to day/month names
4. Categorical variables are encoded using saved LabelEncoders
5. Linear Regression model makes prediction
6. Result is displayed on the cute pink themed page

## Troubleshooting 🔍

### Model not found error
- Run `python train_model.py` to train the model first

### Port 5000 already in use
- Change the port in app.py: `app.run(debug=True, port=5001)`

### Import errors
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Verify virtual environment is activated

## Credits 💖

Made with 💗 for Ice Cream Lovers 🍦

## License 📄

This project is open source and available for personal and educational use.

---

Enjoy predicting ice cream sales! 🍨✨
