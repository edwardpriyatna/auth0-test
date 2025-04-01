import streamlit as st
import joblib
import pandas as pd

# --- Authentication ---
st.title("Authentication")
if not st.experimental_user.is_logged_in:
    st.title("📔 Stroke Prediction Model Using Time Series Data")
    
    with st.container(border=True):
        try:
            st.image("./img/stroke-brain.gif", use_container_width=True)
        except Exception as e:
            st.warning(f"Could not load image: {e}")
    
    if st.button("✨ Sign up / Log in via Auth0", type="primary", key="auth0-login-button", use_container_width=True):
        st.login("auth0")
    
    with st.expander("📝 Privacy & Data Security Disclaimer"):
        st.markdown("""
        This app uses Auth0 for secure authentication. Your login credentials are handled and stored securely.
        - 🔒 Secure Storage: Your authentication data is protected.
        - 🚫 No Data Reuse: Your credentials will not be shared.
        If you have questions, contact [support](mailto:edwardpriyatnax@gmail.com).
        """)
    
    st.link_button("Find Any Bug?", url="https://github.com/andfanilo/streamlit-auth0-test/issues", icon=":material/bug_report:", type="tertiary")
else:
    # --- Post-login View ---
    st.json(st.experimental_user)
    st.header(f"Hello {st.experimental_user.name}")
    st.image(st.experimental_user.picture)
    
    # Load Model
    model = joblib.load("decision_tree_model.pkl")
    
    # Sidebar Navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Data Entry", "Stroke Self-Assessment"])
    st.session_state.page = page
    
    # Home Page
    if page == "Home":
        st.title("Welcome to the Healthcare Prediction System")
        st.write("This project predicts patient outcomes using machine learning.")
    
    # Data Entry Page
    elif page == "Data Entry":
        st.title("Patient Data Entry & ML Model Prediction")
        
        if "fields" not in st.session_state:
            st.session_state.fields = []
        
        uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
        if uploaded_file:
            df = pd.read_csv(uploaded_file)
            st.session_state.fields = df.to_dict(orient="records")
            st.success("CSV uploaded and data loaded.")
        
        if st.button("➕ Add Another Entry"):
            st.session_state.fields.append({
                "temperature": 0.0, "heartrate": 0.0, "resprate": 0.0, "o2sat": 0.0,
                "sbp": 0.0, "dbp": 0.0, "rhythm": 0, "pain": 0, "gender": 0,
                "anchor_age": 0, "anchor_year": 0, "anchor_year_group": 0,
                "year": 0.0, "month": 0.0, "day": 0.0, "hour": 0.0, "minute": 0.0, "second": 0.0
            })
        
        for i, field in enumerate(st.session_state.fields):
            with st.expander(f"Entry {i + 1}"):
                for key in field:
                    st.session_state.fields[i][key] = st.number_input(key.capitalize(), value=field[key])
        
        if st.button("Run ML Model"):
            if not st.session_state.fields:
                st.error("No entries to process.")
            else:
                input_df = pd.DataFrame(st.session_state.fields)
                prediction = model.predict(input_df.values)
                st.subheader("Model Prediction")
                st.write(f"Prediction: {prediction[0]}")
    
    # Stroke Self-Assessment Page
    elif page == "Stroke Self-Assessment":
        st.title("🩺 Stroke Risk Assessment")
        risk_factors = [
            "Is your blood pressure greater than 120/80 mmHg?",
            "Have you been diagnosed with atrial fibrillation?",
            "Is your blood sugar greater than 100 mg/dL?",
            "Is your body mass index greater than 25 kg/m²?",
            "Is your diet high in unhealthy fats or excess calories?",
            "Is your total blood cholesterol greater than 160 mg/dL?",
            "Have you been diagnosed with diabetes mellitus?",
            "Do you get less than 150 minutes of exercise per week?",
            "Do you have a family history of stroke or heart attack?",
            "Do you use tobacco or vape?"
        ]
        
        if "responses" not in st.session_state:
            st.session_state.responses = [None] * len(risk_factors)
        
        with st.form("stroke_assessment_form"):
            for i, factor in enumerate(risk_factors):
                st.session_state.responses[i] = st.radio(factor, ["Yes or unknown", "No"], key=f"q_{i}")
            submitted = st.form_submit_button("Submit")
        
        if submitted:
            risk_score = sum(1 for response in st.session_state.responses if response == "Yes or unknown")
            st.subheader("Total Score:")
            st.write(f"**{risk_score} points**")
            if risk_score >= 6:
                st.error("⚠️ High Risk: Consult a healthcare professional.")
            elif risk_score >= 3:
                st.warning("⚠️ Moderate Risk: Consider lifestyle changes.")
            else:
                st.success("✅ Low Risk: Maintain a healthy lifestyle.")
    
    if st.button("Log Out"):
        st.logout()