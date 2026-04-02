import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import pickle

# Load dataset
df = pd.read_csv('ice-cream.csv')

# Select features and target
X = df[['Temperature', 'Rainfall', 'DayOfWeek', 'Month']]
y = df['IceCreamsSold']

# Encode categorical variables
le_day = LabelEncoder()
le_month = LabelEncoder()

X['DayOfWeek'] = le_day.fit_transform(X['DayOfWeek'])
X['Month'] = le_month.fit_transform(X['Month'])

# Train Linear Regression model
model = LinearRegression()
model.fit(X, y)

# Save the trained model with encoders
model_data = {
    'model': model,
    'le_day': le_day,
    'le_month': le_month
}

with open('model.pkl', 'wb') as file:
    pickle.dump(model_data, file)

print("Model trained successfully")
