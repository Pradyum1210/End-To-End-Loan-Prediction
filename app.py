import streamlit as st
import pandas as pd
import numpy as np
import pickle


# Page Config

st.set_page_config(
    page_title="Loan Approval App",
    layout="centered",
    page_icon="🏦"
)


# Background Image

bg_image_url = "https://static.vecteezy.com/system/resources/previews/024/269/235/non_2x/car-house-personal-money-loan-concept-finance-business-icon-on-wooden-cube-saving-money-for-a-car-money-and-house-wooden-cubes-with-word-loan-copy-space-for-text-loan-payment-car-and-house-photo.jpg"

st.markdown(f"""
    <style>
        .stApp {{
            background-image: url("{bg_image_url}");
            background-size: cover;
            background-attachment: fixed;
            background-repeat: no-repeat;
        }}
    </style>
""", unsafe_allow_html=True)


# Sidebar

st.sidebar.title("📌 Navigation")
st.sidebar.markdown("""
### 🏦 Loan Approval App  
Predict your loan approval using trained ML model.

---

### 📂 Sections  
- Applicant Information  
- Loan Information  
- Prediction Result  

---
""")


# GitHub Link Button

st.sidebar.markdown("### ⭐ Project Repository")

st.sidebar.markdown(
    """
    <a href='https://github.com/YOUR_USERNAME/YOUR_REPO' target='_blank'
        style='text-decoration:none;'>
        <button style='background-color:#24292E; color:white; padding:10px 18px;
            border:none; border-radius:8px; font-size:15px; cursor:pointer; width:100%;'>
            🔗 View on GitHub
        </button>
    </a>
    """,
    unsafe_allow_html=True
)




# Advanced CSS (Glass + Icons + Glow)

st.markdown("""
    <style>
        /* Main title */
        .main-title {
            background: linear-gradient(135deg, #4F46E5, #6D28D9);
            padding: 20px;
            border-radius: 14px;
            text-align: center;
            color: white;
            font-size: 32px;
            font-weight: bold;
            margin-bottom: 30px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.35);
        }

        /* Glassmorphism Box */
        .glass-box {
            background: rgba(255, 255, 255, 0.10);
            border-radius: 18px;
            padding: 25px;
            margin-bottom: 25px;
            border: 1px solid rgba(255, 255, 255, 0.3);
            backdrop-filter: blur(12px);
            box-shadow: 0 4px 18px rgba(0,0,0,0.25);
        }

        /* Section Title */
        .glass-title {
            font-size: 23px;
            font-weight: bold;
            margin-bottom: 18px;
            color: white;
            text-shadow: 0 0 6px rgba(0,0,0,0.5);
        }

        /* Predict button */
        .predict-button {
            width: 100%;
            background: linear-gradient(135deg, #4F46E5, #6D28D9);
            color: white !important;
            padding: 12px;
            border-radius: 12px;
            font-size: 20px;
            font-weight: bold;
            border: none;
            box-shadow: 0px 4px 15px rgba(79, 70, 229, 0.4);
        }

        .predict-button:hover {
            background: linear-gradient(135deg, #4338CA, #5B21B6);
            cursor: pointer;
        }

        /* Make success message dark */
        .stSuccess {
            background-color: #064E3B !important;
            color: white !important;
            padding: 12px !important;
            border-radius: 8px !important;
        }
    </style>
""", unsafe_allow_html=True)


# Load model

with open("loan_approval_model.pkl", "rb") as f:
    model, scaler, encoders = pickle.load(f)


# Title

st.markdown('<div class="main-title">🏦 Loan Approval Prediction App</div>', unsafe_allow_html=True)
st.markdown(
    "<h3 style='color: #4F46E5;'>Fill the details below to check if your loan will be approved:</h3>",
    unsafe_allow_html=True
)



# Applicant Section

st.markdown("""
<div class="glass-box">
    <h3 class="glass-title">👤 Applicant Information</h3>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])
    married = st.selectbox("Married", ["Yes", "No"])
    dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
    education = st.selectbox("Education", ["Graduate", "Not Graduate"])

with col2:
    self_employed = st.selectbox("Self Employed", ["Yes", "No"])
    applicant_income = st.number_input("Applicant Income", min_value=0)
    coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
    loan_amount = st.number_input("Loan Amount", min_value=0)


# Loan Info Section

st.markdown("""
<div class="glass-box">
    <h3 class="glass-title">💰 Loan Information</h3>
</div>
""", unsafe_allow_html=True)

col3, col4 = st.columns(2)

with col3:
    loan_amount_term = st.selectbox("Loan Amount Term (in months)", [12, 36, 60, 120, 180, 240, 300, 360, 480])

with col4:
    credit_history = st.selectbox("Credit History", [0, 1])
    property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])


# Create Data

df_input = pd.DataFrame({
    "Gender": [gender],
    "Married": [married],
    "Dependents": [dependents],
    "Education": [education],
    "Self_Employed": [self_employed],
    "ApplicantIncome": [applicant_income],
    "CoapplicantIncome": [coapplicant_income],
    "LoanAmount": [loan_amount],
    "Loan_Amount_Term": [loan_amount_term],
    "Credit_History": [credit_history],
    "Property_Area": [property_area],
})

# encoding
for col in df_input.columns:
    if col in encoders:
        df_input[col] = encoders[col].transform(df_input[col].astype(str))

# scaling
df_input_scaled = scaler.transform(df_input)


# Predict Button

st.markdown("<br>", unsafe_allow_html=True)

if st.button("🔍 Predict Loan Approval", type="primary"):
    pred = model.predict(df_input_scaled)[0]

    if pred == 1:
        st.success("🎉 **Loan Approved! Congratulations!**")
    else:
        st.error("❌ **Loan Rejected. Try Again After Improving Your Profile.**")
