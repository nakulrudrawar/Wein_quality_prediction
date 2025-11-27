import streamlit as st
import pickle
import numpy as np
import time

# Load model
model = pickle.load(open('wine_model.pkl', 'rb'))

# --- Page Config ---
st.set_page_config(page_title="🍷 Wine Quality Predictor", page_icon="🍇", layout="centered")

# --- CSS Styling ---
st.markdown("""
    <style>
        body {
            background-color: #faf3f3;
        }
        .main {
            background-color: #fff5f7;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0px 0px 15px rgba(150, 75, 0, 0.2);
        }
        h1 {
            text-align: center;
            color: #8B0000;
        }
        .stButton>button {
            background-color: #8B0000;
            color: white;
            border-radius: 10px;
            padding: 10px 24px;
            font-size: 16px;
        }
        .stButton>button:hover {
            background-color: #B22222;
            color: #fff;
        }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/4150/4150897.png", width=120)
st.sidebar.title("📘 About This Project")
st.sidebar.write("""
### 🍇 Wine Quality Prediction
This ML-based web app predicts whether a wine is **Good** or **Bad** based on its chemical properties.

### 🧠 Tools & Technologies
- Python  
- Scikit-learn  
- Streamlit  
- NumPy, Pickle

### 👨‍💻 Developer
**G6**  
MCA Student, Pune  
G H Raisoni College of Engineering and Management.
""")
st.sidebar.markdown("---")
st.sidebar.info("📢 Tip: Adjust the parameters to see how quality prediction changes!")

# --- Title Section ---
st.markdown("<h1>🍷 Wine Quality Prediction App</h1>", unsafe_allow_html=True)
st.write("Welcome to the **Wine Quality Predictor!** Fill in the wine parameters below and click on **Predict** to know the result.")

# --- Input Section ---
with st.container():
    st.subheader("🔢 Enter Wine Parameters")
    col1, col2, col3 = st.columns(3)

    with col1:
        fixed_acidity = st.number_input("Fixed Acidity", min_value=0.0, step=0.1)
        citric_acid = st.number_input("Citric Acid", min_value=0.0, step=0.1)
        chlorides = st.number_input("Chlorides", min_value=0.0, step=0.001)
        density = st.number_input("Density", min_value=0.0, step=0.0001)

    with col2:
        volatile_acidity = st.number_input("Volatile Acidity", min_value=0.0, step=0.1)
        residual_sugar = st.number_input("Residual Sugar", min_value=0.0, step=0.1)
        free_sulfur_dioxide = st.number_input("Free Sulfur Dioxide", min_value=0.0, step=1.0)
        pH = st.number_input("pH", min_value=0.0, step=0.01)

    with col3:
        total_sulfur_dioxide = st.number_input("Total Sulfur Dioxide", min_value=0.0, step=1.0)
        sulphates = st.number_input("Sulphates", min_value=0.0, step=0.01)
        alcohol = st.number_input("Alcohol (%)", min_value=0.0, step=0.1)

# --- Predict Button ---
st.markdown("### 🔍 Click below to get your prediction")
if st.button("✨ Predict Wine Quality"):
    features = np.array([[fixed_acidity, volatile_acidity, citric_acid,
                          residual_sugar, chlorides, free_sulfur_dioxide,
                          total_sulfur_dioxide, density, pH, sulphates, alcohol]])

    with st.spinner("🔮 Analyzing the wine... Please wait..."):
        time.sleep(2)  # Simulate model processing
        prediction = model.predict(features)

    st.markdown("---")

    # --- Attractive Output Section ---
    if prediction[0] == 1:
        st.balloons()
        st.markdown("""
        <div style='background-color:#ffe6e6; padding:20px; border-radius:15px; text-align:center;
                    box-shadow:0px 0px 10px rgba(0,0,0,0.1);'>
            <h2 style='color:#8B0000;'>🍇 Good Quality Wine!</h2>
            <p style='font-size:18px; color:#333;'>This wine is likely **enjoyable, smooth, and well-balanced**.  
            A perfect choice for fine dining or celebrations!</p>
        </div>
        """, unsafe_allow_html=True)
        st.progress(90)
        st.success("Quality Score: 9/10")

    else:
        st.markdown("""
        <div style='background-color:#fff0f0; padding:20px; border-radius:15px; text-align:center;
                    box-shadow:0px 0px 10px rgba(0,0,0,0.1);'>
            <h2 style='color:#B22222;'>🍷 Low Quality Wine</h2>
            <p style='font-size:18px; color:#333;'>This wine may need **improvement in taste or composition**.  
            Try adjusting acidity, sulphates, or alcohol levels.</p>
        </div>
        """, unsafe_allow_html=True)
        st.progress(40)
        st.error("Quality Score: 4/10")

    st.markdown("---")

# --- Footer ---
st.markdown("""
<hr>
<p style="text-align:center; color:gray;">
Developed by <b>G6</b> | Streamlit + ML | Pune
</p>
""", unsafe_allow_html=True)
