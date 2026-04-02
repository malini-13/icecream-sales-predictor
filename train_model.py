import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import pickle

# Load dataset
df = pd.read_csv('ice-cream.csv')

# Define all possible month and day names
all_months = ['January', 'February', 'March', 'April', 'May', 'June', 
              'July', 'August', 'September', 'October', 'November', 'December']
all_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Select features and target
X = df[['Temperature', 'Rainfall', 'DayOfWeek', 'Month']]
y = df['IceCreamsSold']

# Create and fit LabelEncoders with ALL possible values
le_day = LabelEncoder()
le_month = LabelEncoder()

# Fit encoders with all possible values to handle any input
le_day.fit(all_days)
le_month.fit(all_months)

# Transform the training data
X['DayOfWeek'] = le_day.transform(X['DayOfWeek'])
X['Month'] = le_month.transform(X['Month'])

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
