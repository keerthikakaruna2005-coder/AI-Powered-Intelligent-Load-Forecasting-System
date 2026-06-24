import joblib
import pandas as pd

model = joblib.load("models/load_forecast_model.pkl")

data = pd.DataFrame({
    'Hour':[15],
    'Temperature':[35],
    'Humidity':[70],
    'Previous_Load':[180]
})

prediction = model.predict(data)

print("Predicted Load:",prediction[0])