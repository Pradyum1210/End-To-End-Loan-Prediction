# 1️⃣ Loan Prediction Application 🏦

An end-to-end Loan Approval Prediction System built using **Python, Streamlit, SQL, and Machine Learning**.  
This application analyzes applicant information and predicts whether a loan should be **approved** or **rejected**, using a trained ML model stored as a `.pkl` file.

---

# 2️⃣ Live Demo 🚀

Run the App locally:  
👉 [http://localhost:8501/](http://localhost:8501/)

---

# 3️⃣ Project Overview 📌

This project demonstrates an end-to-end ML deployment pipeline, including:

| Step | Description |
|------|-------------|
| Data Collection | Applicant, Financial, and Loan Information (JSON format) |
| Data Processing & Cleaning | Handle missing values, normalize inputs, and validate data |
| Model Training | Python-based ML model (Logistic Regression / RandomForest) |
| Pickle File Generation | Save trained model as `loan_approval_model.pkl` |
| SQL Database Integration | Store customer and loan details, track prediction history |
| Streamlit Web Application | User-friendly interface for real-time loan approval prediction |
| Real-time Prediction | Predict loan approval instantly from user inputs |
| Frontend UI | Modern UI components with sidebar navigation and validation |

---

# 4️⃣ Machine Learning Model 🧠

| Feature | Description |
|---------|-------------|
| Algorithm | Logistic Regression / RandomForest |
| Trained on | Structured loan applicant data |
| Model Saved | `loan_approval_model.pkl` |

### Key Features Used for Prediction:
- Applicant Income  
- Loan Amount  
- Credit Score  
- Employment Status  
- Loan History  
- Financial Stability  

---

# 5️⃣ How the Model Works 🧪

1. User enters loan-related details in the Streamlit UI  
2. Data is validated and preprocessed  
3. ML model is loaded from `loan_approval_model.pkl`  
4. Prediction result (**Approved / Rejected**) is generated  
5. Result is displayed instantly on Streamlit UI  

---

# 6️⃣ SQL Database Integration 🗄️

| Database Action | Description |
|-----------------|-------------|
| Store Applicant Records | Save user input details for tracking |
| Store Loan Details | Track loan amounts, history, and status |
| Save Prediction History | Log predictions for audit and analysis |

---

# 7️⃣ Streamlit Web Application 🖥️

### Sidebar Navigation
- Applicant Information  
- Financial Information  
- Loan Information  
- Prediction Output  

### Modern UI Components
| Component | Usage |
|-----------|-------|
| Text Input | Enter applicant details and loan information |
| Dropdown | Select options like employment status or loan type |
| Slider | Adjust numerical inputs like income or loan amount |
| Button | Submit for prediction |
| Alerts | Display success or warning messages |

---

# 8️⃣ Screenshots 📸

<img width="1909" height="960" alt="Loan Prediction App Screenshot" src="https://github.com/user-attachments/assets/2a4cf23e-7dc3-4f7b-be37-bcf15d65481b" />

---

# 9️⃣ How to Run the Project

### Requirements
- Python 3.x  
- Streamlit  
- Pandas, NumPy, Scikit-learn  
- SQL Database (MySQL, SQLite, PostgreSQL)  


