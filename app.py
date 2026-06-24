import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Smart Load Forecasting",
    page_icon="⚡",
    layout="wide"
)

model = joblib.load("load_forecast_model.pkl")

st.title("⚡ AI-Powered Intelligent Load Forecasting System")

st.markdown("""
Predict future electrical load demand for smart distribution networks.
""")

col1, col2 = st.columns(2)

with col1:
    hour = st.slider("Hour", 1, 24, 12)
    temp = st.slider("Temperature (°C)", 20, 50, 30)

with col2:
    humidity = st.slider("Humidity (%)", 40, 90, 60)
    prev_load = st.number_input("Previous Load (kW)", value=150)

if st.button("Forecast Load"):

    input_data = pd.DataFrame({
        "Hour":[hour],
        "Temperature":[temp],
        "Humidity":[humidity],
        "Previous_Load":[prev_load]
    })

    prediction = model.predict(input_data)[0]

    st.success(f"Predicted Load Demand: {prediction:.2f} kW")

    if prediction > 180:
        st.warning("⚠ Peak Demand Expected")

        st.write("### Recommended Actions")
        st.write("• Shift non-critical loads")
        st.write("• Utilize battery storage")
        st.write("• Enable demand response")

    else:
        st.info("✅ Normal Operating Condition")
